import { Component } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'manage-genre',
  templateUrl: './manage-genre.component.html',
  styleUrls: ['./manage-genre.component.scss']
})
export class ManageGenreComponent {
  genreForm: FormGroup;
  msg: string = '';

  constructor(private fb: FormBuilder, private api: ApiService) {
    this.genreForm = this.fb.group({
      genre: this.fb.control(''),
      desc: this.fb.control(''),
    });
  }
//Function to add Genre using GenreName and Description of Genre
  addNewGenre() {
    let g = this.Genre.value;
    let d = this.Description.value

    this.api.insertGenre(g).subscribe({
      next: (res: any) => {
        this.msg = res.toString();
        setInterval(() => (this.msg = ''), 5000);
      },
      error: (err: any) => {
        console.log(err);
      },
    });
  }

  get Genre(): FormControl {
    return this.genreForm.get('genre') as FormControl;
  }
  get Description(): FormControl {
    return this.genreForm.get('desc') as FormControl;
  }
}
