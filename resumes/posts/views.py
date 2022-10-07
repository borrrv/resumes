from django.shortcuts import render

def index(request):
    template = 'posts/index.html'
    info = 'Главный текст'
    title = 'Главная страница'
    context = {
        'info': info,
        'title': title,
    }
    return render(request, template, context)
