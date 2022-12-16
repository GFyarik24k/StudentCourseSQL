from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentCourseSerializer
from saveDB.func import getStudentCourse, addStudentCourse
from drf_spectacular.utils import extend_schema


class GetStudentCourseView(APIView):
    @extend_schema(request=StudentCourseSerializer, responses=StudentCourseSerializer)
    def get(self, request, num, full_name, topic_selection, selecting_sources,
                  carrying_reserch, shaping_work, making, defending):
        a = getStudentCourse(num, full_name, topic_selection, selecting_sources,
                  carrying_reserch, shaping_work, making, defending)
        print(num, full_name, topic_selection, selecting_sources,
                  carrying_reserch, shaping_work, making, defending)
        print(a)
        a = (StudentCourseSerializer(instance=st).data for st in a) if a is not None else []
        print(a)
        return Response(a)

class AddStudentCourseView(APIView):
    @extend_schema(request=StudentCourseSerializer, responses=StudentCourseSerializer)
    def post(self, request, num, full_name, topic_selection, selecting_sources,
                  carrying_reserch, shaping_work, making, defending):
        a = addStudentCourse(num, full_name, topic_selection, selecting_sources,
                  carrying_reserch, shaping_work, making, defending)

        return Response(a)
