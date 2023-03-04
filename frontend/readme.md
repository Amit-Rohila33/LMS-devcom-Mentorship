# LMS-devcom-Mentorship

This project aims to make a management system for a library, in order to maintain the records of books available/not available in the library and the students who are already registered or want to register in the library. The system offers a variety of features to perform this task efficiently.

## Features of the Management System<br>

#### **1) Home** <br>

- This is the first page that is opened on accessing the website. <br>
- 'URL' http://localhost:port/home <br>

#### **2) View Book** <br>

- This page contains all the books available or not available in the library.<br>
- Genre, ID, Book name, Author and the book's availability are displayed on this page. <br>
- A book can even be ordered from this page.<br>
- 'URL' http://localhost:port/books/library<br>

#### **3) Manage Books** <br>

- This page can only be accessed by an ADMIN.<br>
- If a book needs to be added to the library system, it can be added from this page.<br>
- Any existing book can also be deleted from management system using this page.<br>
- To add a book, there are three fields, Book Title, Book Genre and Book Author. <br>
- 'URL' http://localhost:port/books/maintenance <br>

#### **4) Manage Genre** <br>

- This page also can only be accessed by an ADMIN. <br>
- If a book needs to be added but it's genre is not available in the system, then the genre can be added from this page.<br>
- Only two things are required to add a genre, Genre Name and Description.<br>
- 'URL' http://localhost:port/manage-genre<br>

#### **5) Return Book**<br>

- In order to return a book, this page is used.<br>
- After entering the Book ID and User Id, a student can return the book issued to them.<br>
- 'URL' http://localhost:port/books/return <br>

#### **6) View Users**<br>

- This page can only be accessed by an ADMIN.<br>
- The details of all the students that are registered on the system can be found here.<br>
- ID, Name, Email, and the date student account was created is displayed here.<br>
- 'URL' http://localhost:port/users/list<br>

#### **7) All Orders**<br>

- This page can only be accessed by an ADMIN.<br>
- The orders of books placed by all the students arer displayed here.<br>
- Order ID, User ID, User Name, Book ID, Book Name, Order Date, and the Return Status of an order can be seen here.<br>
- A filter is also present to display orders on the basis of their Return Status.<br>
- 'URL' http://localhost:port/users/all-orders<br>

#### **8) My Orders**<br>

- This page is different for every user depending on their orders.<br>
- All the orders placed by a user are available here.<br>
- A user can see the Order ID, Book ID, Book Name, Order Date, and Return Status of all their order.<br>
- 'URL' http://localhost:5015/users/order<br>

## Overview:-

### 1). Planning and design:-<br>

(i) Identify the requirements for the system, including user roles, functionalities, and features.<br>
(ii) Define the database schema for the system, including tables for books, members, loans, reservations, etc.<br>
(iii) Determine the relationships between the tables and create foreign key constraints.<br>
(iv) Decide on the API endpoints needed for the frontend to interact with the backend.<br>
(v) Design the user interface and create mockups of the screens for the frontend<br>

### 2). Setting up the Django Backend:<br>

(i) Create a new Django project and app for the library management system.<br>
(ii) Define the database schema by creating Django models for each table in the database.<br>
(iii) Implement the views and serializers needed for each API endpoint.<br>
(iv) Create URL patterns for the API endpoints.<br>
(v) Implement authentication and authorization for the API using Django's built-in authentication system <br>
(vi) Implement unit tests for the backend.

#### 3). Implementing the Angular Frontend:<br>

(i) Create a new Angular project and app for the library management system.<br>
(ii) Design and implement the user interface by creating components and services.<br>
(iii) Implement the Angular services needed to interact with the backend API endpoints using the HttpClient module.<br>
(iv) Implement authentication and authorization in the frontend by creating a login form and using Angular's guards to restrict access to certain pages.<br>
(v) Create unit tests for the frontend.<br>
