from django.db import models
from authentication.models import Student

# Create your models here.


class Genre(models.Model):
    
    name = models.CharField(max_length=200, name="name")
    thumb_img = models.ImageField(blank=True, upload_to='genre-img/')
    desc = models.TextField(max_length=400)
    slug = models.SlugField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255, name='name')
    desc = models.TextField(name = 'desc')
    image = models.ImageField(upload_to='author-images/', blank=True, name='image')
    slug = models.SlugField(default='',blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    thumb_img = models.ImageField(blank=True, upload_to='book-img/')
    desc = models.TextField()
    genre = models.ForeignKey(Genre, blank=True, on_delete=models.SET_NULL, null=True, name="genre")
    issued_to = models.ForeignKey(Student,null=True, default=None, on_delete=models.SET_NULL,blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    availability = models.BooleanField(default=False)
    author = models.ForeignKey(Author, default=None, null = True, blank=True, on_delete=models.SET_NULL, name="author")


    def __str__(self):
        return self.title
    

class Order(models.Model):
    status = models.CharField(name="status", max_length=255)
    book = models.ForeignKey(Book, name="book", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, name="student", on_delete=models.CASCADE)
    order_date = models.DateTimeField(blank=True, null=True, name="order_date")
    return_date = models.DateTimeField(blank=True, null=True, name="return_date")

    def __str__(self) :
        return self.book.title

    




