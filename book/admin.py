from django.contrib import admin
from .models import Book,Cart,Customer,department

# Register your models here.
admin.site.register(Book)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(department)