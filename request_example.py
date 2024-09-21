import requests

url = "https://www.youtube.com"  
response = requests.get(url)
print(response.text)
