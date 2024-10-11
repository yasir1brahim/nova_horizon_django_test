from django.urls import path
from .views import CustomAuthToken, FetchAccountStagesView, CreateAccountStageView

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('create_account_stage/', CreateAccountStageView.as_view(), name='create_account_stage'),
    path('fetch_account_stages/', FetchAccountStagesView.as_view(), name='fetch_account_stages'),
]
