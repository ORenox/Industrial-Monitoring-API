from rest_framework.routers import DefaultRouter
from apps.measurements.views import MeasurementViewSet

router = DefaultRouter()

router.register(
    "measurements",
    MeasurementViewSet,
    basename="measurement"
)

urlpatterns = router.urls