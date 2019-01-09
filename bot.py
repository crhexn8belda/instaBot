# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
from termcolor import colored
from getpass import getpass
from os import system
from platform import platform


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)


    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)



        # gathering photos
        pic_hrefs = []
        try:
            time.sleep(2)
            # get tags
            hrefs_in_view = driver.find_elements_by_tag_name('a')
            # finding relevant hrefs
            hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                             if '.com/p/' in elem.get_attribute('href')]
            # building list of unique photos
            [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
            print("we are giong to like " + str(len(pic_hrefs)))

        except Exception:
            pass


        # Liking photos and comment

        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            print (colored("photo link : "+pic_href,"yellow"))
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                like_button().click()

                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1


banner = """
                 __^__                                                        __^__
                ( ___ )------------------------------------------------------( ___ )
                 | / |                                                        | \ |
                 | / |       INSTAGRAM AUTO LIKE ON YOUR NICHE BOT            | \ |
                 |___|                                                        |___|
                (_____)------------------------------------------------------(_____)
                                Coded by : Crhex_n8tbleda
                                
                    FB : https://www.facebook.com/profile.php?id=100008152720330
                    


                     
"""



if "Windows" in platform():
    system("cls")
else:
    system("clear")

print(colored(banner,"yellow"))

username = str(raw_input(colored("your Instagram Username >>>>>>>>>>>> ","blue")))
password = str(getpass(colored("Your Instagram password >>>>>>>>>>>> ","blue")))


ig = InstagramBot(username, password)
ig.login()


hashtags = ['animals', 'animal', 'pet', 'socialsteeze', 'dog', 'cat', 'dogs', 'cats', 'photooftheday', 'cute', 'pets', 'instagood', 'animales', 'cute', 'love', 'nature', 'animallovers', 'pets_of_instagram', 'petstagram', 'petsagra', 'dog', 'dog', 'puppy', 'pup', 'socialsteeze', 'cute', 'instagood', 'dogs_of_instagram', 'pet', 'pets', 'animal', 'animals', 'petstagram', 'petsagram', 'dogsitting', 'photooftheday', 'dogsofinstagram', 'ilovemydog', 'instagramdogs', 'dogstagram', 'dogoftheday', 'lovedogs', 'lovepuppies', 'hound', 'adorable', 'doglover', 'instapuppy', 'instado', 'cat', 'cats', 'socialsteeze', 'catsagram', 'catstagram', 'instagood', 'kitten', 'kitty', 'kittens', 'pet', 'pets', 'animal', 'animals', 'petstagram', 'petsagram', 'photooftheday', 'catsofinstagram', 'ilovemycat', 'instagramcats', 'nature', 'catoftheday', 'lovecats', 'furry', 'sleeping', 'lovekittens', 'adorable', 'catlover', 'instaca', 'fish', 'aquarium', 'fishtank', 'socialsteeze', 'fishporn', 'instafish', 'instagood', 'swim', 'swimming', 'water', 'coral', 'reef', 'reeftank', 'tropical', 'tropicalfish', 'aquaria', 'photooftheday', 'saltwater', 'freshwater', 'beautiful', 'ocean', 'watertank']


while len(hashtags)!=0:
    try:
        # Choose a random tag from the list of tags
        tag = random.choice(hashtags)
        ig.like_photo(tag)
        hashtags.remove(tag)
    except Exception:
        ig.closeBrowser()
        time.sleep(60)
        ig = InstagramBot(username, password)
        ig.login()
