import unittest, time, os
from appium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = '192.168.73.103:5555'
        desired_caps['appPackage'] = 'atpwta.live'
        desired_caps['appActivity'] = '.activity.Main'
        desired_caps['appWaitActivity'] = '.activity.root.TournamentList'
        desired_caps['autoGrantPermissions'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_app_atp_wta(self):
        self.driver.implicitly_wait(30)
        time.sleep(5)

        cancel = self.driver.find_element_by_id('android:id/button2')
        cancel.click()
        time.sleep(5)


        # Clicar em Navigation Bar MainMenu para encontrar elemento pelo xpath
        menubar = self.driver.find_element_by_id('atpwta.live:id/NavBarMainMenuSpinner')
        click = menubar.click()

        # Da lista de opções clicque em Rankings encontre o elemento pelo uiautomator
        rankings = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Rankings")')
        rankings.click()

        singles = self.driver.find_element_by_id('atpwta.live:id/RankingsListItem')
        singles.click()

        # Assert que o nome de jogador aparece na lista
        elmnt = self.driver.find_element_by_id('atpwta.live:id/Player1TV')
        self.assertEqual('Novak Djokovic', elmnt.get_attribute('text'))

        print(elmnt.get_attribute('text'))
        elmnt = self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=0]")
        elmnt.cli
        elmnt.click()

        table = self.driver.find_element_by_android_uiautomator(
            "new UiSelector().className(android.widget.TableLayout)")
        rows = table.find_elements_by_class_name('android.widget.TableRow')
        for i in range(0, len(rows)):
            cols = rows[i].find_elements_by_class_name('android.widget.TextView')
            for j in range(0, len(cols)):
                print(cols[j].get_attribute('text') + " -- "),
            print("")

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
