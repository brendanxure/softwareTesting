import unittest
from time import sleep

from selenium import webdriver

# Import the Action Chains package.
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

class DragDropDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(executable_path="chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        sleep(2)

    # Go to https://jqueryui.com/draggable/ and drop the draggable object to some x, y coordinates
    def test01_drag(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get('https://jqueryui.com/draggable/')

        # switch to frame
        driver.switch_to.frame(0)

        # Find the element
        source1 = driver.find_element(By.ID, "draggable")


        # Create an ActionChains Object
        action = ActionChains(driver)

        # Perform the drag and drop by offset
        action.drag_and_drop_by_offset(source1, 100, 100).perform()
        sleep(5)

    # Go to https://jqueryui.com/droppable/ and drag the object and drop it in a box and assert
    # whether it has been dropped or not
    def test02_drag_drop(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get('https://jqueryui.com/droppable/')

        # switch to frame
        driver.switch_to.frame(0)

        # Find the elements - source box and target box
        source1 = driver.find_element(By.ID, "draggable")
        target1 = driver.find_element(By.ID, "droppable")

        # Create an ActionChains Object
        action2 = ActionChains(driver)
        # Perform the drag  and drop
        action2.drag_and_drop(source1, target1).perform()

        # Assert whether the target has received the item
        self.assertEqual("Drag me to my target", target1.text)
        sleep(2)

    # Go to https://jqueryui.com/draggable/ and by using click_and_hold(element),
    # pause(sec), move_by_offset(xOffset, yOffset), release() commands perform drag and drop
    def test03_click_hold_move_offset_drag_drop(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get('https://jqueryui.com/draggable/')

        # switch to frame 0
        driver.switch_to.frame(0)

        # Find the element
        source1 = driver.find_element(By.ID, "draggable")

        # Create an ActionChains object
        action = ActionChains(driver)

        # Use move_by_offset, pause, release commands to perform drag and drop
        action.click_and_hold(source1).move_by_offset(150, 100).pause(5).move_by_offset(-10, -10).release().perform()

        # Printing the successful results
        print("Dragging and dropping test case successful\n")

    # Go to https://jqueryui.com/draggable/ and by using click_and_hold(element), move_to_element(target),
    # pause(sec), move_by_offset(xOffset, yOffset), release() commands perform drag and drop
    def test04_click_hold_move_offset_drag_drop(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get('https://jqueryui.com/droppable/')

        # switch to frame 0
        driver.switch_to.frame(0)

        # Find the elements
        source1 = driver.find_element(By.ID, "draggable")
        target1 = driver.find_element(By.ID, "droppable")

        # Create an ActionChains object
        actions2 = ActionChains(driver)

        # Use move_to_element, pause, move_by_offset, release commands to perform drag and drop
        actions2.click_and_hold(source1).move_to_element(target1).pause(5).move_by_offset(20, 20).release().perform()

        # Printing the success of the case
        print("dragging and dropping test case successful\n")

        # Asserting the item has been dropped at target
        self.assertEqual("Dropped", target1.text)
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
