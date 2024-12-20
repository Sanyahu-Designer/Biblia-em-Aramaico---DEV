from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from bible_app.views.auth_views import CustomLogoutView
from bible_app.views.cache_monitor import cache_dashboard

admin.site.site_header = 'Evangelhos Aramaico Siriaco'
admin.site.site_title = 'Evangelhos Aramaico Siriaco'
admin.site.index_title = 'Administração'

urlpatterns = [
    path('admin/logout/', CustomLogoutView.as_view(), name='admin_logout'),
    path('admin/cache-monitor/', cache_dashboard, name='admin_cache_dashboard'),
    path('admin/', admin.site.urls),
    path('', include('bible_app.urls', namespace='bible_app')),    
    path('dictionary/', include('dictionary_app.urls', namespace='dictionary_app')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
