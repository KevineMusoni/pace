from django.shortcuts import render, redirect
from .forms import UploadSiteForm,UploadAssignForm,UploadAnnounceForm, ReviewForm, UpdateProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, Project,Assign,Announce, Review
from django.urls import reverse
from django.db.models import Avg
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer,AssignSerializer,AnnounceSerializer

# Create your views here.
def index(request):
    if User.objects.filter(username = request.user.username).exists():
        user = User.objects.get(username=request.user)
        if not Profile.objects.filter(user = request.user).exists():
            Profile.objects.create(user = user)   
    projects = Project.objects.order_by('-pub_date')
    assigns = Assign.objects.order_by('-pub_date')
    announces = Announce.objects.order_by('-pub_date')
    return render(request,"index.html",{"projects":projects ,"assigns":assigns, "announces":announces})

def project(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user)
    project = Project.objects.get(id = id)
    reviews = Review.objects.filter(project = project)
    design = reviews.aggregate(Avg('design'))['design__avg']
    usability = reviews.aggregate(Avg('usability'))['usability__avg']
    content = reviews.aggregate(Avg('content'))['content__avg']
    average = reviews.aggregate(Avg('average'))['average__avg']
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.average = (review.design + review.usability + review.content) / 3
            review.project = project
            review.user = user
            review.save()
        return redirect('project', id)
    else:
        form = ReviewForm()
    return render(request, 'project.html', {'project': project, 'reviews': reviews, 'form': form, 'design': design, 'usability': usability, 'content': content, 'average': average})



def assign(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user)
    assign = Assign.objects.get(id = id)
    return render(request, 'assign.html', {'assign': assign})

def announce(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user)
    announce = Announce.objects.get(id = id)
    # reviews = Review.objects.filter(announce = announce)
    # design = reviews.aggregate(Avg('design'))['design__avg']
    # usability = reviews.aggregate(Avg('usability'))['usability__avg']
    # content = reviews.aggregate(Avg('content'))['content__avg']
    # average = reviews.aggregate(Avg('average'))['average__avg']
    # if request.method == 'POST':
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         review = form.save(commit=False)
    #         review.average = (review.design + review.usability + review.content) / 3
    #         review.announce = announce
    #         review.user = user
    #         review.save()
    #     return redirect('announce', id)
    # else:
    #     form = ReviewForm()
    return render(request, 'announce.html', {'announce': announce})


def search(request):
    if 'site' in request.GET and request.GET['site']:
        search_term = request.GET.get('site')
        projects = Project.objects.filter(title__icontains = search_term)
        message = f'{search_term}'
        return render(request, 'search.html', {'projects': projects, 'message': message})
        
    return render(request, 'search.html')

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

class AssignList(APIView):
    def get(self, request, format=None):
        all_assigns = Assign.objects.all()
        serializers = AssignSerializer(all_assigns, many=True)
        return Response(serializers.data)
class AnnounceList(APIView):
    def get(self, request, format=None):
        all_announces = Announce.objects.all()
        serializers = AnnounceSerializer(all_announces, many=True)
        return Response(serializers.data)

@login_required(login_url='/accounts/login/')
def upload_site(request):
    if request.method == 'POST':
        form = UploadSiteForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
        return redirect('index')
    else:
        form = UploadSiteForm()

    return render(request, 'upload.html', {'form': form})

@login_required(login_url='/accounts/login/')
def upload_assign(request):
    if request.method == 'POST':
        form = UploadAssignForm(request.POST, request.FILES)
        if form.is_valid():
            assign = form.save(commit=False)
            assign.user = request.user
            assign.save()
        return redirect('index')
    else:
        form = UploadAssignForm()

    return render(request, 'uploadassign.html', {'form': form})

@login_required(login_url='/accounts/login/')
def upload_announce(request):
    if request.method == 'POST':
        form = UploadAnnounceForm(request.POST, request.FILES)
        if form.is_valid():
            announce = form.save(commit=False)
            announce.user = request.user
            announce.save()
        return redirect('index')
    else:
        form = UploadAnnounceForm()

    return render(request, 'uploadannounce.html', {'form': form})

def profile(request, username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)
    projects = Project.objects.filter(user = user)
    assigns = Assign.objects.filter(user = user)
    return render(request, 'profile.html', {'profile': profile, 'projects': projects, 'assigns': assigns})

@login_required(login_url = '/accounts/login/')
def update_profile(request, id):
    if request.method == 'POST':
        profile = Profile.objects.get(id = id)
        form = UpdateProfile(request.POST or None, request.FILES or None, instance = profile)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            return redirect('profile', username = request.user)
    else:
        form = UpdateProfile()

    return render(request, 'update_profile.html', {'form': form})

