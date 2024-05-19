from django.urls import path
from drf_yasg import openapi
from .views import *
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view


class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):

        swagger = super().get_schema(request, public)
        swagger.tags = [

            {
                "name": "car",
                "description": "Get car by car id"
            },
            {
                "name": "cars",
                "description": "Get all cars"
            },
        ]

        return swagger


schema_view = get_schema_view(
    openapi.Info(
        title="Swagger documentation",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
    generator_class=CustomOpenAPISchemaGenerator,
)


urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='signup'),

    path('userprofile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='userprofile-list'),
    path('userprofile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='userprofile-detail'),

    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category-detail'),

    path('carmake/', CarMakeViewSet.as_view({'get': 'list', 'post': 'create'}), name='carmake-list'),
    path('carmake/<int:pk>/', CarMakeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='carmake-detail'),

    path('model/', ModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='model-list'),
    path('model/<int:pk>/', ModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='model-detail'),

    path('car/', CarViewSet.as_view({'get': 'list', 'post': 'create'}), name='car-list'),
    path('car/<int:pk>/', CarViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='car-detail'),

    path('bet/', BetViewSet.as_view({'get': 'list', 'post': 'create'}), name='bet-list'),
    path('bet/<int:pk>/', BetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='bet-detail'),

    path('comment/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('comment/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment-detail'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
