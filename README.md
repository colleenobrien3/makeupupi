# Makeupupi

## Description

In the past, I have looked for interesting datasets and API's with information concerning cosmetics brands, but have been unable to find them. So I decided to create my own. I am particularly interested in furthering the mission of cruelty-free brands, so I compiled a list of such brands from CrueltyFreeKitty.com and arranged the data as a fixture file for my Django API's Company model. While creating the [frontend tool](https://hilight.netlify.app/) for searching the database, I decided to implement an autocomplete tool for the input box, so I added a new model (Candidate) to my API that stores brands that have been searched.

## Languages and Technologies

- Python
- Django REST Framework
- PostgreSQL

## Getting Started

Click [here](https://arcane-brook-10088.herokuapp.com) to view the deployed API.

## Dependencies

In order to setup the API and database locally, you will need the following installed on your machine:

- ['python'](https://www.python.org/downloads/)
- ['pipenv'](https://github.com/pypa/pipenv)
- ['postgresql'](https://www.postgresql.org/docs/9.3/tutorial-install.html)

## Setup and Installation

1. Clone this repository.

In your command line, enter:

```
git clone https://github.com/colleenobrien3/programmingChallengeAPI.git
```

2. Enter cloned repository.

3. Run the command `pipenv install` to set up the virtual environment and install the dependencies in the Pipfile.

4. Open the virtual shell with the command `pipenv shell`.

5. To load the sql file into Postgres and create the database, run the following:

```
psql -U postgres -f settings.sql
```

6. Run `python manage.py migrate` to set up the model as a table in the database.

7. Run the command `python manage.py runserver` to set up the local server.

## Coding Style

I installed [autopep8](https://github.com/hhatto/autopep8) for Python code format.

## Database Setup

The database is called 'makeupupi,' and the user is called 'admin'. When you run migrations, the tables called 'makeupupi_company' and 'makeupupi_candidate' will be created. These tables represent models that include fields for the company's or candidate's name and an id number.

## API Paths

| Method |    Path     | Description                  |
| ------ | :---------: | ---------------------------- |
| GET    | /companies  | Retrieves companies          |
| GET    | /candidates | Retrieves all words searched |
| POST   | /candidates | Adds a new word to the table |

## Next Steps

Please click [here](https://hilight.netlify.app/) to view the deployed frontend, and [here](https://github.com/colleenobrien3/react_cruelty_free) to view the frontend repo.
