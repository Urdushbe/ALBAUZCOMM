from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class RegistrationView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'

class UserProfileView(DetailView):
    model = get_user_model()
    template_name = 'user_profile.html'
    context_object_name = 'user_profile'

class UserProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'user_profile_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.pk == self.request.user.pk or self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy('user_profile', args=[self.request.user.id])

