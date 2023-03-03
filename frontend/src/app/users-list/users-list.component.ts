import { Component, OnInit } from '@angular/core';
import { User } from '../models/models';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'users-list',
  templateUrl: './users-list.component.html',
  styleUrls: ['./users-list.component.scss'],
})
export class UsersListComponent implements OnInit {
  users: User[] = [];
  columnsToDisplay: string[] = [
    'id',
    'name',
    'email',
  ];

  constructor(private api: ApiService) {}

  ngOnInit(): void {
    //API used to get data regarding all users from backend
    this.api.getAllUsers().subscribe({
      next: (res: User[]) => {
        this.users = [];
        this.users = res;
      },
      error: (err: any) => console.log(err),
    });
  }
}
