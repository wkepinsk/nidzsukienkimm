import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class MojPrzypadek(unittest.TestCase):

# Instrukcje, które zostaną automatycznie wykonane przed każdym testem
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('https://www.sukienkimm.pl/sukienki/midi/strona-2/')
    def testNiePoprawneHaslo(self):
        driver = self.driver
        zaloguj_btn = driver.find_element_by_xpath('//span[text()=" zaloguj się"]')
        zaloguj_btn.click()
        print("test wlasciwy")
    def tearDown(self) -> None:
        print("sprzatanie po tescie")
        self.driver.quit()

if __name__=='__main__':
    unittest.main()