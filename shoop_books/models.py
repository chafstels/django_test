from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=25, blank=True, null=True)
    amount = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.title

class BuyBooks(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    title = models.ForeignKey(Books, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user and self.title:
            return f'Покупатель {self.user.username} заказал {self.title.title} в количестве {self.amount}'
        else:
            return self.user
