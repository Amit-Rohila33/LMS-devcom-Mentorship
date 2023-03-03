import { Component, OnInit } from '@angular/core';
import { Book, Genre, GenreBooks } from '../models/models';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'genre',
  templateUrl: './genre.component.html',
  styleUrls: ['./genre.component.scss']
})
export class GenreComponent implements OnInit {
  availableBooks: Book[] = [];
  booksToDisplay: GenreBooks[] = [];
  displayedColumns: string[] = [
    'id',
    'name',
    'desc'
  ];
  constructor(private api: ApiService) {}

  ngOnInit(): void {
    this.api.getGenre().subscribe({
      next: (res: Genre[]) => {
        this.availableBooks = [];
        console.log(res);
        // for (var genre of res) this.availableBooks.push(genre);
        // this.updateList();
      },
      error: (err: any) => console.log(err),
    });
  }

  updateList() {
    this.booksToDisplay = [];
    for (let book of this.availableBooks) {
      let exist = false;
      for (let genreBooks of this.booksToDisplay) {
        if (
          book.genre === genreBooks.genre //&&
          // book.subCategory === categoryBooks.subCategory
        )
          exist = true;
      }

      if (exist) {
        for (let genreBooks of this.booksToDisplay) {
          if (
            book.genre === genreBooks.genre //&&
            // book.subCategory === categoryBooks.subCategory
          )
            genreBooks.books.push(book);
        }
      } else {
        this.booksToDisplay.push({
          genre: book.genre,
          // subCategory: book.subCategory,
          books: [book],
          // subCategory: ''
        });
      }
    }
  }
}