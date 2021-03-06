import pathlib

from selenium                          import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by      import By
from selenium.webdriver.support.ui     import WebDriverWait
from selenium.webdriver.support        import expected_conditions as EC
from selenium.common.exceptions        import TimeoutException


class DriverUtils:
    def driver_wait(self, time = 2):
        wait = WebDriverWait(self.driver, time)

        return wait


    def wait_until_clickable_by_xpath(self, xpath):
        try:
            return True if self.driver_wait().until(
                EC.EC.element_to_be_clickable(By.XPATH, xpath)
            ) else False
        
        except TimeoutError:
            return False

    
    def wait_until_clickable_by_selector(self, selector):
        try:
            return True if self.driver_wait().until(
                EC.element_to_be_clickable(By.CSS_SELECTOR, selector)
            ) else False

        except TimeoutException:
            return False

    
    def get_element_by_xapth(self, xpath):
        if self.__until_clickable_by_xpath(xpath):
            element = self.find_element_by_xpath(xpath)        
            return element
        
        else:
            return None


    def get_element_by_css_selector(self, selector):
        if self.__until_clickable_by_selector(selector):
            element = self.find_element_by_css_selector(selector)
            return element

        else:
            return None


class WebDriver(webdriver.Chrome, DriverUtils):
    def __init__(self, file: str = 'chromedriver'):
        path = pathlib.Path(file).absolute()
        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--single-process')
        options.add_argument('--disable-dev-shm-sage')

        webdriver.Chrome.__init__(
            self,
            executable_path = path,
            options         = options
        )



if __name__ == "__main__":
    login_url = "https://wis.hufs.ac.kr/src08/jsp/index.jsp"

    
    driver = WebDriver()
    driver.get(login_url)

    driver.get_element_by_xapth()

    user_id = driver.get_element_by_xpath('/html/body/div[1]/form[3]/div[2]/div/div[2]/div/input[1]')
    user_pw = driver.get_element_by_xpath('//*[@id="password"]')

    user_id.send_keys("201602719")
    user_pw.send_keys("GK2ahdzl2!")
    