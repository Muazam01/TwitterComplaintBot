import options as options
from selenium  import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

USERNAME="YOUR USERNAME"
PASSWORD="YOUR PASSWORD"


class TwitterBot():
    def __init__(self):
        self.service = Service("E:\chrome_driver\chromedriver")
        self.chromeoptions = Options()
        self.chromeoptions.headless = False
        time.sleep(8)
        self.driver = webdriver.Chrome(service=self.service,options=self.chromeoptions)

    def getinternetspeed(self):

        self.speedtest = self.driver.get("https://www.speedtest.net/")
        self.go = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        self.go.click()
        time.sleep(60)
        self.speeds = []
        self.speed = self.driver.find_elements(By.CLASS_NAME, "result-data-large")
        for i in self.speed:
            self.speeds.append(i.text)

        self.download_speed = self.speeds[0]
        self.upload_speed = self.speeds[1]

        #self.driver.quit()

    def tweet_at_provider(self):
        self.access_twitter = self.driver.get(
            "https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D")
        time.sleep(10)
        self.getlogin_details = self.driver.find_element(by=By.XPATH,
                                                         value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        self.getlogin_details.send_keys(USERNAME, Keys.ENTER)
        time.sleep(5)
        self.get_password = self.driver.find_element(by=By.XPATH,
                                                     value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input')
        self.get_password.send_keys(PASSWORD, Keys.ENTER)
        time.sleep(10)
        self.search = self.driver.find_element(By.CLASS_NAME, "r-30o5oe")
        self.search.send_keys("airtel India", Keys.ENTER)
        time.sleep(5)
        self.isp_link = self.driver.find_element(By.XPATH,
                                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[3]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a').click()
        # self.driver.execute_script()
        time.sleep(8)
        self.gettweetbutton = self.driver.find_element(By.XPATH,
                                                       '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        time.sleep(8)
        self.tweetbar = self.driver.find_element(By.XPATH,
                                                 '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div')
        self.tweetbar.send_keys(f"Hey Internet Provider\n My download speed is :{self.download_speed}mbps and"
                                f"upload speed is {self.upload_speed}mbps. My promised speed was {30}mbps")
        time.sleep(6)
        self.send = self.driver.find_element(By.XPATH,
                                             '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]').click()

        self.driver.quit()
