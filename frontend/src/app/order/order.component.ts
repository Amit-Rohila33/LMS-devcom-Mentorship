import { Component, OnInit } from '@angular/core';
import { Order } from '../models/models';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.scss'],
})
export class OrderComponent implements OnInit {
  listOfOrders: Order[] = [];
  columns: string[] = ['id', 'name', 'bookid', 'book', 'date', 'status'];

  constructor(private api: ApiService) {}
//The data of orders of a user is pulled here using a Get command
  ngOnInit(): void {
    let userid = this.api.getTokenUserInfo()?.id ?? 0;
    this.api.getOrdersOfUser(userid).subscribe({
      next: (res: Order[]) => {
        console.log(res);
        this.listOfOrders = res;
      },
      error: (err: any) => console.log(err),
    });
  }
}
