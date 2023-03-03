//All the models used in the project are exported from here
export interface SideNavItem {
  title: string;
  link: string;
}

export enum UserType {
  ADMIN,
  STUDENT,
}

export interface User {
  id: number;
  name: string;
  email: string;
  password: string;
  user_type: UserType;
}

export interface Book {
  id: number;
  title: string;
  genre: string;
  available: boolean;
  count?: number;
  author: string;
}

export interface GenreBooks {
  genre: string;
  books: Book[];
}

export interface Order {
  id: number;
  userid: number;
  name: string;
  bookid: number;
  booktitle: string;
  orderedon: string;
  status: string;
}

export interface Genre {
  name: string;
  id: number;
  desc: string;
  children?: Genre[];
}
