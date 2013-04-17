from django.conf.urls import patterns, url
from communities import views

urlpatterns = patterns('',

    url(r'^$', views.CommunityDetailView.as_view(), name='community'),

    url(r'^upcoming/$', views.UpcomingMeetingView.as_view(),
        name='upcoming_meeting'),

    url(r'^upcoming/publish/$', views.PublishMeetingView.as_view(),
        name="upcoming_publish"),

)