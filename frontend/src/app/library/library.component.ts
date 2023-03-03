import { Component, OnInit } from '@angular/core';
import { Book, GenreBooks, Genre } from '../models/models';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'library',
  templateUrl: './library.component.html',
  styleUrls: ['./library.component.scss'],
})
export class LibraryComponent implements OnInit {
  availableBooks: Book[] = [];
  booksToDisplay: GenreBooks[] = [];
  displayedColumns: string[] = [
    'id',
    'title',
    'author',
    'available',
    'order',
  ];

  constructor(private api: ApiService) {}

  ngOnInit(): void {
//This is used to get the data of books from backend. Initially array of Book is defined as empty and then using a for loop, the array is filled.
    this.api.getAllBooks().subscribe({
      next: (res: Book[]) => {
        this.availableBooks = [];
        console.log(res);
        for (var book of res) this.availableBooks.push(book);
        this.updateList();
      },
      error: (err: any) => console.log(err),
    });
  }
//This function uses the data from backend and displays it on the frontend
  updateList() {
    this.booksToDisplay = [];
    for (let book of this.availableBooks) {
      let exist = false;
      for (let genreBooks of this.booksToDisplay) {
        if (
          book.genre === genreBooks.genre 
        )
          exist = true;
      }

      if (exist) {
        for (let genreBooks of this.booksToDisplay) {
          if (
            book.genre === genreBooks.genre 
          )
            genreBooks.books.push(book);
        }
      } else {
        this.booksToDisplay.push({
          genre: book.genre,
          books: [book],
        });
      }
    }
  }
//This function is used to count the number of books.
  getBookCount() {
    return this.booksToDisplay.reduce((pv, cv) => cv.books.length + pv, 0);
  }
//This function is used to search a book using it's title or author name.
  search(value: string) {
    value = value.toLowerCase();
    this.updateList();
    if (value.length > 0) {
      this.booksToDisplay = this.booksToDisplay.filter((genreBooks) => {
        genreBooks.books = genreBooks.books.filter(
          (book) =>
            book.title.toLowerCase().includes(value) ||
            book.author.toLowerCase().includes(value)
        );
        return genreBooks.books.length > 0;
      });
    }
  }
//This function enables a user to order a book.
  orderBook(book: Book) {
    let userid = this.api.getTokenUserInfo()?.id ?? 0;
    this.api.orderBook(userid, book.id).subscribe({
      next: (res: any) => {
        if (res === 'success') {
          book.available = false;
        }
      },
      error: (err: any) => console.log(err),
    });
  }
}
