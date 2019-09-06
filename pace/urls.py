from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project/(\d+)$', views.project, name='project'),
    url(r'^assign/(\d+)$', views.assign, name='assign'),
    url(r'^announce/(\d+)$', views.announce, name='announce'),
    url(r'^upload/$', views.upload_site, name='upload'),
    url(r'^uploadassign/$', views.upload_assign, name='uploadassign'),
    url(r'^uploadannounce/$', views.upload_announce, name='uploadannounce'),
    url(r'^profile/(?P<username>\w{0,50})/$', views.profile, name='profile'),
    url(r'^update_profile/(\d+)$', views.update_profile, name='update_profile'),
    url(r'^search/$', views.search, name='search_results'),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/assigns/$', views.AssignList.as_view()),
    url(r'^api/announce/$', views.AnnounceList.as_view()),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)