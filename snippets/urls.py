from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = [
    # url(r'^$', views.snippet_list),
    # url(r'^(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^$', views.SnippetList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
