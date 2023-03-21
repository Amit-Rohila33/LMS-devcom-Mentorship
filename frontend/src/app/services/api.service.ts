//All the APIs from the backend are imported here and the URLs for all the components is defined here
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Params } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';
import { map } from 'rxjs/operators';
import { Book, Genre, Order, User, UserType } from '../models/models';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  
  baseUrl = 'http://127.0.0.1:8000/auth/';
  baseURL2 = "http://127.0.0.1:8000/api/"
  constructor(private http: HttpClient, private jwt: JwtHelperService) {}

  //API to register
  createAccount(user: User) {
    return this.http.post(this.baseUrl + 'signup/', user, {
      responseType: 'text',
    });
  }
//API to login
  login(login: any) {
    let params = {
      email:login.email,
      password:login.password
    };
    console.log(params);
    let headers = new HttpHeaders();
headers= headers.append('content-type', 'application/json');
//console.log(this.http.get(this.baseUrl + 'login/', {params: params}));
return this.http.get(this.baseUrl + 'login/', {params: params}
      )
 }
//The functions that are used in many components and also in this file are defined here
  saveToken(token: string) {
    localStorage.setItem('access_token', token);
  }

  isLoggedIn(): boolean {
    return !!localStorage.getItem('access_token');
  }
  getToken() {
    let token = localStorage.getItem('access_token');
   //console.log('token>>>>>>>'+token);
    return token;
  }
  deleteToken() {
    localStorage.removeItem('access_token');
    location.reload();
  }
  getTokenUserInfo(): User | null {
    if (!this.isLoggedIn()) return null;
    let token = this.getToken();
    //console.log(JSON.stringify(token));
    //token = json.decodeToken(token);
    
    if (token == null) return null;
    let token1 = JSON.parse(token);
    
  
    //console.log(token1.name);
    
    //let token = this.jwt.decodeToken();
     let user: User = {
      id: token1.id,
      name: token1.name,
      email: token1.email,
      password: '',
      password2:'',
      user_type: token1.user_type === 'USER' ? 'STUDENT' : 'ADMIN',
      image: null,
   };
    return user;
  }

  getAllBooks() {
    return this.http.get<Book[]>(this.baseURL2 + 'books/');
  }

  orderBook(userId: number, bookId: number) {
    return this.http.get(this.baseURL2 + 'order_book/' + bookId + '/' + userId + '/', {
      responseType: 'text',
    });
  }

  getOrdersOfUser(userid: number) {
    return this.http.get<Order[]>(this.baseURL2 + 'orders/' + userid);
  }

  getAllOrders() {
    return this.http.get<Order[]>(this.baseURL2 + 'orders/');
  }

  returnBook(bookId: string, userId: string) {
    return this.http.get(this.baseURL2 + 'ReturnBook/' + bookId + '/' + userId + '/', {
      responseType: 'text',
    });
  }

  getAllUsers() {
    return this.http.get<User[]>(this.baseURL2 + 'student/').pipe(
      map((users) =>
        users.map((user) => {
          let temp: User = user;
          temp.user_type = user.user_type == '' ? 'STUDENT' : 'ADMIN';
          return temp;
        })
      )
    );
  }

  // blockUser(id: number) {
  //   return this.http.get(this.baseUrl + 'ChangeBlockStatus/1/' + id, {
  //     responseType: 'text',
  //   });
  // }

  // unblockUser(id: number) {
  //   return this.http.get(this.baseUrl + 'ChangeBlockStatus/0/' + id, {
  //     responseType: 'text',
  //   });
  // }

  // enableUser(id: number) {
  //   return this.http.get(this.baseUrl + 'ChangeEnableStatus/1/' + id, {
  //     responseType: 'text',
  //   });
  // }

  // disableUser(id: number) {
  //   return this.http.get(this.baseUrl + 'ChangeEnableStatus/0/' + id, {
  //     responseType: 'text',
  //   });
  // }

  getGenre() {
    return this.http.get<Genre[]>(this.baseURL2 + 'genres/');
  }

  insertBook(book: any) {
    var headers = {
      headers: new HttpHeaders()
      .set('Authorization', 'Token 42bb71c851dda63976b993ffb2bd237135cfba56')
    }
    //  let headers = {
    //    Authorization: 'Token 42bb71c851dda63976b993ffb2bd237135cfba56'
    //  }
    return this.http.post(this.baseURL2 + 'books/', book, headers
    //{headers : headers} 
     
    );
  }

  deleteBook(slug : string) {
    return this.http.delete(this.baseURL2 + 'DeleteBook/' + slug, {
      responseType: 'text',
    });
  }

  insertGenre(name: string, desc: string) {
    return this.http.post(
      this.baseURL2 + 'genres/',
      { name : name, desc: desc},
      // {desc: desc},
      { responseType: 'text' }
    );
  }
  insertAuthor(name:string, desc: string) {
    return this.http.post(
      this.baseURL2 + 'authors/',
      { name : name, desc: desc},
      {responseType : 'text'}
    )
  }
  insertCategory(category: string,) {
    return this.http.post(
      this.baseURL2 + 'InsertCategory',
      { category : category},
      { responseType: 'text' }
    );
  }
  checkIfGenreExists(genre:string){
    return this.http.get<boolean>(this.baseURL2 + 'genres/?q='+genre);
  }
  checkIfAuthorExists(name: string){
    return this.http.get<boolean>(this.baseURL2 + 'authors/?q=' + name);
  }
}
