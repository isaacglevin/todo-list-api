# Todo List API

A simple RESTful To-Do List API built with Flask and Flask-RESTX, featuring Swagger/OpenAPI documentation.

## Features

- Full CRUD operations (Create, Read, Update, Delete)
- In-memory storage (no database required)
- Auto-incrementing IDs
- Input validation
- Swagger UI documentation at `/docs`
- Production-ready deployment configuration

## Data Model

A Todo object has the following structure:

```json
{
  "id": 1,
  "text": "Complete assignment",
  "completed": false
}
```

## API Endpoints

### GET /todos
Returns all todos.

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "text": "Complete assignment",
    "completed": false
  }
]
```

### POST /todos
Creates a new todo.

**Request Body:**
```json
{
  "text": "New todo item",
  "completed": false
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "text": "New todo item",
  "completed": false
}
```

**Note:** The `text` field is required. The `completed` field is optional and defaults to `false`.

### PUT /todos/{id}
Updates an existing todo.

**Request Body:**
```json
{
  "text": "Updated todo text",
  "completed": true
}
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "text": "Updated todo text",
  "completed": true
}
```

**Note:** Both `text` and `completed` are optional in the request body. Only provided fields will be updated.

### DELETE /todos/{id}
Deletes a todo.

**Response:** `204 No Content`

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or download this repository**

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

   Or set a custom port:
   ```bash
   PORT=8080 python app.py
   ```

The API will be available at `http://localhost:5000` (or your specified PORT).

## Swagger Documentation

Once the server is running, visit:
- **Swagger UI:** http://localhost:5000/docs

The Swagger UI provides interactive documentation where you can:
- View all available endpoints
- See request/response schemas
- Test endpoints directly from the browser

## Testing the API

### Using cURL

**Get all todos:**
```bash
curl http://localhost:5000/todos
```

**Create a todo:**
```bash
curl -X POST http://localhost:5000/todos \
  -H "Content-Type: application/json" \
  -d '{"text": "Buy groceries", "completed": false}'
```

**Update a todo:**
```bash
curl -X PUT http://localhost:5000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"text": "Buy groceries and cook dinner", "completed": true}'
```

**Delete a todo:**
```bash
curl -X DELETE http://localhost:5000/todos/1
```

### Using Swagger UI

1. Navigate to http://localhost:5000/docs
2. Click on any endpoint to expand it
3. Click "Try it out"
4. Fill in the required parameters/body
5. Click "Execute"
6. View the response

## Deployment

This API is configured for deployment on platforms like Render, Railway, or Fly.io:

- Binds to `0.0.0.0` (all interfaces)
- Uses `PORT` environment variable (defaults to 5000)
- No database dependencies

### Example Deployment on Render

1. Create a new Web Service
2. Connect your GitHub repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python app.py`
5. Render will automatically set the `PORT` environment variable

## Important Notes

- **No persistence:** Todos are stored in memory and will be lost when the server restarts
- **No authentication:** This is a simple API without user authentication
- **Single instance:** In-memory storage means todos are not shared across multiple server instances

## License

This project is created for educational purposes.

