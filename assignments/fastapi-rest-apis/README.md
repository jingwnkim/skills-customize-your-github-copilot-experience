# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to create a simple REST API in Python using FastAPI. Students will build endpoints for managing data, validate request payloads, and explore how APIs respond to client requests.

## 📝 Tasks

### 🛠️ Create a FastAPI App

#### Description
Set up a minimal FastAPI application and define the main app object that will serve API routes.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Define a root route that returns a welcome message
- Start the app with a local development server
- Verify the app responds successfully in the browser or API client

### 🛠️ Add CRUD Endpoints

#### Description
Build API endpoints to create, read, update, and delete items in a simple in-memory list.

#### Requirements
Completed program should:

- Create a route to list all items
- Create a route to retrieve one item by ID
- Create a route to add a new item
- Create a route to update an existing item
- Create a route to delete an item
- Return JSON responses in a consistent format

### 🛠️ Validate Requests and Handle Errors

#### Description
Improve the API by validating input data and returning helpful responses for invalid requests.

#### Requirements
Completed program should:

- Use a request model to validate incoming data
- Reject missing or invalid fields with clear error messages
- Handle cases such as missing item IDs gracefully
- Include at least one example request and response in comments or documentation
