from urllib.request import urlopen

url = 'http://www.python.org/'
with urlopen(url) as f:
    doc = f.read().decode()
    with open('pythonhome.html', 'w') as h:
        h.writelines(doc)