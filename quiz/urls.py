from django.urls import path
from .views import (
    quiz_view,
    render_pdf_view,
    result_view,
    delete_eval,
    thank,
)

app_name = 'quiz'

urlpatterns = [
    path('', quiz_view, name='quiz-view'),
    path('results/', result_view, name='result-view'),
    path('delete/<str:pk>/', delete_eval, name='delete-eval'),
    path("eval/<str:pk>/", render_pdf_view, name='eval-view'),
    path("thank/", thank, name='thank-view'),
]
