import unittest
from selenium import webdriver

class MojPrzypadek(unittest.TestCase):

# Instrukcje, które zostaną automatycznie wykonane przed każdym testem
    def setUp(self):
        self.driver = webdriver.Firefox()


    def testSelenium(self):
        print("test wlasciwy")
    def tearDown(self) -> None:
        print("sprzatanie po tescie")

if __name__=='__main__':
    unittest.main()