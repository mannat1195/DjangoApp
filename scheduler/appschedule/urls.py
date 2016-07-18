from django.conf.urls import url

from . import views

app_name='appschedule'
urlpatterns=[
	url(r'^index/$',views.IndexView.as_view(),name='index'),
        url(r'^index/detail/$',views.DetailView.as_view(),name='detail'),
        url(r'^index/detail/results/$',views.ResultView.as_view(),name='results'),
]