from rest_framework import serializers

from authapp.models import Userinfo

class UserinfoSerializer(serializers.ModelSerializer):
   class Meta:
       model = Userinfo
       fields = ('Email','Password')


