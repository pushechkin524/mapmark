from rest_framework import serializers
from .models import Marker, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'image', 'order')

class MarkerSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False, max_length=3
    )

    class Meta:
        model = Marker
        fields = ('id', 'title', 'description', 'latitude', 'longitude', 'photos', 'images', 'created_at')

    def validate_images(self, value):
        if len(value) > 3:
            raise serializers.ValidationError('Максимум 3 фотографии.')
        return value

    def create(self, validated_data):
        images = validated_data.pop('images', [])
        marker = Marker.objects.create(**validated_data)
        for idx, img in enumerate(images):
            Photo.objects.create(marker=marker, image=img, order=idx)
        return marker
