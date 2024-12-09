from django.shortcuts import render, redirect
from .models import Quiz, Question, Answer
from .forms import QuizForm

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)

    if request.method == 'POST':
        score = 0
        total_questions = questions.count()
        for question in questions:
            user_answer = request.POST.get(str(question.id))
            if user_answer == question.correct_answer:
                score += 1
        return render(request, 'quiz/result.html', {'score': score, 'total': total_questions})

    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz, 'questions': questions})