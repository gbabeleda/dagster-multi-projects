# Standard Library
import os
import pickle
import logging

# 3rd Party Google
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("extract_google_file.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def authenticate_google_drive() -> Credentials:
    """
    Simple authentication function that returns credentials for Google Drive.
    Saves credentials to token.pickle for future use.
    """
    creds = None
    
    # If we have a token.pickle file, load credentials from it
    if os.path.exists('token.pickle'):
        logging.info("Loading existing credentials...")
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If credentials don't exist or are invalid
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            logging.info("Refreshing expired credentials...")
            creds.refresh(Request())
        else:
            logging.info("Getting new credentials...")
            # Create flow from credentials file
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json',
                ['https://www.googleapis.com/auth/drive.readonly']
            )
            # Let user authenticate in their browser
            creds = flow.run_local_server(port=0)
            
        # Save credentials for next run
        logging.info("Saving credentials for future use...")
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return creds

def list_files_simple(creds: Credentials, page_size=10):
    """
    List just the names of files in Google Drive root.
    """
    # Build the Drive service
    service = build('drive', 'v3', credentials=creds)
    
    # Call the Drive API
    results = service.files().list(
        pageSize=page_size,
        fields="files(name)"  # Only get file names
    ).execute()
    
    files = results.get('files', [])
    
    # Print the files
    if not files:
        logging.error('No files found.')
    else:
        logging.info('Files:')
        for file in files:
            logging.info(f"- {file['name']}")

if __name__ == '__main__':
    # Get credentials
    credentials = authenticate_google_drive()
    
    # List some files
    list_files_simple(credentials)