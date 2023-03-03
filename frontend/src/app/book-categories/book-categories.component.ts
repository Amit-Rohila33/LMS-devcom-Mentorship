import { NestedTreeControl } from '@angular/cdk/tree';
import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { MatTreeNestedDataSource } from '@angular/material/tree';
import { Genre } from '../models/models';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'book-categories',
  templateUrl: './book-categories.component.html',
  styleUrls: ['./book-categories.component.scss'],
})
export class BookCategoriesComponent {
  dataSource = new MatTreeNestedDataSource<Genre>();
  treeControl = new NestedTreeControl<Genre>((node) => node.children);

  constructor(private api: ApiService) {
    this.updateCategories();
  }

  hasChild = (_: number, node: Genre) =>
    !!node.children && node.children.length > 0;

  updateCategories() {
    this.api.getGenre().subscribe({
      next: (res: any) => (this.dataSource.data = res),
    });
  }
}
