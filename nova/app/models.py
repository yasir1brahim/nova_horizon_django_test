from django.db import models

class AccountStage(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  # Assuming 'id' is unique
    team_id = models.CharField(max_length=50)
    display_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    display_order = models.FloatField()
    default_exclude_for_leadgen = models.BooleanField(default=False)
    category = models.CharField(max_length=50)
    is_meeting_set = models.BooleanField(null=True)

    def __str__(self):
        return self.name
