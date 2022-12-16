from rest_framework import serializers


class StudentCourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    num = serializers.CharField(max_length=7, min_length=None, allow_blank=False, trim_whitespace=True)
    full_name = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    topic_selection = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    selecting_sources = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    carrying_reserch = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    shaping_work = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    making = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    defending = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)