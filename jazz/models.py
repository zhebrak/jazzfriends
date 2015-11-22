# coding: utf-8

from django.db import models


class Concert(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'название')
    location = models.CharField(max_length=200, verbose_name=u'место')
    show_time = models.DateTimeField(verbose_name=u'время')

    site = models.URLField(blank=True, null=True, verbose_name=u'сайт')
    description = models.TextField(blank=True, null=True, verbose_name=u'описание')

    class Meta:
        verbose_name = u'Концерт'
        verbose_name_plural = u'Концерты'
        ordering = ('-show_time',)


class Attachment(models.Model):
    IMAGE = 0
    type_choices = (
        (IMAGE, u'картинка'),
    )

    file_type = models.SmallIntegerField(choices=type_choices, verbose_name=u'название')
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name=u'название')
    group = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'группа')
    file = models.FileField(verbose_name=u'файл', upload_to='attachments/')

    class Meta:
        verbose_name = u'Документ'
        verbose_name_plural = u'Документы'


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'имя')
    contact = models.CharField(max_length=100, verbose_name=u'контакт')
    message = models.TextField(verbose_name=u'сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'дата создания')

    class Meta:
        verbose_name = u'Обратная связь'
        verbose_name_plural = u'Обратная связь'

