from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_title = models.CharField(max_length=250)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_headline = models.CharField(max_length=300)
    post_body = models.TextField() 

    def __str__(self):
        return self.post_title + ' - ' + str(self.post_author.get_full_name())
    
class Comment(models.Model):
    comment_post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    comment_name = models.CharField(max_length=255)
    comment_body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.comment_post) + ' - ' + str(self.comment_name)
       