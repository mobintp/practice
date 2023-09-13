import os
import pathlib
import unittest

from selenium import webdriver


import os

def file_uri(filename):
    current_dir = os.path.dirname(__file__)  # Get the directory of the current script
    absolute_path = os.path.abspath(os.path.join(current_dir, "html", filename))
    return pathlib.Path(absolute_path).as_uri()



driver = webdriver.Chrome()


class WebpageTests(unittest.TestCase):

    def setUp(self):
        driver.get(file_uri("counter.html"))

    def tearDown(self):
        driver.quit()

    def test_title(self):
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        increase = driver.find_element_by_id("increase")
        increase.click()
        expected_value = 1
        self.assertEqual(driver.find_element_by_tag_name("h1").text, str(expected_value))

    def test_decrease(self):
        decrease = driver.find_element_by_id("decrease")
        decrease.click()
        expected_value = -1
        self.assertEqual(driver.find_element_by_tag_name("h1").text, str(expected_value))

    def test_multiple_increase(self):
        increase = driver.find_element_by_id("increase")
        expected_value = 0
        for i in range(3):
            increase.click()
            expected_value += 1
        self.assertEqual(driver.find_element_by_tag_name("h1").text, str(expected_value))


if __name__ == "__main__":
    unittest.main()
