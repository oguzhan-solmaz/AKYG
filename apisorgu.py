import shutil
import requests

def showimg():
    size1=input("resimin birinci boyutunu girin: ")
    size2=input("resimin ikinci boyutunu girin: ")
    my_url = "https://place.dog/" +  size1 + "/" + size2
    response = requests.get(my_url, stream=True)
    with open('my_image.png', 'wb') as file:
        shutil.copyfileobj(response.raw, file)
    del response

    from PIL import Image

    img = Image.open('my_image.png')
    img.show()


showimg()