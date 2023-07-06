from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='posts',
                                 related_query_name='posts')
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.category:
            return f'{self.category.title} > {self.title}'
        else:
            return self.title

