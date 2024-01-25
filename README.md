# US.Hardware Data Entry System

## Overview

The **US.Hardware Data Entry System** is a simple yet effective Tkinter-based application designed for data entry and management of hardware sales. This project provides an intuitive graphical user interface (GUI) for users to input customer details, product information, and sales data. The entered data is then stored in an SQLite database, facilitating organized record-keeping and retrieval.

## Key Features

### 1. User-Friendly Interface

The application offers a clean and user-friendly interface, making it easy for users to input information without the need for advanced technical knowledge. The form is divided into sections for customer details, product information, and sales specifics.

### 2. SQLite Database Integration

The project incorporates an SQLite database to persistently store entered data. The database is initialized upon application startup, creating an 'entries' table to store customer names, contact details, product information, pricing, quantities, sales dates, and payment methods.

### 3. Efficient Data Entry

The system ensures efficient data entry by validating and requiring essential information in each field. Users are prompted with a warning if any of the mandatory fields are left blank, ensuring data accuracy.

### 4. Modular Code Structure

The code is organized into modular components, promoting readability, maintainability, and extensibility. Custom Tkinter widgets (`CTkLabel`, `CTkEntry`, `CTkComboBox`, `CTkButton`) from the `customtkinter` module enhance the appearance and functionality of the GUI.

## Requirements

To run this application, ensure you have the following dependencies installed:

- Python (3.x recommended)
- Tkinter library
- SQLite3

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
