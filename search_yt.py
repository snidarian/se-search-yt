#!/usr/bin/python3
# Selenium program for enabling cli-searching of youtube videos


try:
    from selenium import webdriver
    from selenium.webdriver.firefox import service
    from selenium.webdriver.firefox.service import Service
    from selenium.webdriver.firefox.options import Options
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

from selenium.webdriver.firefox import options




# Setup firefox webdriver and give it a profile
OPTIONS = Options()

profile0 = '6ugn43v9.default-esr'
profile1 = '79rs4mg6.default'

OPTIONS.profile = f'/home/cn1d4r14n/.mozilla/firefox/{profile0}'

# Decide whether program runs headlessly or not. False here is initially a dev dependency
OPTIONS.headless = False


driver = webdriver.Firefox(options=OPTIONS)



def main() -> None:
    # Setup argparse
    parser = argparse.ArgumentParser(description="Search YT video results and metadata from the command line")
    args = parser.add_argument("query", help="Search term for video results", type=str)
    args = parser.add_argument("-c", "--count", help="Number of video results (default 15)", type=int, default=15)
    args = parser.parse_args()
    


if __name__=="__main__":
    main()

