# from rest_framework_nested import routers
# from . import views
# from .views import user_creation
# from django.urls import path


# urlpatterns = [
#     path('', views.user_creation),

# ]


from rest_framework_nested import routers
from . import views
from .views import UserCreationViewSet



router = routers.DefaultRouter()
router.register('', views.UserCreationViewSet, basename='users')

urlpatterns = router.urls 

