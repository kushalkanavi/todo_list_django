from django.conf.urls import url
from .views import index, saveTaskInfo, tasksearch, taskfilter, edittask

urlpatterns = [
	url(r'^saveTaskInfo/', saveTaskInfo.as_view(),name='saveTaskInfo'),
	url(r'^edittask/(?P<id>\d+)/$', edittask.as_view(),name='edittask'),
	url(r'^tasksearch/', tasksearch, name='tasksearch'),
	url(r'^taskfilter/', taskfilter, name='taskfilter'),

    url(r'^$', index.as_view(),name='index'),
]