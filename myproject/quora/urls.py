from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('questions/', views.QuestionListView.as_view(), name='question_list'),
    path('questions/ask/', views.AskQuestionView.as_view(), name='ask_question'),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name='question_detail'),
    path('questions/<int:question_id>/answer/', views.AnswerQuestionView.as_view(), name='answer_question'),
    path('answers/<int:answer_id>/like/', views.like_answer, name='like_answer'),
]