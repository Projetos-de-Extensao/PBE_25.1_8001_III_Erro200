from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger/OpenAPI config
schema_view = get_schema_view(
   openapi.Info(
      title="API de Produtos",
      default_version='v1',
      description="API para gerenciamento de produtos",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@empresa.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs tradicionais da sua aplicação (HTML)
    path('', include('myapp.urls')),

    # URLs da API REST
    path('api/', include('myapp.api_urls')),

    # Autenticação da API REST
    path('api-auth/', include('rest_framework.urls')),

    # Documentação Swagger e Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
