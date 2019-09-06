from rest_framework import serializers
from .models import Profile, Project, Assign, Announce

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'profile_pic', 'bio','contacts')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'description', 'image', 'url', 'user', 'pub_date')
class AssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assign
        fields = ('topic', 'description', 'image', 'url', 'user', 'pub_date')
class AnnounceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announce
        fields = ('title', 'description', 'image', 'url', 'user', 'pub_date')