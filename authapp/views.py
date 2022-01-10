from django.shortcuts import render
from authapp.models import Userinfo
from rest_framework.views import APIView 
from authapp.forms import UserLoginForm
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework import viewsets
from authapp.serializers import UserinfoSerializer

# Create your views here.



class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = Userinfo.objects.get(Email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(Password):
                return user
        return None




class UserinfoViewSet(viewsets.ModelViewSet):
   queryset = Userinfo.objects.all()
   serializer_class = UserinfoSerializer


def Index(request):
	return render(request, 'authapp/index.html')


def Login(request):
	form = UserLoginForm()
	if request.method=="POST":
		form=UserLoginForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request, 'authapp/login.html', {'form':form})

from rest_framework.views import APIView




