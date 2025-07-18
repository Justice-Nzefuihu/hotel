from django.contrib import admin
from .models import Rooms

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'capacity')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('bed',)
    list_per_page = 25

admin.site.register(Rooms, RoomAdmin)