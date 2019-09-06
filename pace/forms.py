from django import forms
from .models import Project, Assign,Announce, Review, Profile
class UploadSiteForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','pub_date']

class UploadAssignForm(forms.ModelForm):
    class Meta:
        model = Assign
        exclude = ['user','pub_date']

class UploadAnnounceForm(forms.ModelForm):
    class Meta:
        model = Announce
        exclude = ['user','pub_date']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['average','project', 'assign', 'announce', 'user']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']