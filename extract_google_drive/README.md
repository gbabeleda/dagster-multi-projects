# Notes

Okay so apparently to even be able to do this locally we need to create a project on the google cloud console

### Setup Google Cloud Project
- Go to cloud console
- Create new project
- Go to APIs & Services
- Search for and enable APIS you need

For this one we just need the Google Drive API


### Configure OAuth Consent Screen
- Go to APIs & Services -> OAuth consent screen
- Choose External User Type (unless youre in a Google Workspace organization)
- Fill in required information
- Can skip scopes
- Add your email as a test user

An external user is any test user with a google account. The app will start in testing mode and will only be available to users you add to the list of test users

### Create OAuth 2.0 Client Credentials
- Go to APIs & Services -> Credentials
- Create Credentials -> OAuth client ID
- Choose Desktop application as application type
- Give it a name
- Download the JSON file

