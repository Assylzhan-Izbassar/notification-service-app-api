"""
Constructing urls for Notification App models.
"""
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('distributions', views.DistributionViewSet)
router.register('clients', views.ClientViewSet)
router.register('messages', views.MessageViewSet)


urlpatterns = router.urls
