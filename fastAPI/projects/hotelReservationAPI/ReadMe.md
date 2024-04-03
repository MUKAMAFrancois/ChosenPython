
# Hotel Room Reservation System

This project is a web application built using FastAPI and MongoDB that allows users to search for hotels, view room availability, and make reservations. It provides a user-friendly interface for both guests and hotel administrators.

## Features

### Guest Features

- Search for hotels based on location, date range, and other criteria
- View hotel details, including amenities, room types, and pricing
- Check room availability and pricing
- Make room reservations
- View and manage existing reservations

### Admin Features

- Manage hotel information, including details, amenities, and room types
- Update room availability and pricing
- View and manage guest reservations
- Generate reports on hotel occupancy and revenue

## Technologies Used

- **FastAPI**: A modern, fast, and high-performance web framework for building APIs with Python.
- **MongoDB**: A flexible and scalable NoSQL database used for storing hotel, room, and reservation data.
- **Pydantic**: A data validation and parsing library used for defining data models and schemas.
- **Motor**: An asynchronous Python driver for MongoDB used for efficient database operations.
- **Passlib**: A library for secure hashing and validation of passwords.

## Installation

1. Create a virtual environment and activate it:

```
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Set up environment variables for MongoDB connection and other settings.

6. Run the application:

```
uvicorn main:app --reload
```

The application should now be accessible at `http://localhost:8000`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements,please submit a pull request.



