from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Quiz
from .forms import QuizForm
from quiz.utils import generate_pdf
# decorators
from django.contrib.auth.decorators import login_required
from authentication.decorators import allowed_users
from django.views.decorators.csrf import csrf_protect


# Create your views here.

@csrf_protect
def quiz_view(request):
    form = QuizForm()
    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('quiz:thank-view')
    context = {
        'form': form,
    }
    return render(request, 'quiz/quiz.html', context)


@login_required(login_url='login')
def result_view(request):
    results = Quiz.objects.all()
    context = {
        'results': results,
    }
    return render(request, 'quiz/result.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['team'])
def render_pdf_view(request, pk):
    """
    student eval pdf views
     """
    eval = get_object_or_404(Quiz, id=pk)
    # other_formations = list(eval.other_formation2)
    author = eval.name if eval.name else 'NR'
    context = {
        # 'other_formations': other_formations,
        'eval': eval,
    }
    template_path = 'quiz/render_pdf.html'
    pdf_name = f'Fiche-eval-de-{author}-du-{eval.created.day}-{eval.created.month}-{eval.created.year}'
    # return render(request, template_path, context)
    return generate_pdf(request, template_path, pdf_name, context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['team'])
@csrf_protect
def delete_eval(request, pk):
    result = Quiz.objects.get(id=pk)
    if request.method == "POST":
        result.delete()
        return redirect('quiz:result-view')
    context = {
        'result': result,
    }
    return render(request, 'quiz/delete.html', context)


def thank(request):
    context = {
        'sms': "Merci d'avoir participer à l'évaluation de notre formation."
    }
    return render(request, 'quiz/thank.html', context)
