import unittest
from selenium import webdriver
from time import  sleep




class MojPrzypadek(unittest.TestCase):

# Instrukcje, które zostaną automatycznie wykonane przed każdym testem
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('https://www.sukienkimm.pl/sukienki/midi/strona-2/')

    def testNiePoprawneHaslo(self):
        driver = self.driver
        al = driver.find_element_by_id('onesignal-popover-cancel-button')
        al.click()
        zaloguj_btn = driver.find_element_by_xpath('//span[text()=" zaloguj się"]')
        zaloguj_btn.click()
        print("test wlasciwy")
        sleep(2)

    def tearDown(self) -> None:
        print("sprzatanie po tescie")
        self.driver.quit()





if __name__=='__main__':
    unittest.main()