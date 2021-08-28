import time
from selenium import webdriver

channels='reidboyy','cloakzy','timthetatman','frozone'
channel='timthetatman'

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
header = {"authorization": "MzM2Mjc3OTM0NTcyNTY4NTc4.X3EwXw.OF4fUdtM0PZM5uImuAqd5JVYAy8"}

options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--disable-popup-blocking")
options.add_argument('--incognito')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-fullscreen")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument("--disable-web-security");
options.add_argument("--allow-running-insecure-content");

driver=webdriver.Chrome(options=options)
url=f"https://player.twitch.tv/?channel={channel}&muted=true&parent=twitch.tv&player=popout"
driver.get(url)
time.sleep(4)
# button=driver.find_element(by="data-a-target",value="player-overlay-mature-accept")
button=driver.find_element_by_class_name('"ScCoreButton-sc-1qn4ixc-0 ScCoreButtonPrimary-sc-1qn4ixc-1 euIPFy"')
button.send_keys('\n')

# for channel in channels:
#   driver=webdriver.Chrome(options=options)
#   url=f"https://player.twitch.tv/?channel={channel}&muted=true&parent=twitch.tv&player=popout"
#   driver.get(url)
#   time.sleep(5)
#   driver.save_screenshot(f'./dump/{channel}.png')
# x=0
# time.sleep(5)
# while x<50:
#   driver.save_screenshot(f'./dump/{channel}.png')
#   x+=1