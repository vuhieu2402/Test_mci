

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/customers/', include('customers.urls')),
    path('api/products/', include('products.urls')),
    path('api/employees/', include('employees.urls')),
    path('api/tasks/', include('taskboard.urls')),
    path('api/account/', include('accounts.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
