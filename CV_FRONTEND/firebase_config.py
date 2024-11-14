import firebase_admin
from firebase_admin import credentials

# Initialize Firebase Admin SDK with the credentials
cred = credentials.Certificate('key.json')

firebase_admin.initialize_app(cred)