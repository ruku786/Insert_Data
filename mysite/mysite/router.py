from myapp.viewsets import employeeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', employeeViewset)