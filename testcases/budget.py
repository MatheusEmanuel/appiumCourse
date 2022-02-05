import unittest, time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


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

    def test_app_budget_edit(self):
        self.test_app_budget_add()
        action = TouchAction(self.driver)

        item = self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[contains(@text, 'supermarket')]")
        action.long_press(item)
        action.perform()

        editmenu = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Edit')]")
        editmenu.click()

        edit = self.driver.find_element(AppiumBy.ID, 'protect.budgetwatch:id/action_edit')
        edit.click()

        self.driver.implicitly_wait(30)
        time.sleep(5)
        value_budget = self.driver.find_element(AppiumBy.ID, "protect.budgetwatch:id/value")
        value_budget.clear()
        value_budget.send_keys("400")
        time.sleep(5)
        salve_button = self.driver.find_element(AppiumBy.ID, "protect.budgetwatch:id/saveButton")
        salve_button.click()


if __name__ == '__main__':
    unittest.main()
