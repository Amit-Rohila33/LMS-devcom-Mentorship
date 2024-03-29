from django.urls import path
from . import views

urlpatterns = [
   
   path('books/', views.book_list_display),
   path('authors/', views.author_list_display),
   path('genres/', views.genre_list_display),
   path('books/<slug:slug>/', views.book_details),
   path('genres/<slug:slug>/', views.genre_details), 
   path('authors/<slug:slug>/', views.author_details),
   path('issued-books/', views.issued_book_list_display),
   path('orders/', views.orders_list),
   path('trending-books/', views.trending_books),
   path('order_book/<int:bookid>/<int:studid>/', views.orderbook),
   path('ReturnBook/<int:bookid>/<int:studid>/', views.returnbook),
   path('DeleteBook/<int:bid>', views.deletebook),
   path('orders/<int:userid>', views.order_by_student)

]