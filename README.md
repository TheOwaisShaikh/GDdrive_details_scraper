# Googledrive_details_scraper
Get Drive Owner Detail With Just Few Lines Of Codes including email



# How to get json key file

To get the JSON key file for authenticating with Google APIs, you typically need to create a service account and download the associated JSON key file. Here are the steps to obtain the JSON key file:

Create a Project on Google Cloud Console:

Go to the Google Cloud Console.
Click on the project drop-down and create a new project or select an existing project.
Enable APIs and Services:

In the Cloud Console, navigate to "APIs & Services" > "Library."
Search for the specific Google API you want to use (e.g., "Google Drive API").
Click on the API, then click the "Enable" button.
Create Service Account:

In the Cloud Console, navigate to "APIs & Services" > "Credentials."
Click the "Create credentials" drop-down and select "Service Account Key."
Fill out the required fields, such as service account name and role.
Choose the role that matches your use case (e.g., "Project" > "Editor" for full access).
Under "Key" type, select "JSON."
Click the "Create" button.
Download JSON Key File:

After creating the service account key, a JSON file containing the credentials will be downloaded to your computer.
Save this JSON file securely. It contains sensitive information and should not be shared publicly.
Now, you can use the path to this JSON key file in your Python code to authenticate with Google APIs. Replace 'YOUR_JSON_KEY_FILE.json' in your code with the actual path to the downloaded JSON key file.

Make sure to protect this JSON key file because it provides access to your Google APIs and services. Do not share it publicly or commit it to a public code repository.

