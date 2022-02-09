from appium.webdriver.common.appiumby import AppiumBy
from BasePage import BasePage


class AddBudgetPage(BasePage):
    budget_type_locator = (AppiumBy.ID, 'protect.budgetwatch:id/budgetName')
    budget_value_locator = (AppiumBy.ID, 'protect.budgetwatch:id/value')
    save_button_locator = (AppiumBy.ID, 'protect.budgetwatch:id/saveButton')
    msg_error_locator = (AppiumBy.ID, 'protect.budgetwatch:id/snackbar_text')
    edit_icon_locator = (AppiumBy.ACCESSIBILITY_ID, 'Edit')
    delete_icon_locator = (AppiumBy.ACCESSIBILITY_ID, 'Delete')
    confirm_locator = (AppiumBy.ID, 'android:id/button1')
    cancel_button_locator = (AppiumBy.ID, 'protect.budgetwatch:id/cancelButton')
    cancel_locator = (AppiumBy.ID, 'android:id/button2')

    def type_budget_type(self, text):
        budget_type = self.driver.find_element(*AddBudgetPage.budget_type_locator)
        budget_type.send_keys(text)

    def type_budget_value(self, text):
        budget_value = self.driver.find_element(*AddBudgetPage.budget_value_locator)
        budget_value.send_keys(text)

    def click_save_button(self):
        save_button = self.driver.find_element(*AddBudgetPage.save_button_locator)
        save_button.click()

    def get_error(self):
        msg_error = self.driver.find_element(*AddBudgetPage.msg_error_locator)
        return msg_error.text

    def is_budget_type_enabled(self):
        budget_type = self.driver.find_element(*AddBudgetPage.budget_type_locator)
        return budget_type.is_enabled()

    def click_edit_icon(self):
        edit_icon = self.driver.find_element(*AddBudgetPage.edit_icon_locator)
        edit_icon.click()

    def click_delete_icon(self):
        delete_icon = self.driver.find_element(*AddBudgetPage.delete_icon_locator)
        delete_icon.click()
        confirm_button = self.driver.find_element(*AddBudgetPage.confirm_locator)
        confirm_button.click()