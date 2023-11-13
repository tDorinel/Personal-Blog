from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
admin.site.site_header = "Dori's Blog Control Panel"
admin.site.register(Comment)