from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts__1, create_random_user_accounts_2__1, add

class UsersListView(ListView):
    template_name = 'core/users_list.html'
    model = User


class GenerateRandomUserView(FormView):
    template_name = 'core/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        from .example import ada
        total = form.cleaned_data.get('total')
        create_random_user_accounts__1.apply_async(args=[total], queue='queue1', routing_key='queue1')
        create_random_user_accounts_2__1.apply_async(args=[total], queue='queue2', routing_key='queue2')
        number = add.delay(2, 2)
        ada.delay()

        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')
