
import os
import time
import pathlib



from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from .keys import *



class YoutubeController:
    '''
                                            
        A class that implements Selenium driver and setup
            YouTube on it.                                    
                                                            '''
    def __init__(self,url,testing:bool=False) -> None:
        self.__url = url
        self.__driver = self.__setup(testing)
        self.__load_page()
        self.__driver.set_window_position(0,0)
        self.__driver.maximize_window()

    def __setup(self,testing):
        
        if testing:
            options = webdriver.ChromeOptions()
            options.add_argument('load-extension=' + str(pathlib.Path().resolve()).replace('\\','\\\\')+EXTENSION)
            options.add_argument('--ignore-ssl-errors=yes')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Remote(options=options)
        else : 
            chrome_options =    Options()
            chrome_options.add_argument('load-extension=' + str(os.getcwd())+EXTENSION)
            driver =    webdriver.Chrome(str(os.getcwd())+DRIVER,chrome_options=chrome_options)
            driver.create_options()
        driver.maximize_window()
        driver.set_window_position(-10000,0)
        return driver
    
    def __load_page(self):

        time.sleep(3)
        if len(self.__driver.window_handles) == 2 :
            self.__driver.switch_to.window(self.__driver.window_handles[1])
            self.__driver.close()
        
        self.__driver.switch_to.window(self.__driver.window_handles[0])
        self.__driver.get(self.__url)
        time.sleep(.1)
        
    def get_driver(self):
        self.__driver.find_element_by_id
        return self.__driver
    
    def test(self):
        
        while True:
            x = input("bla bla")
            if x :
                print(self.__driver.current_url.split('/')[3][0])
