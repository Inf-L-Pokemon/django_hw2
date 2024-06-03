from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserCreateForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('users:login')
