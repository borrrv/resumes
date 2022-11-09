from django.db import models
from core.models import CreatedModel
from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(CreatedModel):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    name = models.TextField('ФИО')
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts'
    )
    image = models.ImageField(
        'Загрузите ваше фото',
        upload_to='posts/',
        blank=True
    )  
    city = models.TextField('Город проживания')
    birth_day = models.TextField('Дата рождения')
    sex = models.TextField('Пол')
    nationality = models.TextField('Гражданство')
    experience = models.TextField('Опыт работы')
    carrer_objective = models.TextField('Желаемая должность')
    education = models.TextField('Образование')
    language = models.TextField('Языки')
    employment = models.TextField('Тип занятости')
    about_me = models.TextField('О себе')
    phone_number = models.TextField('Номер телефона')
    email = models.TextField('email')

    class Meta:
        ordering = ('-pub_date', )

