from django.shortcuts import render, get_object_or_404

# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group
'''
В этом фаиле обрабатываются запросы к страницам
'''

def index(request):
    title = 'Последние обновления на сайте'
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        # В словарь можно передать переменную
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    title = 'Записи сообщества Лев Толстой – зеркало русской революции'
    # Функция ищет в базе объект модели, а если не находит,
    # прерывает работу view-функции и возвращает страницу с ошибкой 404.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    # Метод .filter позволяет ограничить поиск по критериям.
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
