from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from account.forms import CustomUserCreationForm, LoginUserForm
from account.models import CustomUser


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

    #def get_context_data(self, *, object_list=None, **kwargs):
        #context = super().get_context_data(**kwargs)
       # c_def = self.get_user_context(title="Авторизация")
        #return dict(list(context.items()) + list(c_def.items()))

def Profile(request):
    return render(request, 'account/profil.html')




    """def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            #return redirect('entrance')

        else:
            return render(request, self.template_name, {'form': form})
"""

