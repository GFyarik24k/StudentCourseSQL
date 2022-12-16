from django.shortcuts import render
from django.http import HttpResponse
from saveDB.func import *


def queryGetStudentCourse(request):
    num = request.GET.get("num")
    full_name = request.GET.get("full_name")
    topic_selection = request.GET.get("topic_selection")
    selecting_sources = request.GET.get("selecting_sources")
    carrying_reserch = request.GET.get("carrying_reserch")
    shaping_work = request.GET.get("shaping_work")
    making = request.GET.get("making")
    defending = request.GET.get("defending")

    student = getStudentCourse(num, full_name, topic_selection, selecting_sources,
                  carrying_reserch, shaping_work, making, defending)

    print(student)
    return HttpResponse((f"ID студента: {obj['id']} - №Студ.: {obj['num']}, ФИО: {obj['full_name']}, "
                         f"Тема: {obj['topic_selection']}, Источники: {obj['selecting_sources']}, "
                         f"Исследование: {obj['carrying_reserch']}, Формирование структуры: {obj['shaping_work']}, "
                         f"Оформление: {obj['making']}, Защита: {obj['defending']}<br>" for obj in student)
        if len(student) else f"Студента не существует в базе")
def queryAddStudentCourse(request):
    num = request.GET.get("num")
    full_name = request.GET.get("full_name")
    full_name = request.GET.get("full_name")
    topic_selection = request.GET.get("topic_selection")
    selecting_sources = request.GET.get("selecting_sources")
    carrying_reserch = request.GET.get("carrying_reserch")
    shaping_work = request.GET.get("shaping_work")
    making = request.GET.get("making")
    defending = request.GET.get("defending")

    student = getStudentCourse(num, full_name, topic_selection, selecting_sources,
                  carrying_reserch, shaping_work, making, defending)

    return HttpResponse((f"ID студента: {student['id']} - №Студ.: {student['num']}, ФИО: {student['full_name']}, "
                         f"Тема: {student['topic_selection']}, Источники: {student['selecting_sources']}, "
                         f"Исследование: {student['carrying_reserch']}, Формирование структуры: {student['shaping_work']}, "
                         f"Оформление: {student['making']}, Защита: {student['defending']}<br>"))
