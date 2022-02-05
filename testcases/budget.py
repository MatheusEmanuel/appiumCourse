import unittest, time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

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
        time.sleep(5)
        action = TouchAction(self.driver)
        item = self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[contains(@text, 'supermarket')]")
        action.long_press(item)
        action.perform()
        time.sleep(5)
        editmenu = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Edit')]")
        editmenu.click()
        time.sleep(5)
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

    def test_app_budget_add_transaction(self):
        self.test_app_budget_add()
        self.driver.back()
        time.sleep(5)
        transactions = self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[contains(@text, 'Transactions')]")
        transactions.click()
        time.sleep(5)
        add_transactions = self.driver.find_element_by_id('protect.budgetwatch:id/action_add')
        add_transactions.click()
        time.sleep(5)
        add_name = self.driver.find_element_by_id('protect.budgetwatch:id/name')
        add_name.send_keys('Tony Hawks')
        time.sleep(5)
        add_account = self.driver.find_element_by_id('protect.budgetwatch:id/account')
        add_account.send_keys('noo')
        time.sleep(5)
        add_value = self.driver.find_element_by_id('protect.budgetwatch:id/value')
        add_value.send_keys('123')
        time.sleep(5)
        add_note = self.driver.find_element_by_id('protect.budgetwatch:id/note')
        add_note.send_keys('aaaa')
        time.sleep(5)
        TouchAction(self.driver).press(x=620, y=500).move_to(x=621, y=371).release().perform()
        time.sleep(5)
        TouchAction(self.driver).press(x=620, y=500).move_to(x=621, y=371).release().perform()
        time.sleep(5)
        capture = self.driver.find_element_by_id('protect.budgetwatch:id/captureButton')
        capture.click()
        time.sleep(5)
        allow_perm = self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button')
        allow_perm.click()
        time.sleep(5)
        # allow_cam = self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_always_button')
        # allow_cam.click()
        # time.sleep(5)
        # allow_loc = self.driver.find_element_by_id('com.android.camera2:id/confirm_button')
        # allow_loc.click()
        # time.sleep(5)
        capture_Cam = self.driver.find_element_by_id('com.android.camera2:id/shutter_button')
        capture_Cam.click()
        time.sleep(5)
        # select_capture = self.driver.find_element_by_accessibility_id("Done")
        select_capture = self.driver.find_element(AppiumBy.XPATH,'//android.widget.ImageButton[@content-desc="Done"]')
        select_capture.click()
        time.sleep(5)
        # save = self.driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="SAVE"]')
        TouchAction(self.driver).press(x=620, y=500).move_to(x=621, y=371).release().perform()
        time.sleep(5)
        TouchAction(self.driver).press(x=620, y=500).move_to(x=621, y=371).release().perform()
        time.sleep(5)
        save = self.driver.find_element_by_id('protect.budgetwatch:id/saveButton')
        save.click()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
