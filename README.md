# Aban Project

The Aban Project is a Python-based application that integrates cryptocurrency functionalities, user management, and exchange features. This project provides tools for managing users, handling assets, and interacting with cryptocurrency exchanges.

Features
User Management: Tools for creating and managing user accounts.
Cryptocurrency Support: Functions for handling cryptocurrency-related operations.
Exchange Integration: Facilitates interaction with various cryptocurrency exchanges.
Modular Structure: Organized directories for better maintainability (users, assets, crypto_currencies, etc.).
## Getting Started

### Prerequisites

Before running the project, you'll need to have the following installed on your machine:

- Python 3
- PostgreSQL
- Docker (if running with Docker)

### Environment Variables

This project uses environment variables to store sensitive information such as database credentials. To run the project, you'll need to create a `.env` file in the root directory of your project and add the required variables.

1. Create a `.env` file in the root directory of your project:

```bash
touch .env
```

2. Open the `.env.sample` file and copy its contents, paste the contents of the `.env.sample` file into the `.env` file.

3. Replace the default values of the variables with your own values.

```
POSTGRES_USER=your_postgres_username
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_database_name
POSTGRES_HOST=your_database_host
POSTGRES_PORT=your_database_port

```

Save the `.env` file.

### Running Locally

To run the project locally, follow these steps:

1. Ensure that PostgreSQL is installed and running locally.
2. Clone the repository to your local machine:

```bash
git clone https://github.com/hnbz/aban_project
cd aban_project
```

3. Install the project's dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Create a superuser account:

````bash
python manage.py create_superuser
````

5. Run the development server:

````bash
python manage.py runserver
````

Once the server is running, you can access the API at http://localhost:8000/.

### Running with Docker

To run the project using Docker, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/hnbz/aban_project
cd aban_project
```

2. Build and start the Docker containers:

````bash
docker-compose build
docker-compose --env-file=.env up
````

Once the containers are running, you can access the API at http://localhost:8000/.

#### Running Tests

To run the tests, follow these steps:

1. Activate the virtual environment:

```bash
source venv/bin/activate
```

2. Ensure that the project's dependencies are installed:

```bash
pip install -r requirements.txt
```

3. Run the tests:

```
python manage.py test
```

This will run all the tests in the project.

Once the tests have completed running, you should see a summary of the test results in your terminal.