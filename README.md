# Flask User Management REST API

A simple REST API built with Flask to manage user data with CRUD operations.

## Setup

1. **Install Flask**
```bash
pip install flask
```

2. **Run the application**
```bash
python app.py
```

Server runs on: `http://127.0.0.1:5000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users` | Get all users |
| GET | `/users/<id>` | Get user by ID |
| POST | `/users` | Create new user |
| PUT | `/users/<id>` | Update user |
| DELETE | `/users/<id>` | Delete user |

## Quick Test

**Browser:** Open `http://127.0.0.1:5000/users`

**cURL Examples:**

```bash
# Get all users
curl http://127.0.0.1:5000/users

# Get specific user
curl http://127.0.0.1:5000/users/1

# Create user
curl -X POST http://127.0.0.1:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@test.com"}'

# Update user
curl -X PUT http://127.0.0.1:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"John Updated"}'

# Delete user
curl -X DELETE http://127.0.0.1:5000/users/1
```

## Sample Data

The API starts with 2 users:
- John Doe (john@example.com)
- Jane Smith (jane@example.com)

## Tech Stack

- Python
- Flask
- In-memory storage (list)

## Notes

- Data is stored in memory (resets on restart)
- Debug mode enabled for development
- Use Postman for easier testing
