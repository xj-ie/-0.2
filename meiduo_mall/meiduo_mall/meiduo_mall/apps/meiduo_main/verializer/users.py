from rest_framework import serializers

from users.models import User


class UerShow(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('id','username', 'email', 'mobile')
        # exclude =
        fields = ('id', 'username', 'mobile', 'email')
