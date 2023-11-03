# Task Management Application with Django and PostgreSQL

This is a simple task management application built with Django and PostgreSQL. The application is containerized using Docker for easy deployment and scalability.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Postgres](https://www.postgresql.org/)

## Getting Started

1. Clone the repository:

    ```bash
   
    git clone https://github.com/AsifAhmed16/taskManagement.git
   
    cd taskManagement
   
    ```

2. Copy the example environment file and customize it inside taskManagement application directory:

    ```bash
   
    cp .env.example .env
   
    ```

    Update the `.env` file with your specific configuration, such as database credentials and Django settings.


3. Build and start the Docker containers:

    ```bash
   
    docker-compose up -d --build
   
    ```

   Access the application by the url:
    [http://localhost:8000](http://localhost:8000)

   Access the Django admin panel:
    [http://localhost:8000/admin/](http://localhost:8000/admin/)


4. Create a user by Django default user-registration and you will be automatically logged into the system:
    [http://0.0.0.0:8000/register/](http://0.0.0.0:8000/register/)

    [http://0.0.0.0:8000/login/](http://0.0.0.0:8000/login/)

    [http://0.0.0.0:8000/logout/](http://0.0.0.0:8000/logout/)

    [http://0.0.0.0:8000/change_password/](http://0.0.0.0:8000/change_password/)

    ```bash
   
   Functionalities -
   
   1. User registration and login functionality.
   2. Users is able to access task management features when logged in only.
   3. Users are able to change their password and log out.
   
    ```


5. CRUD Functionalities for Task:

    TaskList - [http://0.0.0.0:8000/home/](http://0.0.0.0:8000/home/)

    Create - [http://0.0.0.0:8000/tasks/add/](http://0.0.0.0:8000/tasks/add/)

    Update - (//0.0.0.0:8000/tasks/update/<id>)

    Delete - (//0.0.0.0:8000/tasks/delete/<id>)

    Details - (//0.0.0.0:8000/tasks/details/<id>)

    Search - (//0.0.0.0:8000/tasks/search/<key>)

    Filter - (//0.0.0.0:8000/tasks/filter/<key>)

    ```bash
   
   Functionalities -
   
   1. Users can create a new task by providing a title, description, and due date. 
   2. Users can view a list of all their tasks, showing the title and due date.
   3. Users can click on a task to view its details (including the description).
   4. Users can update the task (title, description, and due date) or delete it.
   5. Tasks is categorized as "To Do," "In Progress," or "Done." Users can change the status of a task between these categories.

    ```
   
    ```bash
   
   Additional Functionalities -
   
   User can create Maximum 5 tasks a day.

    ```

6. Other features:

    ```bash
   
   Features -
   
   1. Django built-in authentication system is used.
   2. Proper input validation is available and potential errors were handled.
   3. Used Django forms for data input.
   4. Django Object-Relational Mapping (ORM) for database operations.
   5. Clear and user-friendly interface.
   6. Unit tests were implemented to ensure code quality.
   7. Source code is available in Git.
   8. Application is containerized.
   9. Resource policies are applied. (logical limitation to the tasks that can be assigned to a user in a certain time window.)

    ```

7. Deployment:

    ```bash
   
   The project is deployed in the hosting service - PythonAnywhere.
   
    ```



PythonAnyWhere:
    [https://www.pythonanywhere.com/](https://www.pythonanywhere.com/)



## Live Demo Link:

- [https://www.pythonanywhere.com/](https://www.pythonanywhere.com/)


## Usage

- Use the Django admin panel to manage tasks and users.
- The API is available at [http://localhost:8000/api/](http://localhost:8000/api/)
