import { Component } from '@angular/core';
import {
  FormGroup,
  FormControl,
  FormBuilder,
  Validators,
} from '@angular/forms';
import { ApiService } from '../services/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'manage-books',
  templateUrl: './manage-books.component.html',
  styleUrls: ['./manage-books.component.scss'],
})
export class ManageBooksComponent {
  addBookForm: FormGroup;
  deleteBookForm: FormControl;
  query = '';
  result: string[] = [];
  addMsg: string = '';
  delMsg: string = '';

  constructor(private fb: FormBuilder, private api: ApiService, private router:Router) {
    this.addBookForm = fb.group({
      title: fb.control(''),
      author: fb.control(''),
      genre: fb.control(''),
      desc: fb.control(''),
      // title: fb.control('', [Validators.required]),
      // author: fb.control('', [Validators.required]),
      // genre: fb.control('', [Validators.required]),
    });
    this.deleteBookForm = fb.control('');
    //this.deleteBookForm = fb.control('', [Validators.required]);
  }
//Funtion to insert a book using three details, title, author and genre.
  insertBook() {
    var book = {
      id: 0,
      title: this.Title.value,
      genre: this.Genre.value,
      available: true,
      author: this.Author.value,
      desc: this.Desc.value,
    };
    this.api.checkIfGenreExists(this.Genre.value).subscribe(
      (genreExists: boolean) =>{
        if (genreExists){
    this.api.insertBook(book).subscribe({
      next: (res: any) => {
        this.addMsg = 'Book Inserted';
        setInterval(() => (this.addMsg = ''), 5000);
        this.Title.setValue('');
        this.Author.setValue('');
        this.Genre.setValue('');
        this.Desc.setValue('');
      },
      error: (err: any) => console.log(err),
    });
  }
  else {
    console.error("Genre doesn't exist");
    this.router.navigateByUrl('/manage-genre');
  }
  }
    );
}
  // search(){
  //   this.api.search(this.api.insertBook(book)?.genre).subscribe(
  //     (data:any) => {
  //       this.result = data.result;
  //     },
  //   (error) => {console.error(error);}
  //   )
  // }
//Function to delete a book using BookID
  deleteBook() {
    let slug : string = (this.deleteBookForm.value);

    this.api.deleteBook(slug).subscribe({
      next: (res: any) => {
        if (res === 'success') {
          this.delMsg = 'Book Deleted';
        } else {
          this.delMsg = 'Book Deleted';
        }
        setInterval(() => (this.delMsg = ''), 5000);
      },
      error: (err: any) => console.log(err),
    });
  }

  get Title(): FormControl {
    return this.addBookForm.get('title') as FormControl;
  }
  get Author(): FormControl {
    return this.addBookForm.get('author') as FormControl;
  }
  get Genre(): FormControl {
    return this.addBookForm.get('genre') as FormControl;
  }
  get Desc(): FormControl{
    return this.addBookForm.get('desc') as FormControl;
  }
}

