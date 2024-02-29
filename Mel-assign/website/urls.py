from django.contrib import admin
from django.urls import path
from commerce.views import home, about, contacts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', home, name= 'home'),
    path('about/', about, name= 'about'),
    path('contacts/', contacts, name= 'contact'),
    path('product/', product, name='product'),
    # Other URL patterns...

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
