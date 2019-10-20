from django.contrib import admin
from .models import Realtor


# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'email', 'hire_date')  # Add extra table field in the Realtor page
    list_display_links = ('id', 'name')  # Adding extra functionality to redirect the links in Realtor page
    search_fields = ('name',)  # Adding search functionality on given fields
    list_per_page = 25  # Adding Pagination


admin.site.register(Realtor, RealtorAdmin)
