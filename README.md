# MySQL-Python Database Management System

This project is a Python-based database management system using MySQL as the backend. It provides functionalities to create, manage, and interact with databases and tables through a command-line interface. Users can perform various operations like inserting, updating, deleting, and searching records in the database.

## Features

- **Database Creation**: Create a new MySQL database or connect to an existing one.
- **Table Management**: Create new tables, add attributes, remove attributes, and define foreign keys.
- **CRUD Operations**: 
  - **C**reate: Insert new records into the table.
  - **R**ead: Fetch and display all records from a table.
  - **U**pdate: Update existing records based on specific conditions.
  - **D**elete: Remove records or delete all records from a table.
- **Search Functionality**: Search for records in a table based on specific column values.
- **Foreign Key Management**: Add foreign keys to maintain relational integrity between tables.

## Prerequisites

- Python 3.x
- MySQL Server
- MySQL Connector for Python

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Prathamesh1407/MySQL-with-Python.git
    cd MySQL-with-Python
    ```

2. **Install the required Python package**:
    ```bash
    pip install mysql-connector-python
    ```

3. **Run the application**:
    ```bash
    python main.py
    ```

## Usage

Upon running the application, you will be prompted to choose between creating a new database or connecting to an existing one. You can then manage tables within the selected database and perform various operations as needed.

### Main Menu Options

1. **Insert**: Add a new record to the table.
2. **Display All**: Fetch and display all records from the selected table.
3. **Delete User**: Delete a specific record based on a chosen column.
4. **Update**: Update a specific record based on a chosen condition.
5. **Delete All**: Delete all records from the table.
6. **Search**: Search for records based on a specific column value.
7. **Add Attribute**: Add a new attribute (column) to the table.
8. **Remove Attribute**: Remove an attribute (column) from the table.
9. **Foreign Key**: Define a foreign key relationship between tables.
10. **Exit**: Exit the application.

### Example

Here's an example of how you might interact with the application:

```bash
0 : New Database 
1 : Existing Database 
1
Enter password to your Database 
<password>
These are your Exisiting Databases
[... list of databases ...]

Enter the Existing Database name 
[... Database Name ...]
0 : New Table 
1 : Existing Table 
1
These are your Exisiting Tables
[... list of tables ...]

Enter the Table name 
[... Table Name ...]

1:Insert
2:Display All user
3:Delete user
4:Update
5.Delete all
6.Search
7.Add Attribute
8.Remove Attribute
9.Foreign Key
10.Exit



## Contributing

If you wish to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Please ensure that your code adheres to the existing style and structure of the project.

## Acknowledgments

<h2><a href="https://dev.mysql.com/doc/">MySQL Documentation</a></h2>
- [Python MySQL Connector Documentation](https://dev.mysql.com/doc/connector-python/en/)

