
from django.shortcuts import get_object_or_404, redirect,render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, Like
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})

class QuestionListView(ListView):
    model = Question
    template_name = 'question_list.html'
    context_object_name = 'object_list'
    ordering = ['-created_at']  # Newest questions first

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question_detail.html'

class AskQuestionView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'ask_question.html'
    success_url = '/questions/'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the current user
        return super().form_valid(form)

class AnswerQuestionView(LoginRequiredMixin, CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'answer_question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = get_object_or_404(Question, id=self.kwargs['question_id'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question = get_object_or_404(Question, id=self.kwargs['question_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.question.get_absolute_url()  # Redirect to the question detail page

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    Like.objects.get_or_create(answer=answer, user=request.user)  # Create a like if it doesn't exist
    return redirect(answer.question.get_absolute_url())