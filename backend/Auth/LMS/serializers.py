from rest_framework import serializers
from .models import Book, Genre, Author, Order
from authentication.models import Student

'''
two distinct serializers for the Book model that exhibit varying data sets based on the requesting user. Specifically, if the user making the request is a privileged superuser, they are granted access to the additional issued_to field of the Book model.'''
class BookSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset= Genre.objects.all(),required = False, allow_null=True)
    thumb_img = serializers.ImageField(required = False, allow_null = True)
    class Meta:
        model = Book
        fields = ('id', 'genre', 'thumb_img', 'title', 'slug', 'availability', 'author', 'desc')

    def to_representation(self, instance):
        rep = super(BookSerializer, self).to_representation(instance)
        if instance.genre is not None:
            rep['genre'] = instance.genre.name
        else:
            rep['genre']= 'None'
        if instance.author is not None:
            rep['author'] = instance.author.name
        else:
            rep['author']= 'None'
        if instance.availability:
            rep['available'] = 1
        else:
            rep['available'] = None
        return rep
        
        
    
    
class AdminBookSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset= Genre.objects.all(), many=True,required = False)
    issued_to = serializers.PrimaryKeyRelatedField(queryset= Student.objects.all(), required = False, allow_null=True)
    thumb_img = serializers.ImageField(required = False, allow_null = True)
    class Meta:
        model = Book
        fields = '__all__'

        


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset= Book.objects.all(),required = False)
    student = serializers.PrimaryKeyRelatedField(queryset= Student.objects.all(), required = False, allow_null=True)
    
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(OrderSerializer, self).to_representation(instance)
        if instance.book is not None:
            rep['book'] = instance.book.title
            rep['bookId'] = instance.book.id
        else:
            rep['book']= 'None'
        if instance.student is not None:
            rep['student'] = instance.student.name
            rep['UserId'] = instance.student.id
        else:
            rep['student']= None
            rep['UserId'] = None
        return rep