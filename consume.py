# consuming an API
import requests

response = requests.get('http://127.0.0.1:8000/lecturers/2')

print(response.json())