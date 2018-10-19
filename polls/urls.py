from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # added the word 'specifics'
    url(r'^(?P<question_id>[a-z\d]+)/$', views.detail, name='detail'),
    # ex: /polls/54c69fdd44ae8acdff264464/results/
    url(r'^(?P<pk>[a-z\d]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/54c69fdd44ae8acdff264464/vote/
    url(r'^(?P<question_id>[a-z\d]+)/vote/$', views.vote, name='vote'),
    )

