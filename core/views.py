from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
import string
import random
from django.core.mail import send_mail
from django.conf import settings
from uuid import uuid4
from .cache import CacheService

User = get_user_model()


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
       return ''.join(random.choice(chars) for _ in range(size))



class UserCreationViewSet(ModelViewSet):
     serializer_class =  UserSerializer

     @classmethod
     def sendEmail(cls, instance, uuid):
          subject = 'welcome to Hossein and Amin world'
          message = f'{instance.first_name}, thank you for registering in Sotoon, uuid : {uuid}.'
          email_from = settings.EMAIL_HOST_USER
          recipient_list = [instance.email]
          send_mail( subject, message, email_from, recipient_list )

     def get_serializer_context(self):
         username = id_generator()
         return {'username':username}

     def get_queryset(self):
         return User.objects.all()     

     def perform_create(self, serializer):
         instance = serializer.save()
         uuid = uuid4()
         CacheService.cache_user_id(uuid, instance.id)
         self.sendEmail(instance, uuid)
         
         




# I have to make this flow better and send email afte user created not before but for pace of proccess ignore it now


     
