import { Component } from '@angular/core';
import { SideNavItem } from '../models/models';

@Component({
  selector: 'side-nav',
  templateUrl: './side-nav.component.html',
  styleUrls: ['./side-nav.component.scss'],
})
export class SideNavComponent {
  sideNavContent: SideNavItem[] = [
    {//Home Page
      title: 'home',
      link: 'home',
    },
    {//View Books Page
      title: 'view books',
      link: 'books/library',
    },
    {//Manage Books Page
      title: 'manage books',
      link: 'books/maintenance',
    },
    {//Manage Genre Page
      title: 'manage genre',
      link: 'manage-genre',
    },
    {//Return Book Page
      title: 'return book',
      link: 'books/return',
    },
    {//View Users Page
      title: 'view users',
      link: 'users/list',
    },
    {//All Orders Page
      title: 'all orders',
      link: 'users/all-orders',
    },
    {//My Orders Page
      title: 'my orders',
      link: 'users/order',
    },
  ];
}
