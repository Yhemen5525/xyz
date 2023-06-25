import requests
import json
import socket

# Function to fetch dummy data from API
def get_dummy_data():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to get IP address
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Fetch dummy data
dummy_data = get_dummy_data()
if dummy_data is not None:
    print("Dummy Data:")
    print(json.dumps(dummy_data, indent=4))
else:
    print("Failed to fetch dummy data.")

# Get IP address
ip_address = get_ip_address()
print("Your IP Address:", ip_address)