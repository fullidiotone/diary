#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.set_window_size(1200, 800)
browser.get('http://www.sm-stomatology.ru.verkeev.techart.intranet/')

element_menu = browser.find_element_by_xpath("(//a[@class='nav-link dropdown-toggle'])[2]");
print(element_menu.text)

hover = ActionChains(browser).move_to_element(element_menu);
hover.perform()

browser.quit()
