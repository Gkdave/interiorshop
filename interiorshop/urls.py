
# gajendra    dave@123
# bhawana     admin@123
# himanshu    gajendra@12
# ravindra    admin@12

from django.conf import settings 
from django.contrib import admin
from django.urls import path,include 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vendors/',include('shop.vendor.urls')),
    path('',include('shop.core.urls')),
    path('',include('shop.product.urls'))
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
