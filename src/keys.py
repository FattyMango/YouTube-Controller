'''
    Static Keys and Paths that are used in the application.
                                                                '''

'''                                               Links                                                  '''

YOUTUBE     =   "https://www.youtube.com"

'''                                                                                                      '''

'''                                             FILEPATHS                                                '''

EXTENSION   =   r'C:\Users\malak\Desktop\Projects\Python\YoutubeController\driver\adblock\4.46.2_0'
DRIVER      =   "C:\\Users\\malak\\Desktop\\Projects\\Python\\YoutubeController\\driver\\chromedriver.exe"

'''                                                                                                      '''


'''                                              BUTTONS                                                 '''

TOGGLE_PLAY         =   "K"
TOGGLE_CAPTION      =   "C"
TOGGLE_FULLSCREEN   =   "F"
TOGGLE_MUTE         =   "M"
FORWARD             =   "L"
BACKWARD            =   "J"

'''                                                                                                      '''


'''                                              XPATHS                                                  '''

SEARCH              =   '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input'
SEARCH_RESULTS      =   "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]"
VIDEO_CHOICE        =   '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]'
VIDEOS_CONTAINER    =   '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]'
SETTINGS_CONTAINER  =   '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[29]'
'''                                                                                                      '''


'''                                             SELECTORS                                                '''

SETTINGS    =   'document.querySelector("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button.ytp-button.ytp-settings-button").click();'
QUALITY     =   'document.querySelector("#ytp-id-17 > div > div").lastElementChild.click();'
HIGHEST     =   'document.querySelector("#ytp-id-17 > div > div.ytp-panel-menu > div:nth-child(1)").click()'
LOWEST      =   'n = document.querySelector("#ytp-id-17 > div > div.ytp-panel-menu").childNodes.length - 1;selector = "#ytp-id-17 > div > div.ytp-panel-menu > div:nth-child("+n.toString()+")";document.querySelector(selector).click();'
AUTO        =   'document.querySelector("#ytp-id-17 > div > div.ytp-panel-menu").lastElementChild.click()'


'''                                                                                                      '''

'''                                                TAGS                                                  '''

PLAYER_CONTAINER    =   'player-container'
VIDEO_PLAYER        =   'ytd-video-renderer'

'''                                                                                                      '''

'''                                                ENUMS                                                 '''

SEARCH_STATE = 0
PLAYING_STATE = 1

'''                                                                                                      '''