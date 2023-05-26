from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from account.email import send_contact_email_message
from account.forms import CustomUserCreationForm, LoginUserForm, UpdateUserForm, UpdateProfileForm, AppealCreateForm
from account.models import CustomUser, Appeal
from account.utils import get_client_ip


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('entrance')
    template_name = 'account/registration.html'

    def registration(request):
        form = None
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            email = request.POST.get('email')
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Данная почта уже используется!')
            else:
                if form.is_valid():
                    ins = form.save()
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password1']

                    user = authenticate(username=username, password=password, email=email)
                    ins.email = email
                    ins.save()
                    form.save_m2m()
                    messages.success(request, 'Регистрация прошла успешно')
                    return redirect('entrance')

        else:
            form = CustomUserCreationForm()

        context = {'form': form}
        return render(request, 'account/registration.html', context)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'account/entrance.html'

def LogoutUser(request):
    logout(request)
    return redirect('/')


def Profile(request):
    return render(request, 'account/profile.html')


class AppealHistory(ListView):
    model = Appeal
    template_name = 'account/appeal_history.html'
    context_object_name = 'appeal'

    def get_queryset(self):
        return Appeal.objects.all().filter(user=self.request.user)

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Изменения в профиле были сохранены.')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'account/profile-changed.html', {'user_form': user_form, 'profile_form': profile_form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'account/change_password.html'
    success_message = "Ваш пароль успешно изменен."
    success_url = reverse_lazy('profile')


class AppealCreateView(SuccessMessageMixin, CreateView):
    model = Appeal
    form_class = AppealCreateForm
    success_message = 'Ваше заявка успешно отправлена '
    template_name = 'account/appeal.html'
    extra_context = {'title': 'Контактная форма'}
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        if form.is_valid():
            requests = form.save(commit=False)
            requests.ip_address = get_client_ip(self.request)
            if self.request.user.is_authenticated:
                requests.user = self.request.user
            send_contact_email_message(requests.subject, requests.email, requests.content, requests.ip_address, requests.user_id)
        return super().form_valid(form)


