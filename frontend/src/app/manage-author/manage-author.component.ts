import { Component } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { ApiService } from '../services/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'manage-author',
  templateUrl: './manage-author.component.html',
  styleUrls: ['./manage-author.component.scss']
})
export class ManageAuthorComponent {
  authorForm: FormGroup;
  msg: string = '';

  constructor(private fb: FormBuilder, private api: ApiService, private router:Router) {
    this.authorForm = this.fb.group({
      name: this.fb.control(''),
      desc: this.fb.control(''),
    });
  }
//Function to add Genre using GenreName and Description of Genre
  addNewAuthor() {
    let a = this.Author.value;
    let d = this.Desc.value;

    this.api.insertAuthor(a, d).subscribe({
      next: (res: any) => {
        this.msg = res.toString();
        setInterval(() => (this.msg = ''), 5000);
        this.router.navigateByUrl('/books/library');
      },
      error: (err: any) => {
        console.log(err);
      },
    });
  }

  get Author(): FormControl {
    return this.authorForm.get('name') as FormControl;
  }
  get Desc(): FormControl{
    return this.authorForm.get('desc') as FormControl;
  }
  
}
