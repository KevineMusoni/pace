from django.contrib import admin
from .models import Profile, Project,Assign,Announce, Review

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Assign)
admin.site.register(Announce)
admin.site.register(Review)