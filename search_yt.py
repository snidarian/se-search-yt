#!/usr/bin/python3
# Selenium program for enabling cli-searching of youtube videos


try:
    from selenium import webdriver
    from selenium.webdriver.firefox import service
    from selenium.webdriver.firefox.service import Service
    from selenium.webdriver.firefox.options import Options

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC    
    # keys class for specific keypresses
    from selenium.webdriver.common.keys import Keys
    
except:
    print("Selenium not installed.. Try 'pip3 install selenium before proceeding'")

try:
    from colorama import Fore
except:
    print("Colorama not installed.. try 'pip3 install colorama before proceeding'")

import argparse
import os
import time


# Setup firefox webdriver and give it a profile
OPTIONS = Options()

profile0 = '6ugn43v9.default-esr'
profile1 = '79rs4mg6.default'

OPTIONS.profile = f'/home/cn1d4r14n/.mozilla/firefox/{profile0}'

# Decide whether program runs headlessly or not. False here is initially a dev dependency
OPTIONS.headless = False


driver = webdriver.Firefox(options=OPTIONS)


# setup colored ansi terminal escape sequences
RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
MAGENT = Fore.MAGENTA
RESET = Fore.RESET


# Reaches youtube main site
def reach_youtube_main_page() -> None:
    driver.get('https://www.youtube.com')

# located input search bar, writes search term into it, and presses enter
def search_global_navigation_bar(search_term, video_count) -> None:
    search_box = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, 'input')))
    # Send the search term to the globalnav bar
    print(f'Searching for {RED}{video_count}{RESET} videos with the term {GREEN}{search_term}{RESET}')
    #print(search_box)
    search_box.send_keys(f"{search_term}")
    # a pause here is necessary between key entries - not sure precisely why
    time.sleep(0.8)
    search_box.send_keys(Keys.RETURN)


# gather results from search made with 'search_global_navigation_bar' function
def gather_video_results(video_count) -> list:
    pass


def scroll_to_unlock_next_video_set() -> None:
    # Where the Page down keys are sent
    html = driver.find_element_by_tag_name('html')
    for _ in range(10):
        html.send_keys(Keys.PAGE_DOWN)
        time.sleep(.4)




def print_video_results(metadata_list) -> None:
    pass


def main() -> None:
    # Setup argparse
    parser = argparse.ArgumentParser(description="Search YT video results and metadata from the command line")
    args = parser.add_argument("query", help="Search term for video results", type=str)
    args = parser.add_argument("-c", "--count", help="Number of video results (default 15)", type=int, default=15)
    args = parser.parse_args()

    # Get request to the youtube mainpage
    reach_youtube_main_page()

    # Enter search term into global navigation bar
    search_global_navigation_bar(args.query, args.count)

    # Search through the results and gather video metadata
    finalized_metadata_list = gather_video_results(args.count)

    # Print the video metadata in concise and color-formatted output
    #print_video_results(finalized_metadata_list)


if __name__=="__main__":
    main()

