from django.contrib import admin
from .models import Book, Genre, Author, Order

# Register your models here.

class AdminBook(admin.ModelAdmin):
    exclude=()
    list_display = ('title', 'author', 'genre', 'availability')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'Student', 'book', 'status', 'order_date', 'return_date')

    def order_date(self, obj):
        return obj.order_date
    def Student(self, obj):
        return obj.student.name
    def return_date(self, obj):
        return obj.return_date
    

admin.site.register(Book, AdminBook)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Order, OrderAdmin)
