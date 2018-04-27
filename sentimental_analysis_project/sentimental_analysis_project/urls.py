from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from sentimental_analysis_app import views
urlpatterns = [
    url(r'^$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^charts/$', views.get_percentages_of_different_sentiments, name='sentiments'),
    url(r'^admin/', admin.site.urls),
]