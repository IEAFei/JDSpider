from selenium import webdriver
import time


browser = webdriver.Firefox()
browser.get('https://www.zhihu.com/explore')
time.sleep(2)
browser.execute_script('window.open()')
browser.switch_to.window(browser.window_handles[1])
# button = browser.find_element_by_class_name('zu-top-add-question')
# print(button.text, button.id, button.location, button.tag_name, button.size)
browser.get('https://www.baidu.com')
time.sleep(2)
browser.execute_script('window.open()')
browser.switch_to.window(browser.window_handles[2])
browser.get('http://www.4399.com/')
time.sleep(2)
browser.quit()
