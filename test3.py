from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Firefox()
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_id('draggable')
target = browser.find_element_by_id('droppable')
action = ActionChains(browser)
action.drag_and_drop(source, target)
action.perform()
a = browser.switch_to.alert
print(a.text)
