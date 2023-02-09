from django.db import models
# Из модуля auth импортируем функцию get_user_model
from django.contrib.auth import get_user_model

'''
В этом фаиле описываются предметы(модели) того, 
что будет размещаться в админке и наделяются свойствами.
'''
User = get_user_model()


class Group(models.Model):
    # при печати объекта модели Group выводилось поле title
    def __str__(self):
        return self.title
    # Название группы
    title = models.CharField(max_length=200)
    # Отображение ссылки по slug
    slug = models.SlugField()
    # Описание сообщества
    description = models.TextField()


# Здесь мы задаем поля и параметры вывода полей для БД
class Post(models.Model):
    # Поле для хранения пользовательских данных
    text = models.TextField()
    # Поле для хранения даты и времени
    pub_date = models.DateTimeField(auto_now_add=True)
    # ссылка на другую таблицу, на её primary key (pk).
    # это свойство обеспечивает связь (relation) между таблицами баз данных.
    author = models.ForeignKey(
        User,
        # обеспечивает связность данных: если из таблицы User
        # будет удалён пользователь и будут удалены все связанные с ним посты.
        on_delete=models.CASCADE,
        related_name='posts'
    )
    # свойство group, чтобы при добавлении новой записи,
    # можно было сослаться на сообщество (на модель Group)
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        # обеспечивает связность данных: если из таблицы Group
        # будет удалён пользователь и будут удалены все связанные с ним посты.
        on_delete=models.SET_NULL,
        related_name='groups'
    )
