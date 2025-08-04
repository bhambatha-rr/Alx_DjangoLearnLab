from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Add this import
from django.conf.urls.static import static # Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationships/', include('relationship_app.urls')),
    path('bookshelf/', include('bookshelf.urls')),
]

# Add this line to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
