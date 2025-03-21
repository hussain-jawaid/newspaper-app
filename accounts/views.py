from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.contrib.auth import login
from django.shortcuts import redirect

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        respone = super().form_valid(form)
        user = form.instance
        login(self.request, user)
        return redirect(self.get_success_url())