from django.shortcuts import render
from django.urls import reverse_lazy #Reverse lazy we user to say, if someone is logged in or loggin out, where he should actually go
from django.views.generic import CreateView

from accounts import forms

class SingUp(CreateView):

    form_class = forms.UserCreateForm

    success_url = reverse_lazy('login')
    template_name = "accounts/signup.html"
