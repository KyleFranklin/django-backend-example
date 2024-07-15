from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'password']  # Specify only the fields you want to include

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']

        # Create the user object
        user_obj = UserModel.objects.create_user(
            username=username,
            password=password
        )

        return user_obj

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise ValidationError('Invalid username or password.')

        else:
            raise ValidationError('Both username and password are required.')

        return data
    def check_user(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise ValidationError('User not found.')

        else:
            raise ValidationError('Both username and password are required.')

        return user

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = ('username', 'password')