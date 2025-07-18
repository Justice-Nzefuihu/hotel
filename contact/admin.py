from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'email', 'Contact_date')
    list_display_links = ('id', 'firstname')
    search_fields = ('firstname', 'email')
    list_filter = ('Contact_date',)
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)