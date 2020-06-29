from django.urls import path

from hello_django.calc import views

urlpatterns = [
    path('', views.IndexView.as_view()),

    path('<int:a>/<int:b>', views.IndexView.as_view(), name='calc'),
    path('history', views.HistoryView.as_view(), name='calchistory'),

]
