from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

urlpatterns = [
    # 管理后台路由
    path('admin/', admin.site.urls),
    # 媒体media资源的路由信息
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    # 导向App(index)之路由
    path('', include(('index.urls', 'index'), namespace='index')),
    path('commodity', include(('commodity.urls', 'commodity'), namespace='commodity')),
    path('shopper', include(('shopper.urls', 'shopper'), namespace='shopper'))
]
