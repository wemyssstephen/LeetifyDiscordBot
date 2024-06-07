import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from PIL import Image


hz_website = "https://leetify.com/app/profile/76561197978714095"
dg_website = "https://leetify.com/app/profile/76561197976021559"
pb_website = "https://leetify.com/app/profile/76561197966797302"
dl_website = "https://leetify.com/app/profile/76561198122168878"
path = "C:/Users/wemys/PycharmProjects/LeetifyDiscordBot"


def get_profile_page(name: str):
    """Grabs the profile page of Me, Jamie, Jordan or Ed."""
    driver = webdriver.Firefox()
    driver.maximize_window()

    if name == "Steve":
        driver.get(hz_website)
    elif name == "Jamie":
        driver.get(dg_website)
    elif name == "Ed":
        driver.get(pb_website)
    elif name == "Jordan":
        driver.get(dl_website)
    time.sleep(2)

    driver.save_full_page_screenshot(f"{path}/screenshot.png")
    print(f"Saved screenshot at {path}/screenshot.png")
    driver.quit()

    img = Image.open(f"{path}/screenshot.png")
    width, height = img.size
    print(f"Width: {width}, Height: {height}")
    area = (750, 400, 2050, 1100)
    cropped = img.crop(area)
    cropped.save(f'{path}/croppedscreenshot.png')

response = requests.get(hz_website)
soup = BeautifulSoup(response.text, 'lxml')


