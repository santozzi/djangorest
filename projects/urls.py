from rest_framework import routers
from .api import ProjectViwset
router = routers.DefaultRouter()

router.register('api/projects', ProjectViwset, 'projects')
urlpatterns = router.urls