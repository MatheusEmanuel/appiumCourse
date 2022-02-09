import unittest
from datetime import date

from MainPage import MainPage
from BudgetPage import BudgetPage
from AddBudgetPage import AddBudgetPage
from appium import webdriver
from Data import TestData
import time

#pytest -v pageobjects/BudgetTestCases.py --html=report.html
class MyTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'protect.budgetwatch'
        desired_caps['appActivity'] = '.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_create_new_budget(self):
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(20)
        time.sleep(5)
        add_page.type_budget_type(TestData.budget_type)
        add_page.type_budget_value(TestData.budget_value)
        add_page.click_save_button()
        budget_page = BudgetPage(self.driver)
        self.assertEqual(budget_page.get_first_budget(), TestData.budget_type)

    def test_new_budget_without_type(self):
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(20)
        time.sleep(5)
        add_page.type_budget_value(TestData.budget_value)
        add_page.click_save_button()
        self.assertEqual(add_page.get_error(), TestData.msg_budget_type_empty)

    def test_new_budget_without_value(self):
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(20)
        time.sleep(5)
        add_page.type_budget_type(TestData.budget_type)
        add_page.click_save_button()
        self.assertEqual(add_page.get_error(), TestData.msg_budget_value_empty)

    def test_edit_budget(self):
        self.test_create_new_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.long_click_first_budget()
        budget_page.click_edit()
        add_page = AddBudgetPage(self.driver)
        add_page.click_edit_icon()
        self.driver.implicitly_wait(20)
        time.sleep(3)
        add_page.type_budget_value(TestData.new_budget_value)
        add_page.click_save_button()
        self.assertIn(TestData.new_budget_value, budget_page.get_new_value())

    def test_check_edit_budget_type(self):
        self.test_create_new_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.long_click_first_budget()
        budget_page.click_edit()
        add_page = AddBudgetPage(self.driver)
        add_page.click_edit_icon()
        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.assertFalse(add_page.is_budget_type_enabled())

    def test_delete_budget(self):
        self.test_create_new_budget()

        budget_page = BudgetPage(self.driver)
        budget_page.long_click_first_budget()
        budget_page.click_edit()
        add_page = AddBudgetPage(self.driver)
        add_page.click_edit_icon()
        add_page.click_delete_icon()
        self.assertIn(TestData.budget_empty_list, budget_page.get_emptylist_msg())

    def test_set_calendar(self):
        today = date.today()
        d1 = today.strftime("%d")
        m1 = today.strftime("%m")
        y1 = today.strftime("%y")

        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.set_calendar()
        result = TestData.date_result + m1[1] + "/" + d1[1] + "/" + y1
        self.assertEqual(result, budget_page.get_text_date())


if __name__ == '__main__':
    unittest.main()


