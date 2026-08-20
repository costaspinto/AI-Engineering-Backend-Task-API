# AI Engineering Backend Task API

A production-oriented RESTful CRUD API built with **Python and FastAPI** as part of the FlyRank AI Engineering Internship — Week 2, Task 1.

## Project Overview

This project implements a task-management REST API supporting task creation, retrieval, updating, deletion, request validation, HTTP status codes, error handling, in-memory storage, Swagger/OpenAPI documentation, and Git-based development.

The application intentionally uses **in-memory storage** rather than a database, following the Week 2 assignment scope.

## Objectives

- Design RESTful API endpoints.
- Implement complete CRUD functionality.
- Apply appropriate HTTP status codes.
- Validate incoming API requests.
- Handle missing resources with meaningful errors.
- Document and test an API using Swagger UI.
- Demonstrate incremental Git-based development.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Programming language |
| FastAPI | Backend web framework |
| Pydantic | Request validation and data models |
| Uvicorn | ASGI development server |
| Swagger UI / OpenAPI | Interactive API documentation |
| Git | Version control |
| GitHub | Repository hosting |

## Architecture

```text
Client
  │
  │ HTTP Request
  ▼
FastAPI Application
  │
  ├── Route Handling
  ├── Request Validation
  ├── Business Logic
  └── In-Memory Task Store
  │
  ▼
HTTP Response
```

## API Endpoints

| Method | Endpoint | Description | Success | Error |
|---|---|---|---|---|
| GET | `/` | API information | 200 | — |
| GET | `/health` | Health check | 200 | — |
| GET | `/tasks` | Retrieve all tasks | 200 | — |
| GET | `/tasks/{task_id}` | Retrieve one task | 200 | 404 |
| POST | `/tasks` | Create a new task | 201 | 400 |
| PUT | `/tasks/{task_id}` | Update an existing task | 200 | 400 / 404 |
| DELETE | `/tasks/{task_id}` | Delete a task | 204 | 404 |

## Data Model

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "done": false
}
```

| Field | Type | Description |
|---|---|---|
| `id` | Integer | Unique task identifier |
| `title` | String | Task title |
| `done` | Boolean | Completion status |

## HTTP Status Codes

| Status | Meaning | Usage |
|---|---|---|
| 200 | OK | Successful read/update |
| 201 | Created | Successful task creation |
| 204 | No Content | Successful deletion |
| 400 | Bad Request | Invalid request data |
| 404 | Not Found | Task does not exist |

## Project Structure

```text
AI-Engineering-Backend-Task-API/
│
├── .gitignore
├── main.py
└── README.md
```

## Local Setup

### 1. Clone

```bash
git clone https://github.com/costaspinto/AI-Engineering-Backend-Task-API.git
cd AI-Engineering-Backend-Task-API
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
```

### 3. Activate it

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install fastapi uvicorn
```

### 5. Run the API

```powershell
uvicorn main:app --reload
```

API:

```text
http://localhost:8000
```

## Swagger UI

FastAPI automatically generates interactive OpenAPI documentation.

Open:

```text
http://localhost:8000/docs
```

Use **Try it out** to test the complete CRUD workflow.

### Swagger Screenshot

<img width="3832" height="1664" alt="swagger-overview" src="https://github.com/user-attachments/assets/a7f05690-02de-4f8e-9fb1-3a41f3ba80fa" />
<img width="2462" height="1620" alt="post-201-created" src="https://github.com/user-attachments/assets/d81168e2-3278-405c-9616-1f944548a4f4" />
<img width="2814" height="1264" alt="put-200-updated" src="https://github.com/user-attachments/assets/6f472d75-9efa-464f-802b-5347fdce3d52" />
<img width="2456" height="1244" alt="delete-204-no-content" src="https://github.com/user-attachments/assets/09f13b82-e492-454d-9d04-01d542c06594" />
<img width="2494" height="1292" alt="404-not-found" src="https://github.com/user-attachments/assets/0758ee2c-cebb-4172-ba83-f9189c4f5820" />



## Example Requests

### Get all tasks

```bash
curl -i http://localhost:8000/tasks
```

### Get one task

```bash
curl -i http://localhost:8000/tasks/1
```

### Create a task

```bash
curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d "{"title":"Learn API Testing","done":false}"
```

Expected:

```text
HTTP/1.1 201 Created
```

### Update a task

```bash
curl -i -X PUT http://localhost:8000/tasks/1 -H "Content-Type: application/json" -d "{"title":"Learn FastAPI Properly","done":true}"
```

### Delete a task

```bash
curl -i -X DELETE http://localhost:8000/tasks/1
```

Expected:

```text
HTTP/1.1 204 No Content
```

## Error Handling

Requests for non-existent tasks return `404 Not Found`.

Example:

```bash
curl -i http://localhost:8000/tasks/99
```

The response identifies the missing task instead of incorrectly returning `200`.

## Validation

Incoming task data is validated with Pydantic models.

Example:

```json
{
  "title": "Learn API Testing",
  "done": false
}
```

## In-Memory Storage

Tasks are stored in a Python list:

```text
Client
  ↓
FastAPI
  ↓
Python list
```

Data is lost when the server restarts. This is intentional for the assignment; persistent database storage is a future extension.

## Development Workflow

The API was developed incrementally and each stage was tested before moving forward.

```text
Stage 0: hello server
Stage 1: root and health endpoints
Stage 2: read task endpoints
Stage 3: create task endpoint
Stage 4: update task endpoint
Stage 5: delete task endpoint
```

This creates a traceable Git history rather than one large final-state commit.

## Testing Performed

The following were manually verified through Swagger UI:

- Root endpoint
- Health endpoint
- Retrieve all tasks
- Retrieve individual task
- Unknown task → 404
- Create task → 201
- Retrieve newly created task
- Update existing task → 200
- Update unknown task → 404
- Delete existing task → 204
- Delete unknown task → 404

## Key Backend Concepts Demonstrated

- RESTful API design
- HTTP methods
- Request validation
- HTTP status codes
- Error handling
- CRUD operations
- OpenAPI / Swagger documentation
- In-memory data management
- Incremental Git development

## Engineering Decisions

### Why FastAPI?

FastAPI provides Python-based API development, type-hint-driven validation, automatic OpenAPI documentation, built-in Swagger UI, and clear route definitions.

### Why In-Memory Storage?

The assignment focuses on CRUD and request-response behavior before introducing persistent storage.

### Why Incremental Commits?

Each assignment stage was implemented, tested, and committed separately to maintain a traceable development history.

## Limitations

- No persistent database
- No authentication or authorization
- No automated test suite
- No pagination or filtering
- No production deployment
- Data resets when the server restarts

## Future Improvements

- PostgreSQL integration
- SQLAlchemy or SQLModel
- Authentication and authorization
- Automated unit and integration tests
- Docker containerization
- CI/CD pipeline
- Pagination and filtering
- Structured logging
- Environment-based configuration
- Production deployment
- API versioning

## Internship Context

**Program:** FlyRank AI Engineering Internship  
**Track:** Backend Engineering  
**Week:** 2  
**Assignment:** A1 — Build Your First CRUD API

This project demonstrates the transition from understanding HTTP request-response concepts to implementing a functional backend API.

## Author

**Costas Pinto**

Master of Computer Applications  
Specialization in Artificial Intelligence & Machine Learning

GitHub: https://github.com/costaspinto

## License

Created for educational and internship purposes as part of the FlyRank AI Engineering Internship.
