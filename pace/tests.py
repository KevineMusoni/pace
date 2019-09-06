from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project, Profile, Review

# Create your tests here.
class ProjectTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.project = Project(id=1, image = 'path/to/image',title='test',description='test caption',url='path/to/project',user=self.user)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project))

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile(profile_pic='images/pic', bio='I love cheese', contacts='+254712345678', user = self.user)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

class ReviewTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile(profile_pic='images/pic', bio='I love cheese', contacts='+254712345678', user = self.user)
        self.profile.save()
        self.project = Project(id=1, image = 'path/to/image',title='test',description='test caption',url='path/to/project',user=self.user)
        self.project.save()
        self.review = Review(id=1,project=self.project,design=10,usability=10,content=10,average=7,user=self.user)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.review,Review))