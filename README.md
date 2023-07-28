# Todo API

This is a Todo API built using FastAPI, SQLAlchemy, and Pydantic. It allows users to manage their todo list by providing various endpoints to create, read, update, and delete todos. The API also includes authentication using JSON Web Tokens (JWT) to ensure secure access to user-specific data.

## Installation

To run the Todo API locally, follow these steps:

1. Clone the repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Set up your database and update the configuration in `config.py`.
5. Run the FastAPI application using `uvicorn main:app --reload`.

The API will be accessible at `http://localhost:8000`.

## Endpoints

The Todo API includes the following endpoints:

1. **Register User**: `POST /users`
   - Create a new user by providing a username, email, and password.

2. **Login**: `POST /login`
   - Authenticate the user with their username and password, and receive an access token for subsequent requests.

3. **Deactivate User**: `Delete /users`
   - Deactivate the authenticated user account, which also deactivates all associated todos.

4. **Create Todo**: `POST /todos`
   - Create a new todo by providing the todo name, description, completion date, priority and token key.

5. **Get All Todos**: `GET /todos`
   - Retrieve a list of all todos for the authenticated user, with optional pagination support.

6. **Search Todos**: `GET /todos/search`
   - Search for todos by name, completion date, priority, or completion status.

7. **Mark Todos as Completed**: `PUT /todos`
   - Mark one or more todos as completed by providing a list of todo IDs.

8. **Deactivate User**: `Delete /users`
   - Deactivate the todo for authenticated user account.

9. **Get all User**: `Get /users`
   - For Admin to get all users present.

## Authentication

The API uses JSON Web Tokens (JWT) for user authentication. When a user registers or logs in, they receive an access token that must be included in the `Authorization` header of subsequent requests. The token is validated to ensure secure access to user-specific data.

## Request and Response Formats

The API follows RESTful conventions and uses JSON as the request and response format. Request bodies and response payloads are defined using Pydantic models for data validation and serialization.

## Error Handling

The API returns meaningful error responses for various scenarios, such as invalid input data, unauthorized access, and resource not found. Error messages are descriptive and informative to assist developers in debugging.

## Security

The API ensures secure access to user data through authentication using JWT. Passwords are hashed before storing them in the database to protect user information.

## Deployment

To deploy the Todo API to a production environment, ensure to set the appropriate environment variables for the database configuration and JWT secret key. Additionally, use a web server like Gunicorn and a production-ready ASGI server like Uvicorn.

## Contributing

If you would like to contribute to the Todo API, please fork the repository, create a new branch, and submit a pull request. We welcome your feedback, bug reports, and feature requests.

## License


---

Thank you for using the Todo API! I hope it helps you manage your tasks effectively and efficiently. If you have any questions or need assistance, feel free to open an issue on the repository. Happy coding!