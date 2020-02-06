''' Users views. '''

# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy

# Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

#Exceptions
from django.db.utils import IntegrityError

# Forms
from users.forms import ProfileForm, SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):
	"""User detail view."""

	template_name = 'users/detail.html'
	slug_field = 'username'
	slug_url_kwarg = 'username'
	queryset = User.objects.all()
	context_object_name = 'user'


	def get_context_data(self, **kwargs):
		"""Add user's posts to context."""
		context = super().get_context_data(**kwargs)
		user = self.get_object()
		context['posts'] = Post.objects.filter(user=user).order_by('-created')
		return context


"""
La clase UpdateProfileView hace lo mismo que esta función.

@login_required
def update_profile(request):
	'''Update a user's profile view.'''
	profile = request.user.profile

	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.cleaned_data

			profile.website = data['website']
			profile.phone_number = data['phone_number']
			profile.biography = data['biography']
			profile.picture = data['picture']
			profile.save()

			url = reverse('users:detail', kwargs={'username': request.user.username})
			return redirect(url)

	else:
		form = ProfileForm()


	return render(
		request=request,
		template_name='users/update_profile.html',
		context={
			'profile': profile,
			'user': request.user,
			'form': form,
		}
	)
"""
class UpdateProfileView(LoginRequiredMixin, UpdateView):
	"""Update profile view."""

	template_name = 'users/update_profile.html'
	model = Profile
	fields = ['website', 'biography', 'phone_number', 'picture']

	def get_object(self):
		"""Return user's profile."""
		return self.request.user.profile

	def get_success_url(self):
		"""Return to user's profile."""
		username = self.object.user.username
		return reverse('users:detail', kwargs={'username': username})



class LoginView(auth_views.LoginView):
	"""Login view."""
	template_name = 'users/login.html'

"""
La clase LoginView hace lo mismo que esta función.

def login_view(request):
	'''Login view.'''
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)

		if user:
			login(request, user)
			return redirect('posts:feed')
		else:
			return render(request, 'users/login.html', {'error':'ERROR BABY'})
	return render(request, 'users/login.html')
"""

class SignupView(FormView):
	"""Users sign up view."""
	template_name = 'users/signup.html'
	form_class =SignupForm
	success_url = reverse_lazy('users:login')

	def form_valid(self, form):
		"""Save form date."""
		form.save()
		return super().form_valid(form)
"""
La clase SignupView hace lo mismo que esta función.

def signup(request):
	'''Signup view.'''
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('users:login')
	else:
		form = SignupForm()

	return render(
		request=request,
		template_name='users/signup.html',
		context={'form': form}
		)
"""

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
	"""Logout View"""
	# Este template_name realmente no hace nada. podría no existir y la view seguiría funcionando.
	# Ver en settings.LOGOUT_REDIRECT_URL la variable que define la URL de retorno al cerrar sessión.
	template_name = 'users/logged_out.html'

"""
La clase LogoutView hace lo mismo que esta función.

@login_required
def logout_view(request):
	logout(request)
	return redirect('users:login')
"""