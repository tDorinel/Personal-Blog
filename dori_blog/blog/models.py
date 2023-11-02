from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_title = models.CharField(max_length=250)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_headline = models.CharField(max_length=300)
    post_body = models.TextField() 

    def __str__(self):
        return self.post_title + ' - ' + str(self.post_author.get_full_name())