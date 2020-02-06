# Django
from django.contrib import admin

# Models
from posts.models import Post

@admin.register(Post)
class ProfileAdmin(admin.ModelAdmin):
	pass