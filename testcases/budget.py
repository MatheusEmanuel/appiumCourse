import unittest, time
from appium import webdriver


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = '192.168.73.103:5555'
        desired_caps['appPackage'] = 'protect.budgetwatch'
        desired_caps['appActivity'] = '.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_app_budget_add(self):
        time.sleep(5)
        budget = self.driver.find_element_by_id('protect.budgetwatch:id/menu')
        budget.click()
        time.sleep(5)
        add_budget = self.driver.find_element_by_id('protect.budgetwatch:id/action_add')
        add_budget.click()
        time.sleep(5)
        type_budget = self.driver.find_element_by_id('protect.budgetwatch:id/budgetName')
        type_budget.send_keys('supermarket')
        time.sleep(5)
        value_budget = self.driver.find_element_by_id('protect.budgetwatch:id/value')
        value_budget.send_keys(600)
        time.sleep(5)
        save_budget = self.driver.find_element_by_id('protect.budgetwatch:id/saveButton')
        save_budget.click()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
