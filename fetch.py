import requests

def fetchAndSaveTofile(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)

url = "https://time.com/"

fetchAndSaveTofile(url, "times.html")