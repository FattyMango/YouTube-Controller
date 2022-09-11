import time

from YouTubeController.status import Status
from .keys import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Utils:

    '''
        Utility Class acts as a lower layer for The Remote class,
            contains all the functionalities that operates 
                on Selenium driver.                         

                                                                '''



    def __init__(self,driver : webdriver) -> None:

        self.__driver = driver
        self.action = ActionChains(self.__driver)
    def set_driver(self,driver):
        self.__driver = driver
        self.action = ActionChains(self.__driver)

    def destroy_driver(self):
        self.__driver = None
    
    def go_to_url(self,url):
        try:
            self.__driver.get(url)
            return True
        except :
            return False
    def execute_action(self,action,shift = False):

        '''
            Function performs all the basic command using its 
                shortcut, such as (play (K), Mute (M)...etc)
                                                                '''
                                                               
        try:
            container = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, TAGS["VIDEO_PLAYER"]))
            )
            self.action.move_to_element(container).perform()
            if shift:
                self.action.send_keys(Keys.SHIFT+action)
            else :
                self.action.send_keys(action)

            self.action.perform()
            return True
        except Exception:
            print(Exception)
            return False
            
    def like_video(self):
        try:
            button = WebDriverWait(self.__driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, SELECTORS["LIKE_BUTTON"]))
            )
            
            button.click()
            return True
        except: return False

    def dislike_video(self):
        try:
            button = WebDriverWait(self.__driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, SELECTORS["DISLIKE_BUTTON"]))
            )
            
            button.click()
            return True
        except: return False
    def toggle_auto_play(self):
        try:
            self.__driver.execute_script(SCRIPTS["AUTO_PLAY"])
            return True
        except: return False
    def toggle_subscribe(self):
        try:
            WebDriverWait(self.__driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, SELECTORS["SUBSCRIBE"]))
            ).click()
            self.__driver.find_element_by_css_selector(SELECTORS["UNSUBSCRIBE"]).click()
            
            return True
        except: return False    
    

    
    def set_quality (self,quality):
        self.__driver.execute_script(SCRIPTS["SETTINGS"])
        try:
            # time.sleep(.2)
            # self.__driver.execute_script(SCRIPTS["QUALITY"])
            # time.sleep(.2)
            # self.__driver.execute_script(SCRIPTS[quality])
            # return True  

            # click settings
            # self.__driver.find_element_by_css_selector("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button.ytp-button.ytp-settings-button.ytp-hd-quality-badge").click()
            time.sleep(0.3)
            menu_selections = self.__driver.find_element_by_css_selector('#ytp-id-17 > div').find_elements_by_css_selector('#ytp-id-17 > div > div')
            time.sleep(0.1)
            menu_selections[len(menu_selections)].click()
            time.sleep(0.1)
            menu_selections = self.__driver.find_element_by_css_selector('#ytp-id-17 > div > div.ytp-panel-menu').find_elements_by_css_selector('#ytp-id-17 > div > div.ytp-panel-menu > div')
            if quality == "HIGHEST":
                menu_selections[0].click()
            elif quality == "LOWEST":
                menu_selections[len(menu_selections)-1].click()
            else:
                menu_selections[len(menu_selections)].click()
        except Exception:
            print('a7a1')
            try:
                time.sleep(.3)
                self.__driver.execute_script(SCRIPTS["QUALITY_SECOND"])
                time.sleep(.6)
                
                self.__driver.execute_script(SCRIPTS[quality+'_SECOND'])
                return True  
            except:
                print('a7a2')
                return False

        


    def search(self,q):
        try:
            search = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.XPATH, XPATHS["SEARCH"]))
            )
            time.sleep(.1)
            search.clear()
            time.sleep(.1)
            search.send_keys(str(q))
            time.sleep(.1)
            search.send_keys(Keys.RETURN)
            return True
        except Exception:
            print(Exception)
            return False
        
    def __click_search_result_video(self,index):
        try : 
            container = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.XPATH, XPATHS["SEARCH_RESULTS"]))
            )
            
            container.find_elements_by_tag_name(TAGS["SEARCH_VIDEO_PLAYER"])[index].find_element_by_css_selector('#video-title > yt-formatted-string').click()
            return True
        except Exception:
            return False
    
    def __click_recommended_video(self,index):
        try:
            container =  WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME,'ytd-watch-next-secondary-results-renderer'))
                )
            container.find_elements_by_tag_name('ytd-compact-video-renderer')[index].click()
            return True
        except Exception:
            return False

    def __click_home_video(self,index):
        try:
            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME,'ytd-rich-grid-row'))
                )
            containers = self.__driver.find_elements_by_tag_name('ytd-rich-grid-row')
            containers[0].find_elements_by_tag_name('ytd-rich-item-renderer')[index].click()
            return True
        except Exception:
            return False
    

    def select_video(self,state,index):
        try:
            {
                'HOME'  :  self.__click_home_video,
                'SEARCH':  self.__click_search_result_video,
                'WATCH' :  self.__click_recommended_video

             }[state](index)
            
        except Exception:
            
            return False
    

    

        