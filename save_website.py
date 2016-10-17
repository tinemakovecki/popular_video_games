import requests

def save_website(url, file_name):
    r = requests.get(url)
    with open(file_name, 'w') as file:
        file.write(r.text)
        print('Saved!')