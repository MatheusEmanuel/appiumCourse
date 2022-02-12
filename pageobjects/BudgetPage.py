from appium.webdriver.common.appiumby import AppiumBy
from BasePage import BasePage
from appium.webdriver.common.touch_action import TouchAction


class BudgetPage(BasePage):
    # add_locator = (AppiumBy.ACCESSIBILITY_ID, 'Add')
    add_locator = (AppiumBy.ID, 'protect.budgetwatch:id/action_add')
    first_budget_locator = (AppiumBy.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.TextView')
    new_value_locator = (AppiumBy.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView')
    edit_locator = (AppiumBy.ID, 'android:id/title')
    empty_list_locator = (AppiumBy.ID, 'protect.budgetwatch:id/helpText')
    calendar_locator = (AppiumBy.ID, "protect.budgetwatch:id/action_calendar")
    day_locator = (AppiumBy.ACCESSIBILITY_ID, "02 February 2022")
    setdate_locator = (AppiumBy.ID, "android:id/button1")
    text_date_locator = (AppiumBy.ID, "protect.budgetwatch:id/dateRange")

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

    def set_calendar(self):
        cal = self.driver.find_element(*BudgetPage.calendar_locator)
        cal.click()
        self.driver.implicitly_wait(30)
        set_day = self.driver.find_element(*BudgetPage.day_locator)
        set_day.click()
        self.driver.implicitly_wait(20)
        setcal = self.driver.find_element(*BudgetPage.setdate_locator)
        setcal.click()

    def get_text_date(self):
        text_date = self.driver.find_element(*BudgetPage.text_date_locator)
        self.driver.implicitly_wait(30)
        return text_date.text
