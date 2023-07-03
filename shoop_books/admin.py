from django.contrib import admin

from shoop_books.models import Books, BuyBooks, Users

# Register your models here.

admin.site.register(Books)
admin.site.register(BuyBooks)
admin.site.register(Users)

