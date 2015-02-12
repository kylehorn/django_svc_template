from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from user_profile import views as user_views

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/signup/', 'user_profile.views.signup', name='api-signup'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/v1/', include('oauth2_provider.urls',
        namespace='oauth2_provider')),
    url(r'^admin/', include(admin.site.urls)),
)
