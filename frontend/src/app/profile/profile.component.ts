import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

export interface TableElement {
  name: string;
  value: string | undefined;
}

@Component({
  selector: 'profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss'],
})
export class ProfileComponent implements OnInit {
  dataSource: TableElement[] = [];
  columns: string[] = ['name', 'value'];

  constructor(private api: ApiService) {}

  ngOnInit() {
    let user = this.api.getTokenUserInfo();
// Data is being pulled here to display to the user
    this.dataSource = [
      { name: 'Name', value: user?.name},
      { name: 'Email', value: user?.email ?? '' },
    ];
  }
}
