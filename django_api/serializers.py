from rest_framework import serializers
from courses.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        # fields = '__all__'
        fields = ['id', 'title', 'description', 'language', 'created_at']
        read_only_fields = ['created_at']

    @staticmethod
    def validate_title(value):
        if len(value) < 10:
            raise serializers.ValidationError('Course title must be at least 10 characters long')
        return value






