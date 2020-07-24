from rest_framework import serializers
from . import models


class ProfileSerializer(serializers.ModelSerializer):
    """Serializes the data sent to the profiles viewset api"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password',)
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
    
    def create(self, validated_data):
        """Creates and return new user"""
        user = models.UserProfile.objects.create_user(email=validated_data['email'], name=validated_data['name'], password=validated_data['password'])

        return user


class ProfileFeedSerializer(serializers.ModelSerializer):
    """Serializes JSON data into a ProfileFeedItem object"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'status_text', 'user_profile', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}