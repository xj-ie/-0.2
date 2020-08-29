import re

from rest_framework import serializers

from users.models import User


class UerShow(serializers.ModelSerializer):
    class Meta:
        model = User
        # exclude =
        fields = ('id', 'username', 'mobile', 'email', 'password')

        extra_kwargs = {
                            "username":{
                                'max_length': 20,
                                'min_length': 5
                            },
                            "password":{
                                'max_length':20,
                                'min_length':8,
                                'write_only': True
                            },

                       }
    def validate_mobile(self, attrs):
        if not re.match(r'1[3-9]\d{9}',attrs):


            raise serializers.ValidationError('手机号不正确')

        return attrs
    def create(self, validated_data):
        # user = super().create(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
