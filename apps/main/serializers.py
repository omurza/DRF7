from rest_framework import serializers
from .models import UsersModel , TaskModel
from rest_framework import validators

class UsersSerializer(serializers.Serializer):
    model=UsersModel
    fields='__all__'


class TaskSerializer(serializers.Serializer):
    model=TaskModel
    fields='__all__'
    

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, write_only=True)
    confirm_password = serializers.CharField(max_length=30, write_only=True)
    class Meta:
        model = UsersModel
        fields = ['id', 'username', 'email', 'phone', 'address', 'password', 'confirm_password']

    def create(self, validated_data): 
        user = TaskModel.objects.create(
            username=validated_data['username'], 
            email=validated_data['email'],
            phone=validated_data['phone_number'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate(self, attrs):
        if attrs['phone'] == attrs[str]:
            raise serializers.ValidationError({'phone': "введите цифры"})
        if len(attrs['phone']) < 12:
            raise serializers.ValidationError({'password': "Минимум 12 символов"})
        if +996 in (attrs,['phone']):

        else:
            raise serializers.ValidationError({'password': "Минимум 12 символов"})
        return attrs