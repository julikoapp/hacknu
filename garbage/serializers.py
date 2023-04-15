from rest_framework import serializers

from garbage import models


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ('id', 'email', 'name', 'phone', 'address', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
                'min_length': 8
            }
        }
        
    def create(self, validated_data):
        """Create and return new user"""
        user = models.Client.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            phone = validated_data['phone'],
            address = validated_data['address'],
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
        fields = '__all__'
        # fields = ('id', 'status', 'category', 'description', 'created_at', 'updated_at', 'address') # Add these: 'client', 'brigada')
    
    # def create(self, validated_data):
    #     """ Create a new operator """
    #     task = models.Task.objects.create_task(
    #         category = validated_data['category'],
    #         status = 1,
    #         description = validated_data['description'],
    #         created_at = datetime.datetime.now(),
    #         updated_at = datetime.datetime.now(),
    #         address = validated_data['address'],
    #        # client = validated_data['client'],
    #        # brigada = None
    #     )
    #     return task

    # def update(self, instance, validated_data):
    #     # TODO update the status how? 
    #     # TODO update the brigada that will do it
    #     instance.updated_at = datetime.datetime.now()

