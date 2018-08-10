# from django.urls import path
from django.conf.urls import url
from movies.views import UserList, CreateSubscription, MoviesList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^movies/', MoviesList.as_view()),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<user_id>[0-9]+)/subscription/$', CreateSubscription.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
