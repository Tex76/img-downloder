import requests
from bs4 import BeautifulSoup
import os


def website_name(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    images = soup.findAll('img')
    path_setup()
    for i, data in enumerate(images):
        link = data.get('src')
        content = download_image(link)
        with open("./Images/{}.png".format(i), "wb") as file:
            file.write(content)
            file.close()


def path_setup():
    if not os.path.isdir('Images'):
        os.mkdir("Images")


def download_image(img_url):
    try:
        imgCont = requests.get(img_url)
        return imgCont.content
    except Exception as e:
        print(f"Error: {e}")


def main():
    print("Welcome to website image downloader! :)")
    url = input("please enter the website page url: ")
    print("downloading...")
    website_name(url)
    print("Done..")



if __name__ == "__main__":
    main()
