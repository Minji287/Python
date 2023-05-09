from urllib.request import urlopen

imgurl = 'https://cdn.imweb.me/upload/S202207202685e30f16e24/8b48c67f8cdf6.jpeg'
imgname = imgurl.split('/')[-1]
try:
    with urlopen(imgurl) as f:
        with open(imgname, 'wb') as h:
            img = f.read()
            h.write(img)
except Exception as e:
    print(e)