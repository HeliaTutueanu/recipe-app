from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .forms import CustomUserCreationForm

class profile(LoginRequiredMixin, DetailView):
    model: CustomUser
    context_object_name = 'current_user'
    def get_object(self, queryset=None):
        try:
            return CustomUser.objects.get(user=self.request.user)
        except CustomUser.DoesNotExist:
            return redirect('users:signup')

    
def signup_view(request):
    error_message = None
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = None
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1']
                )

                customuser = CustomUser(
                    user=user,
                    name=form.cleaned_data['name']
                )
                customuser.save()

                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
                login(request, user)
                return redirect('recipes:home')
            
            except:
                if user:
                    user.delete()
                error_message = f'Something went wrong. Please try again'
        else:
            error_message = 'Something went wrong.'
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
        'error_message': error_message
    }

    return render(request, 'auth/signup.html', context)