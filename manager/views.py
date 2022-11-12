from rest_framework.viewsets import ModelViewSet
from .models import Role, EmployeeProfile, Salary
from .serializers import RoleSerializer, PostEmployeeProfileSerializer, GetEmployeeProfileSerializer,SalarySerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from core.cache import CacheService
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import AuthenticationFailed
from .permissions import  IsHrManager, IsPayRollManager, IsHrOrPayRollManager
from rest_framework import permissions

class SalaryViewSet(ModelViewSet):
    serializer_class =  SalarySerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS: 
            return [IsAuthenticated()]
        return [IsPayRollManager()]



    def get_queryset(self):
         return Salary.objects.filter(employee_id = self.kwargs['employee_pk'])         

    def get_serializer_context(self):
         return {'employee_id': self.kwargs['employee_pk']}



class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer



class EmployeeProfileListViewSet(ModelViewSet):

    http_method_names = ['get', 'put', 'patch']
    queryset = EmployeeProfile.objects.prefetch_related('salary').all()
    serializer_class = GetEmployeeProfileSerializer



    def get_permissions(self):
        if self.request.method == 'GET' :
                return [IsHrOrPayRollManager()]
        else :
                return [IsHrManager()]



    def get_serializer_context(self):
        if self.request.method != 'GET' : 
            user_id = EmployeeProfile.objects.get(id=self.kwargs['pk']).user.id
            return {'user_id': user_id}
        else :
            return super().get_serializer_context()



class EmployeeProfileCreateAPIView(CreateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = PostEmployeeProfileSerializer
                  

    def get_serializer_context(self):
        cach_service = CacheService()
        uuid = self.kwargs['uid']
        user_id = cach_service.get_user_id(uuid)
        return {'user_id': user_id}



class EmployeeAPIView(RetrieveUpdateAPIView):
    serializer_class = GetEmployeeProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
          return  EmployeeProfile.objects.all()

    def get_serializer_context(self):
          return {'user_id': self.request.user.id}

    def get_object(self):
        queryset = self.get_queryset()
        if self.request.user.is_anonymous :
            raise AuthenticationFailed('your not logged in as user')
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


# in the task , simple employee just can to view his/er profile 


        

    


