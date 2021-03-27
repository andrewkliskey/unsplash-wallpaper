# Unsplash Wallpaper
Set an image from unsplash.com as your background, simple python script.

![Example image](https://raw.githubusercontent.com/andrewkliskey/unsplash-wallpaper/main/preview.png)

### Requirments
Linux with Gnome Desktop Enviroment - (Submit PR with other Desktop Enviroment's)

[Unsplash API Key](https://unsplash.com/developers)

### Install
Download: `curl -o unspashbackround.py https://raw.githubusercontent.com/andrewkliskey/unsplash-wallpaper/main/unsplashbackground.py`

### Usage
```
Usage: unsplashbackground.py [OPTIONS]

Options:
  -d, --desktop         Desktop Enviroment - gnome
  -o, --orientation     Orientation of image - landscape, portrait, squarish
  -c, --collection      Collection - eg. wallpapers, nature, travel
  -q, --query           Query - eg. pizza, coffee, train
  -a, --authorization   Unspash API Access Key
```
Desktop & Authorization arguments required.

### Example
`python3 unsplashbackground.py -d gnome -o landscape -c wallpaper -q 'New York City' -a API_ACCESS_KEY`
