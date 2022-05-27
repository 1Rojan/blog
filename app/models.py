from django.db import models
from django.contrib.auth.models import User

STATUS = ((0,'Draft'), (1, 'Published'))
class Post(models.Model):
  title = models.CharField(max_length=63, unique=True)
  slug = models.SlugField(max_length=255, unique=True)
  content = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
  status = models.IntegerField(choices=STATUS, default=0)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)


  class Meta:
    ordering = ['-created_on']
    # db_table = 'posts'

  def __str__(self):
    return self.title