from appium.webdriver.common.appiumby import AppiumBy
from BasePage import BasePage
from appium.webdriver.common.touch_action import TouchAction


class BudgetPage(BasePage):
    add_locator = (AppiumBy.ACCESSIBILITY_ID, 'Add')
    first_budget_locator = (AppiumBy.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.TextView')
    new_value_locator = (AppiumBy.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView')
    edit_locator = (AppiumBy.ID, 'android:id/title')
    empty_list_locator = (AppiumBy.ID, 'protect.budgetwatch:id/helpText')

    def click_add(self):
        add_budget = self.driver.find_element(*BudgetPage.add_locator)
        add_budget.click()

    def get_first_budget(self):
        first_element = self.driver.find_element(*BudgetPage.first_budget_locator)
        return first_element.text

    def long_click_first_budget(self):
        first_element = self.driver.find_element(*BudgetPage.first_budget_locator)
        actions = TouchAction(self.driver)
        actions.long_press(first_element)
        actions.perform()

    def get_new_value(self):
        new_value = self.driver.find_element(*BudgetPage.new_value_locator)
        return new_value.text

    def click_edit(self):
        edit = self.driver.find_element(*BudgetPage.edit_locator)
        edit.click()

    def get_emptylist_msg(self):
        empty_list = self.driver.find_element(*BudgetPage.empty_list_locator)
        return empty_list.text
