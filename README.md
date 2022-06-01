# SSO Invitation handler

This is an example of SSO invitations manager. It sends an email to the invited user and automatically accepts invitations.


## Install

- Download poetry: https://python-poetry.org/docs/#installation
- `poetry shell`
- `poetry install` : install all requirements

## Usage

- `flask run`


NB: `FLASK_ENV` env-var can be used to customize behaviour:

- `FLASK_ENV="development"` enable logs and hotreload


## The .env file

The `.env` file is a representation of additionnal ENV variable in order to override default config.
You can duplicate `.env.example` in `.env` and customize your config.
All env variable defined in the file `.env.example` are mandatory.


## Setup git hooks

Install a pre-commit hook with black and flake8 check
```
pre-commit install
```
