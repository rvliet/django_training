from django.contrib import admin
from .models import Project

# Enables the admin site to show project
admin.site.register(Project)
