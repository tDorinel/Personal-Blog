from django.contrib import admin
from .models import Post

admin.site.register(Post)
admin.site.site_header = "Dori's Blog Control Panel"