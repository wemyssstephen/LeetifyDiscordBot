import time
import pandas as pd
from tabulate import tabulate
from selenium import webdriver
from selenium.webdriver.common.by import By
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

    # Returns the correct Leetify profile page from name.
    # TODO: Find a way to return any profile from a search term.
    if name == "Steve":
        driver.get(hz_website)
    elif name == "Jamie":
        driver.get(dg_website)
    elif name == "Ed":
        driver.get(pb_website)
    elif name == "Jordan":
        driver.get(dl_website)

    # Wait for the profile to load in browser.
    time.sleep(2)

    # Grab the data.
    stats = driver.find_element(By.ID, "stats-overview").text.split("\n")
    match_history = driver.find_element(By.ID, "match-history").text.split("\n")

    # Quit selenium webdriver.
    driver.quit()

    # Manipulate data into list of lists.
    del stats[1:3]
    stats_lst = []
    for i in range(0, len(stats)-5):
        if stats[i] in ["AIM", "UTILITY", "POSITIONING", "OPENING DUELS", "CLUTCHING",
                        "WIN RATE", "LEETIFY RATING", "T RATING", "CT RATING"]:
            stats_lst.append(stats[i:i+2])
        elif stats[i] in ["SOLO", "2-4 STACK", "5 STACK"]:
            del stats[i:i+2]

    print(stats_lst)

    stats_table = pd.DataFrame(stats_lst, columns=["Overview", "Score"])
    print(stats_table.to_markdown(index=False))
    # print(tabulate(stats_table, headers=["Overview", "Score"], tablefmt="pipe", showindex=False))

    match_history_table = pd.DataFrame(match_history)


def save_and_crop_screenshot(path: str, driver: webdriver.Firefox):
    # Take a screenshot.
    driver.save_full_page_screenshot(f"{path}/screenshot.png")
    print(f"Saved screenshot at {path}/screenshot.png")
    # Crop the image to include only the profile header and save.
    img = Image.open(f"{path}/screenshot.png")
    width, height = img.size
    print(f"Width: {width}, Height: {height}")
    area = (750, 400, 2050, 1100)
    cropped = img.crop(area)
    cropped.save(f'{path}/croppedscreenshot.png')


get_profile_page("Steve")
