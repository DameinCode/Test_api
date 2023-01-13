from django.contrib import admin
from .models import Application
# Register your models here.

# class OrderAdmin(admin.ModelAdmin):
    # list_display = {'id', 'description', 'title', 'date', 'status'}
    # search_fields = {'id', 'title'}
    # list_editable = {'status', }
    # list_filter = {'status', 'date', }

admin.site.register(Application)
