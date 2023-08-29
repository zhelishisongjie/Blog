from django.urls import path
from article import views

app_name = "article"

urlpatterns = [
     path("",                  views.article_list ,     name = "article_list"),
     path("<int:id>/",         views.article_details ,  name = "article_detail"),
     path("<int:id>/delete/",  views.article_delete,    name = "article_delete"),
     path("create/",           views.article_create,    name = "article_create"),
     path("<int:id>/update/",          views.article_update,    name = "article_update"),

]