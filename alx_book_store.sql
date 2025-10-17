CREATE DATABASE IF NOT EXISTS alx_book_store


CREATE Book (
    book_id INT Primary Key,
    title VARCHAR(130) NOT NULL,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
    price DOUBLE(10,2)
    publication_date DATE
);

CREATE Author (
    author_id INT Primary Key,
    author_name VARCHAR(215) NOT NULL,
);

CREATE Customers (
    customer_id INT Primary Key,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) UNIQUE,
    adress TEXT
);

CREATE Orders (
    order_id INT Primary Key,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    order_date Date
);

CREATE Orders_Details (
    orderdetailid INT Primary Key,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
    FOREIGN KEY(book_id) REFERENCES Book(book_id)
    quantity DOUBLE(10,2)
)