CREATE DATABASE IF NOT EXISTS hotel;
USE hotel;

CREATE TABLE Guests (
    guest_id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(50),
    first_name VARCHAR(50),
    middle_name VARCHAR(50),
    city VARCHAR(100)
);

CREATE TABLE Rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    rooms_count INT,
    floor INT,
    tv BOOLEAN,
    fridge BOOLEAN,
    places INT,
    category VARCHAR(20),
    price_per_day DECIMAL(10,2)
);

CREATE TABLE Registration (
    reg_id INT AUTO_INCREMENT PRIMARY KEY,
    guest_id INT,
    room_id INT,
    arrival_date DATE,
    days INT,
    FOREIGN KEY (guest_id) REFERENCES Guests(guest_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);