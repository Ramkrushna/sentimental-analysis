from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from sentimental_analysis_app import views
urlpatterns = [
    url(r'^$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^admin/', admin.site.urls),
    url(r'^q1/$', views.get_percentages_of_different_sentiments, name='sentiments'),
    url(r'^q2/$', views.get_percentages_of_different_sentiments, name='sentiments'),
    url(r'^q3/$', views.get_percentages_of_different_sentiments, name='sentiments'),
    url(r'^q4/$', views.get_percentages_of_different_sentiments, name='sentiments'),
    url(r'^q5/$', views.get_percentages_of_different_sentiments, name='sentiments'),
    url(r'^q6/$', views.get_percentages_of_different_sentiments, name='sentiments'),
    url(r'^q7/$', views.get_percentages_of_different_sentiments, name='sentiments'),
]