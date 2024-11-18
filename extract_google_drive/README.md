# Notes

## Setup 
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

## Simple Google Drive Authentication




# Concepts:

## Authentication
Pickle File
- a way to serialize (convert to byte stream) and deserialize (convert back to a python object) python objects.
- saves the exact state of a python object to a file
- why use a pickle when dealing with authentication
    - credentials object contains important authentication information: 
        - access tokens 
        - refresh tokens
        - token expiration times
        - other oauth2 related data
    - we want to save this exact state so users dont have to re-authenticate everytime they run this script
    - pickle preserves all complex object data structure exactly as is
- Benefits
    - Simpler Code
    - Preservers all object attributes exactly
    - No need to manually reconstruct objects
    - Handles complex python objects naturally
- Cons
    - Not secure against malicious data / untrusted files
    - Not compatible across different python versions
    - Files are binary, not human-readable like JSON
    - Platform/OS-dependent 

Alternative method to using pickle file
```python
# Instead of pickle, we could save just the basic token info to a JSON file:
import json

# Saving
token_info = {
    'token': creds.token,
    'refresh_token': creds.refresh_token,
    'token_uri': creds.token_uri,
    'expiry': creds.expiry.isoformat() if creds.expiry else None
}
with open('token.json', 'w') as f:
    json.dump(token_info, f)

# Loading
with open('token.json', 'r') as f:
    token_info = json.load(token_info)
    # Would need to reconstruct the Credentials object
    creds = Credentials(
        token=token_info['token'],
        refresh_token=token_info['refresh_token'],
        token_uri=token_info['token_uri'],
        # Would need to parse expiry back to datetime
        expiry=parse_datetime(token_info['expiry']) if token_info['expiry'] else None
    )
```