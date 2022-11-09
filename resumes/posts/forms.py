from django import forms
from django.forms import SelectDateWidget
from phonenumber_field.formfields import PhoneNumberField

from .models import Post


date_list = [*range(1960, 2022)]


class PostForm(forms.ModelForm):
    name = forms.CharField(label = 'ФИО')
    city = forms.CharField(label='Город проживания',
                           max_length=60,
                           )
    birth_day = forms.DateField(label='Дата рождения:',
                                widget=SelectDateWidget(years=date_list))
    sex = forms.ChoiceField(label='Пол',
                            choices=[
                                     ('', ''),
                                     ('Мужчина', 'Мужчина'),
                                     ('Женщина', 'Женщина'),
                            ])
    nationality = forms.CharField(label='Гражданство', max_length=60)
    experience = forms.CharField(label='Опыт работы (перечислите Ваши места работы)',
                                 widget=forms.Textarea(
                                    attrs={'cols': 1, 'rows': 5}))
    carrer_objective = forms.CharField(label='Желаемая должность',
                                       max_length=60)
    education = forms.CharField(label='Образование (Уровень, учебное заведение, факультет, специализация, год окончания)',
                                widget=forms.Textarea(attrs={'cols': 1, 'rows': 5}))
    language = forms.CharField(label='Владение языками (укажите, какими языками владеете и их уровень)', max_length=60)
    employment = forms.ChoiceField(label='Желаемый тип занятости',
                                   choices=[
                                        ('', ''),
                                        ('Частичная', 'Частичная'),
                                        ('Полная', 'Полная'),
                                        ('Проектная работа', 'Проектная работа'),
                                        ('Стажировка', 'Стажировка'),
                                    ])
    about_me = forms.CharField(label='О себе',
                               widget=forms.Textarea(attrs={'cols': 1, 'rows': 5}))
    phone_number = PhoneNumberField(label='Номер телефона')
    email = forms.EmailField()

    class Meta:
        model = Post
        fields = ('name', 'group', 'image',
                  'city', 'birth_day', 'sex',
                  'nationality', 'experience', 'carrer_objective',
                  'education', 'language', 'employment', 'about_me',
                  'phone_number', 'email')
