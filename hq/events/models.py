from django.db import models

# Create your models here.


class events_list(models.Model):
    event_organizer_id = models.AutoField( primary_key = True)
    event_organizer = models.CharField(max_length = 30)
    event_description = models.TextField(max_length = 255)
    event_post_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "events"

    def __str__(self):
        return self.event_description
