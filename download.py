import requests

def download(url, name):
    r = requests.get(url, allow_redirects=True)

    open(name, 'wb').write(r.content)