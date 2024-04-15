# FastAPI with OpenAI and PostgreSQL Integration

This project demonstrates how to use FastAPI to create a simple API that interacts with OpenAI's API and stores responses in a PostgreSQL database.

## Requirements

Ensure you have Python 3.6+ installed on your system. You also need PostgreSQL running and accessible.

## Setup

### Clone the Project

First, clone the repository to your local machine:

```bash
git clone https://your-repository-url-here
cd your_project
```

## Install Dependencies
Install the required Python dependencies by running:
```
pip install -r requirements.txt
```

## Environment Variables
**Create a new .env file and copy the content from .env.example (don’t forget to put your own OPENAI_API_KEY and Postgre DB details)**

## Initialize the Database
Ensure your PostgreSQL database is setup and accessible.

## Running the Application
To start the server, run the following command from the root of your project directory:
```
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```