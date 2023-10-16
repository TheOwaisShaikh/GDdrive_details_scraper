from google.oauth2 import service_account
from googleapiclient.discovery import build
import re

# Replace with the path to your JSON key file
keyfile = 'key.json'

# Replace with the Google Drive file URL
drive_url = 'https://drive.google.com/drive/u/0/folders/1Mw6lHEnfIZi0Xplm_pZUl9hKSad7hzTn'

# Extract the file ID from the URL
match = re.search(r'/folders/([^/]+)', drive_url)
if match:
    folder_id = match.group(1)

# Create credentials and authenticate
credentials = service_account.Credentials.from_service_account_file(keyfile, scopes=['https://www.googleapis.com/auth/drive'])
drive_service = build('drive', 'v3', credentials=credentials)

try:
    # Retrieve the folder metadata to get the owner's email
    folder_metadata = drive_service.files().get(fileId=folder_id, fields="owners").execute()
    
    if 'owners' in folder_metadata:
        owner_email = folder_metadata['owners'][0]['emailAddress']
        print(f"Owner's Email Address: {owner_email}")
    else:
        print("Owner's Email Address not found.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
