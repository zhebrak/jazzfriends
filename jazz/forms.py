# coding: utf-8

from django import forms

from jazz.models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['name', 'contact', 'message']
