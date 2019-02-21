from selenium import webdriver
import time
from urllib.parse import urlencode
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pyquery import PyQuery as pq
from openpyxl import load_workbook


params = {
    'keyword': '电脑背包',
    'enc': 'utf-8'
}
url = 'https://search.jd.com/Search?' + urlencode(params)
browser = webdriver.Firefox()
wait = WebDriverWait(browser, 10)
wb = load_workbook('京东.xlsx')
sheet = wb.active
sheet.append(['name', 'price', 'comments', 'shop'])


def index_page(page):
    print('正在爬取', page, '页')
    try:
        time.sleep(2)
        browser.get(url)
        js = "var q=document.documentElement.scrollTop=100000"
        browser.execute_script(js)
        time.sleep(2)
        if page > 1:
            input = wait.until(
                 ec.presence_of_element_located((By.CSS_SELECTOR, '.p-skip input')))
            button = wait.until(
                 ec.presence_of_element_located((By.CSS_SELECTOR, '.p-skip .btn.btn-default')))
            input.clear()
            time.sleep(2)
            input.send_keys(page)
            time.sleep(2)
            button.click()
        wait.until(
            ec.text_to_be_present_in_element((By.CSS_SELECTOR, '.p-num a.curr'), str(page)))
        wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '.gl-warp .gl-item')))
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc('#J_goodsList .gl-item').items()
    for item in items:
        product = {
            'A': item.find('.p-name em').text().replace('\n', ' '),
            'B': item.find('.p-price strong').text(),
            'C': item.find('.p-commit a').text(),
            'D': item.find('.p-shop').text()
        }
        print(product)
        sheet.append(product)


def main():
    for i in range(1, 10):
        index_page(i)
    browser.close()
    wb.save('京东.xlsx')


if __name__ == '__main__':
    main()




