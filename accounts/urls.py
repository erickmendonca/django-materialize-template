from django.conf.urls import include, url, patterns
from accounts import views

urlpatterns = patterns(
    '',
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^change-language/$', views.change_language, name='change_language'),
)
