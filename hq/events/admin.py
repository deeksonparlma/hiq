from django.contrib import admin

# Register your models here.

from .models import events_list


class event_display(admin.ModelAdmin):
    class Meta:
        model = events_list
        fields = ["event_id","event_organizer","event_description","event_post_date"]

admin.site.register(events_list,event_display)
