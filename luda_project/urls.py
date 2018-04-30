"""luda_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
import luda.views
from kmucafe.views import keyboard, answer, crawl
import word.views
import photos.views
from django.views.generic import TemplateView


urlpatterns = [
    path('up/', include(('photos.urls', 'photos'), namespace='photos')),
    path('admin/', admin.site.urls),
    path('', include('luda.urls'), name='luda'),
    path('image_full/', luda.views.image, name='image'),
    path('gif_full/', luda.views.gif, name='gif'),
    path('new_update_image_and_gif/', luda.views.refresh, name='refresh'),
    path('keyboard/', keyboard, name='keyboard'),
    path('message', answer, name='answer'),
    path('crawl/', crawl, name='crawl'),
    path('word/', word.views.word, name='word'),
    path('word_update/', word.views.update, name='update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)

