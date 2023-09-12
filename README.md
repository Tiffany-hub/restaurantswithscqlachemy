# restaurantswithscqlachemy
This project sets up a simple database to store restaurant reviews, along with information about the restaurants and customers.

## Table of Contents
- [Usage](#usage)
- [Models](#models)
- [Sample Data](#sample-data)
- [License](#license)

## Usage

- To run the script, use:
   ```
   python seeds.py
   ```

- This will create the necessary tables and add some sample data to get you started.


## Models

### Restaurant

- **Attributes**:
  - `id` (Integer, Primary Key)
  - `name` (String)
  - `price` (Integer)

- **Relationships**:
  - One-to-Many with `Review` (One restaurant can have multiple reviews)

### Customer

- **Attributes**:
  - `id` (Integer, Primary Key)
  - `first_name` (String)
  - `last_name` (String)

- **Relationships**:
  - One-to-Many with `Review` (One customer can leave multiple reviews)

### Review

- **Attributes**:
  - `id` (Integer, Primary Key)
  - `rating` (Integer)

- **Relationships**:
  - Many-to-One with `Customer` (Many reviews can be left by one customer)
  - Many-to-One with `Restaurant` (Many reviews can be for one restaurant)

## Sample Data

The script `seeds.py` adds the following sample data:

- **Restaurants**:
  1. Name: Restaurant A, Price: 3
  2. Name: Restaurant B, Price: 2

- **Customers**:
  1. Name: John Doe
  2. Name: Jane Smith

- **Reviews**:
  1. Rating: 4, Comment: Great food!, Customer: John Doe, Restaurant: Restaurant A
  2. Rating: 5, Comment: Excellent service!, Customer: Jane Smith, Restaurant: Restaurant B


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
