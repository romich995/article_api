

# Create your models here.
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    html_text = models.TextField()
    author = models.CharField(max_length=20)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='comment')
    html_text = models.TextField()
    inclusion_level = models.PositiveIntegerField(null=False, default=0, blank=False)
    third_level_comment = models.ForeignKey('self',
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='third_comment')
        