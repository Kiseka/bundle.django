
from rest_framework import serializers
from .models import Todo
class TodoSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=True)
    status = serializers.CharField(required=False)
    description = serializers.CharField(allow_blank=True)

    def validate_title(self, title):
        if len(title) <10:
            raise serializers.ValidationError("Title Length should be greater than 5 characters ")
        return title
    
    class Meta:
        model = Todo
        fields = ['id',"user_id","title","description","status","created_at","updated_at"]


class TodoStatusSerializer(serializers.Serializer):
    status =serializers.CharField(required=True)
    description = serializers.CharField(required=True)
        
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
