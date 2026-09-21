
from rest_framework.routers import DefaultRouter
from apps.maintenance.views import MaintenanceViewSet

router = DefaultRouter()

router.register(
    "maintenances",
    MaintenanceViewSet,
    basename="maintenance"
)

urlpatterns = router.urls


