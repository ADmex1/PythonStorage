//Works Well for Phising Web
import urllib
import requests
import random
import string

url = "Any Url"

def generate_random_string(length):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=length)) 

while True:
   data = {   }
   
   response = requests.post(url, data=data)
   if response.status_code == 200:
      print("Sent")
   else:
      print("Error")
