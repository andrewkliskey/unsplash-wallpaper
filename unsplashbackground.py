import os
import requests
import json
import click
import shutil


def imageUrl(queryurl, desktop, authorization):
    response = requests.get(queryurl, headers = {'Accept-Version':'v1', 'Authorization':'Client-ID '+authorization})
    y = json.loads(response.content)
    image_url = y["urls"]["raw"]

    image = requests.get(image_url, stream = True)

    if image.status_code == 200:
        image.raw.decode_content = True
        
        with open("unspash.jpg",'wb+') as f:
            shutil.copyfileobj(image.raw, f)
            
        print('Image sucessfully Downloaded: unspash.jpg')

        imageFullPath = os.path.abspath("unspash.jpg")

        if desktop == "gnome":
            try:
                os.system("gsettings set org.gnome.desktop.background picture-uri " + imageFullPath)
                print("Background Set")
            except:
                print("Unable to set background")
        else:
            print("Unable to determine Desktop Enviroment")

    else:
        print('Image Couldn\'t be retreived')


@click.command()
@click.option("--desktop", "-d", help="Desktop Enviroment - gnome")
@click.option("--orientation", "-o", help="Orientation of image - landscape, portrait, squarish")
@click.option("--collection", "-c", help="Collection - eg. wallpapers, nature, travel")
@click.option("--query", "-q", help="Query - eg. pizza, coffee, train")
@click.option("--authorization", "-a", help="Unspash API Access Key")
def generatequery(desktop, orientation, collection, query, authorization):
    api_endpoint = "https://api.unsplash.com/photos/random?"
    url = api_endpoint

    if orientation is not None:
        url+=f"orientation={orientation}&"

    if collection is not None:
        url+=f"collection={collection}&"

    if query is not None:
        url+=f"query={query}&"


    imageUrl(url, desktop, authorization)

if __name__ == '__main__':
    url = generatequery()