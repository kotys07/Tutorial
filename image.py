import requests

url =  "http://craphound.com/images/1006884_2adf8fc7.jpg"
response = requests.get(url)
if response.status_code == 200:
    with open("Users/Denis/Downloads/sample.jpg", 'wb') as f:
        f.write(response.status_code)
