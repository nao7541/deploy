"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apiv1.views import TwitterLogin, FacebookLogin


API_TITLE = 'Application API'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apiv1.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('dj_rest_auth.urls')),
    path('api/v1/', include('rest_auth.urls')),
    # ユーザー登録
    path('api/v1/registration/', include('dj_rest_auth.registration.urls')),
    # ソーシャルアカウントでのログイン
    path('api/v1/login/twitter/', TwitterLogin.as_view(), name='twitter_login'),
    path('api/v1/login/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('accounts/', include('allauth.urls'), name='socialaccount_signup'),
]

# 画像をアップロードするための設定
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
