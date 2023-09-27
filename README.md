# SSO Invitation handler

This is an example of SSO invitations manager. It sends an email to the invited user and automatically accepts invitations.

## Customization
To customize emails, you must change `src/templates/content.html` and `src/templates/title.txt`

## Config


`API_URL` - URL of BIMData API
`IAM_URL` - URL of BIMData IAM


`EMAIL_HOST` - URL or IP of the SMTP server
`EMAIL_PORT` - Port of the SMTP server
`EMAIL_HOST_USER` - Username of the SMTP server
`EMAIL_HOST_PASSWORD` - Password of the SMTP server
`DEFAULT_FROM_EMAIL` - Email address of emails sender


`INVITATION_SECRET` - Secret used to sign API requests. Must match value set in IdentityProvider config
`ACCEPT_INVITATIONS` - Set to "true" if you want this module to automatically accept invitations. It is not needed if you have set "Auto accept invitation" is your API App settings.

`INVITATION_CLIENT_ID` - Only needed if ACCEPT_INVITATIONS is true
`INVITATION_CLIENT_SECRET` - Only needed if ACCEPT_INVITATIONS is true


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
