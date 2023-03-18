from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from LMS.models import Book, Genre, Author, Order
from LMS.serializers import BookSerializer, GenreSerializer, AuthorSerializer, AdminBookSerializer, OrderSerializer
from django.db.models import Q
import datetime
import json


    
# Create your views here.
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK, 
    HTTP_201_CREATED,
    HTTP_403_FORBIDDEN,
    HTTP_204_NO_CONTENT
)

from rest_framework.response import Response

'''
The Following three functions contain views for getting Models. 
If the logged in user is a superuser then it also gives options to POST (create) a model object.
'''
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def book_list_display(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            books = Book.objects.filter(Q(title__icontains = query) | Q(desc__icontains = query))
        else:                                  
            books = Book.objects.all()
        if  request.user.is_superuser:
            serializer = AdminBookSerializer(books, many=True)
            return Response(serializer.data)
        else:
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
    elif request.method == 'POST': 
        author = request.data['author']
        genre = request.data['genre']
        # #request.data['desc'] = "Hello "
        try:
            author_id = Author.objects.get(name=author).id
            genre_id = Genre.objects.get(name=genre).id
            request.data['author'] =author_id
            request.data['genre'] = genre_id
            if request.data['available']:
                request.data.pop('available')
            # if not request.user.is_superuser :
            serializer = BookSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
            if not serializer.is_valid:
                data = {"detal":"Somethings is messed up here."}
                return Response(data=data)    
        except Author.DoesNotExist or Genre.DoesNotExist:
            return Response(data = {},status=HTTP_400_BAD_REQUEST)
        # return Response(status=HTTP_400_BAD_REQUEST)
           
    # elif request.method =='POST' and not request.user.is_superuser:
    #     return Response(status = HTTP_403_FORBIDDEN, data={"detail": "Access Forbidden."})
            
    return Response(status = HTTP_400_BAD_REQUEST, data={"detail": "Authentication credentials were not provided."})


@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def author_list_display(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            authors = Author.objects.filter(Q(name__icontains = query) | Q(desc__icontains = query))
        else:
            authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    elif request.method =='POST': #and request.user.is_superuser:
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)   
    # elif request.method =='POST' and not request.user.is_superuser:
    #     return Response(status = HTTP_403_FORBIDDEN, data={"detail": "Acess Forbidden."})
            
    return Response(status = HTTP_400_BAD_REQUEST, data={"detail": "Authentication credentials were not provided."})


@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def genre_list_display(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            genre = Genre.objects.filter(Q(name__icontains = query) | Q(desc__icontains = query))
        else:
            genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)
    elif request.method =='POST' and request.user.is_superuser:
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)   
    elif request.method =='POST' and not request.user.is_superuser:
        return Response(status = HTTP_403_FORBIDDEN, data={"detail": "Acess Forbidden."})
            
    return Response(status = HTTP_400_BAD_REQUEST, data={"detail": "Authentication credentials were not provided."})



'''
The following three functions return views/api endpoints for retrieving a particular 
Object of Genre, Author, Book using using slug.
It gives  PUT, DELETE option if the logged in user is superuser.
'''


@api_view(['GET', 'PUT'])
@permission_classes((AllowAny,))
def book_details(request, slug):
    try:
        book = Book.objects.get(slug=slug)
            
    except Book.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND, data = {'detail':'Book Does Not Exist'})

    if request.method =='GET':
        if request.user.is_superuser:
            serializer = AdminBookSerializer(book)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            serializer = BookSerializer(book)
            return Response(serializer.data, status=HTTP_200_OK)
    
    elif request.method =='PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    # elif request.method =='DELETE': #and request.user.is_superuser:
    #     book.delete()
    #     return Response(status=HTTP_204_NO_CONTENT)
    

    # elif (request.method =='PUT' or request.method =='DELETE') and not request.user.is_superuser:
    return Response(data={"data":"Access Forbidden"}, status=HTTP_403_FORBIDDEN)
    

@api_view(['DELETE'])
@permission_classes((AllowAny,))
def deletebook(request, slug):
    try:
        book = Book.objects.get(slug=slug)
        book.delete()
        return Response(status= HTTP_204_NO_CONTENT)
    except Book.DoesNotExist:
        return Response(status= HTTP_404_NOT_FOUND)
    

#getting Genre by Slug
@api_view(['GET', 'PUT','DELETE'])
@permission_classes((AllowAny,))
def genre_details(request, slug):
    try:
        genre = Genre.objects.get(slug=slug)
            
    except Genre.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND, data = {'detail':'Book Does Not Exist'})

    if request.method =='GET':
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=HTTP_200_OK)
    
    elif request.method =='PUT' and request.user.is_superuser:
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE' and request.user.is_superuser:
        genre.DELETE()
        return Response(status=HTTP_204_NO_CONTENT)
    

    elif (request.method =='PUT' or request.method =='DELETE') and not request.user.is_superuser:
        return Response(data={"data":"Access Forbidden"}, status=HTTP_403_FORBIDDEN)
    


#Getting Author by slug
@api_view(['GET', 'PUT','DELETE'])
@permission_classes((AllowAny,))
def author_details(request, slug):
    try:
        author = Author.objects.get(slug=slug)
            
    except Author.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND, data = {'detail':'Book Does Not Exist'})

    if request.method =='GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=HTTP_200_OK)
    
    elif request.method =='PUT': #and request.user.is_superuser:
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':# and request.user.is_superuser:
        author.DELETE()
        return Response(status=HTTP_204_NO_CONTENT)
    

    # elif (request.method =='PUT' or request.method =='DELETE') and not request.user.is_superuser:
    #     return Response(data={"data":"Access Forbidden"}, status=HTTP_403_FORBIDDEN)


@api_view(['GET'])
def issued_book_list_display(request):
    if request.method == 'GET' and request.user.is_superuser:
        books = Book.objects.filter(availability=False)
        serializer = AdminBookSerializer(books, many=True)
        return Response(serializer.data)
    return Response(data={"data":"Access Forbidden"}, status=HTTP_403_FORBIDDEN)


@api_view(['GET'])
@permission_classes((AllowAny,))
def orders_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders,many =True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((AllowAny,))
def trending_books(request):
    ordered_books = Order.objects.all()
    
    orderss = [
        {'book_id': 123, 'order_date': datetime.datetime(2022, 1, 1), 'title':'Life of Pi'}
    ]
    for orders in ordered_books:
        book_id = orders.book.id
        title = str(orders.book)
        order_date = orders.order_date
        orderss.append({'book_id': book_id,'title':title, 'order_date':order_date})
    return Response(data=orderss)
    


@api_view(['PUT'])
@permission_classes((AllowAny,))
def orderbook(request, bookid, studid):
    try:
        book = Book.objects.get(id=bookid)
    
        # student = 
        request.data['title'] = book.title
        request.data['issued_to'] = studid
        if book.genre == "None":
            request.data['genre'] = 11
        request.data['genre'] = book.genre.name
        request.data['desc'] = book.desc
        request.data['author']=book.author.name
        serializer = AdminBookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # if book.availability:
        #     book.issued_to = student
        #     book.save()
        #     serializer = AdminBookSerializer(book)
        #     return Response(serializer.data)
    
    
    except Book.DoesNotExist: 
        data = {"detail": "This book is not available."}  
        return Response(data=data, status=HTTP_404_NOT_FOUND)
    return Response(data = request.data, status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes((AllowAny,))
def returnbook(request, bookid, studid):
    try:
        book = Book.objects.get(id=bookid)
    except Book.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    if book.issued_to.id == int(studid):
        # student = 
        request.data['title'] = book.title
        request.data['issued_to'] = None
        if book.genre == "None":
            request.data['genre'] = 11
        request.data['genre'] = book.genre.id
        request.data['desc'] = book.desc
        request.data['author']=book.author.id

        #request.data = json.dumps(request.data)
        serializer = AdminBookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)

        
        # request.data['status'] = "Returned"
        # request.data['return_date'] = datetime.datetime.now()
        # request.data['order_date']
        # order = Order.objects.get(book = bookid, status="Ordered")
        # order.status = status
        # order.return_date = return_date
        # order.save()
        return Response(data=request.data,status=HTTP_400_BAD_REQUEST)
    
    else:
        # data = {'detail':book}
        return Response(data ={'data':AdminBookSerializer(book).data, 'datas':int(studid)}, status=HTTP_400_BAD_REQUEST)



    
    
    
  
    
    

