from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.apollo import get_account_stages, create_account_stage_on_apollo
from app.models import AccountStage
from .serializers import AccountStageSerializer


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FetchAccountStagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = get_account_stages()  # Make sure this function is correctly fetching data
        stages = data.get('account_stages', [])

        for stage in stages:
            AccountStage.objects.update_or_create(
                id=stage['id'],
                defaults={
                    'team_id': stage['team_id'],
                    'display_name': stage['display_name'],
                    'name': stage['name'],
                    'display_order': stage['display_order'],
                    'default_exclude_for_leadgen': stage['default_exclude_for_leadgen'],
                    'category': stage['category'],
                    'is_meeting_set': stage['is_meeting_set'],
                }
            )

        serialized_stages = AccountStageSerializer(AccountStage.objects.all(), many=True)
        return Response({'success': True, 'message': 'Successfully fetched and stored account stages', 'stages': serialized_stages.data},  status=status.HTTP_200_OK)
    


class CreateAccountStageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AccountStageSerializer(data=request.data)
        if serializer.is_valid():

            # Call the function to create an account stage on Apollo
            apollo_response = create_account_stage_on_apollo(serializer.validated_data)

            if apollo_response.status_code == 201:  # Check for success
                account_stage = serializer.save()  # Save the new account stage locally
                return Response({'success': True, 'id': account_stage.id}, status=status.HTTP_201_CREATED)
            else:
                return Response(apollo_response.json(), status=apollo_response.status_code)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
