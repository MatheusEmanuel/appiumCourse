from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from BasePage import BasePage

class MainPage(BasePage):

    # budget_option_locator = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]')
    budget_option_locator = (AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc=\"icon\"])[1]')

    def click_budget(self):
        budget_option = self.driver.find_element(*MainPage.budget_option_locator)
        budget_option.click()

