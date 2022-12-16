from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('GetStudentCourseView/<str:num>/<str:full_name>/<str:topic_selection>/<str:selecting_sources>/'
         '<str:carrying_reserch>/<str:shaping_work>/<str:making>/<str:defending>',
         views.GetStudentCourseView.as_view(), name="Getter"),
    path('AddStudentCourseView/<str:num>/<str:full_name>/<str:topic_selection>/<str:selecting_sources>/'
         '<str:carrying_reserch>/<str:shaping_work>/<str:making>/<str:defending>',
         views.AddStudentCourseView.as_view(), name="Setter"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui")]