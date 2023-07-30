from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from aluraflix.views import ProgramaViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Aluraflix",
        default_version="v1",
        description="Provedor de séries e filmes desenvolvida no curso de Django Rest",
        terms_of_service="#",
        contact=openapi.Contact(email="brevefelipe@gmail.com"),
        license=openapi.License(name="Felipe Breve")
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('programas', ProgramaViewSet, basename='programas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name="schema-redoc"),
    path('', include(router.urls)),
]
