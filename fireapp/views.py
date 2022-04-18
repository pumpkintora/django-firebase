from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('secret.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://aptvise-test-ea05f-default-rtdb.asia-southeast1.firebasedatabase.app"
})

ref = db.reference('Data')
print(ref.get()['Framework'])

def index(request):
    name = ref.get()['Name']
    stack = ref.get()['Stack']
    framework = ref.get()['Framework']
    
    context = {
        'name': name,
        'stack': stack,
        'framework': framework
    }
    return render(request, 'index.html', context)
