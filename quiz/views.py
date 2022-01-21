from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Quiz
from .forms import QuizForm
from quiz.utils import generate_pdf
# decorators
from django.contrib.auth.decorators import login_required
from authentication.decorators import allowed_users, admin_only


# Create your views here.


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
    query = request.GET.get('qs', '')
    if query:
        queryset = (Q(stage__icontains=query)) | (Q(name__icontains=query)) | (Q(stage_name__icontains=query)) | (
            Q(start_date__icontains=query)) | (Q(teacher__icontains=query))
        results = Quiz.objects.filter(queryset).distinct()
    paginator = Paginator(results, 20)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'page_obj': page_obj,
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

    context = {
        # 'other_formations': other_formations,
        'eval': eval,
    }
    template_path = 'quiz/render_pdf.html'
    pdf_name = 'Evaluation'
    # return render(request, template_path, context)
    return generate_pdf(request, template_path, pdf_name, context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['team'])
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
