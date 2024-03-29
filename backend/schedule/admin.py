from django.contrib import admin

from .models import Event 


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['start', 'id','route_display', 'end', 'remaining_seats', 'total_seats', 'status']
    list_filter = ['start', 'status']


    def route_display(self, obj):
        return str(obj.route.name)