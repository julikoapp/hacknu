from rest_framework import serializers

from garbage import models

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ('id', 'email', 'name', 'phone', 'address', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
        
    def create(self, validated_data):
        """Create and return new user"""
        user = models.Client.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Task
		fields = ('id', 'status', 'category', 'description', 'created_by', 'created_at', 'updated_at')


  