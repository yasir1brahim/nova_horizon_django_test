import os
import requests
from dotenv import load_dotenv
from django.conf import settings


load_dotenv()

API_KEY = os.getenv('APOLLO_API_KEY')
BASE_URL = os.getenv('APOLLO_BASE_URL')


"""
We can implement proxy rotation with following ways.
    1. Using Free Proxy Lists
    2. Using TOR as a Proxy
    3. Use Proxy Rotating Services with Free Tiers
"""

# Here we have configure TOR as a SOCKS5 Proxy, To setup TOR follow the steps from README.md 
proxies = settings.PROXIES_LIST

def get_account_stages():
    headers = {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
        'X-Api-Key': API_KEY 
    }
    
    response = requests.get(f'{BASE_URL}account_stages', headers=headers, proxies=proxies) 
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def create_account_stage_on_apollo(data):
    apollo_endpoint = f'{BASE_URL}/accounts'
    headers = {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
        'X-Api-Key': API_KEY 
    }
    
    response = requests.post(apollo_endpoint, headers=headers, json=data)
    return response