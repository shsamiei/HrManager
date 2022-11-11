from rest_framework.viewsets import ModelViewSet
from .models import Role, EmployeeProfile, Salary
from .serializers import RoleSerializer, PostEmployeeProfileSerializer, GetEmployeeProfileSerializer,SalarySerializer
from rest_framework.generics import CreateAPIView


class SalaryViewSet(ModelViewSet):
    serializer_class =  SalarySerializer

    def get_queryset(self):
         return Salary.objects.filter(employee_id = self.kwargs['employee_pk'])         

    def get_serializer_context(self):
         return {'employee_id': self.kwargs['employee_pk']}


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class EmployeeProfileViewSet(ModelViewSet):
    http_method_names = ['get', 'put', 'patch']
    queryset = EmployeeProfile.objects.prefetch_related('salary').all()
    serializer_class = GetEmployeeProfileSerializer




class EmployeeProfileCreateAPIView(CreateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = PostEmployeeProfileSerializer


    def get_serializer_context(self):
        return {'user_id': self.kwargs['uid']}




