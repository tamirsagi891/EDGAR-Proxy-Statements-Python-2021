from selenium import webdriver
from constants import *
from class_proxy import *
import time


def extract_data(data):
    with open('data.txt', 'a') as f:
        for item in data:
            f.write(item.get_data() + "\n")


def get_tickers(name):
    new_name = name[:name.find("(")]
    if ("(" in name) and (")" in name):
        tickers = name[name.find("(")+1:name.find(")")]
        return new_name, list(tickers.split(","))
    else:
        return new_name, ['NO_TICKER']


def get_link():
    dates = get_dates()
    link = LINK[0] + str(dates[0]) + LINK[1] + str(dates[1]) + LINK[2]
    return link


def amount_of_results(driver, link):
    driver.get(link)
    time.sleep(1.5)
    results = driver.find_element_by_xpath(XP_RESULTS)
    s = results.text
    return list(s.split(" "))[0].replace(',', '')


def get_page_data(driver, link, lst, amount=100, get_ticker=True):
    driver.get(link)
    time.sleep(1.5)
    for i in range(1, amount + 1):
        print("Link num:", str(i))
        name = driver.find_element_by_xpath(XP_NAME % i).text
        f_date = driver.find_element_by_xpath(XP_F_DATE % i).text
        r_date = driver.find_element_by_xpath(XP_R_DATE % i).text
        link, file_type = get_htm_link(driver, i)
        new_name, tickers = get_tickers(name)
        if get_ticker is False:
            tickers = ['NO_TICKER']
        for ticker in tickers[:2]:
            lst.append(Proxy(new_name, ticker, f_date, r_date, link, ""))


def get_htm_link(driver, index):
    file_type = '8-K'
    button = driver.find_element_by_xpath(XP_BUTTON % index)
    if "K/A" in button.text:
        file_type = '8-K/A'
    button.click()
    link = driver.find_element_by_xpath(XP_LINK).get_attribute("href")
    driver.find_element_by_xpath(XP_XBUTTON).click()
    return link, file_type


def get_dates():
    date1 = "2020-01-01"
    date2 = "2020-12-31"
    return date1, date2


def main():
    data = []
    link = get_link() + '1'
    driver = webdriver.Chrome(PATH)
    results = int(amount_of_results(driver, link))
    num_of_pages = (results // 100) + 1
    last_entry = results % 100
    for i in range(1, num_of_pages + 1):
        page_link = link[:-1] + str(i)
        if i == num_of_pages:
            if last_entry != 0:
                get_page_data(driver, page_link, data, last_entry)
        else:
            get_page_data(driver, page_link, data)
    for item in data:
        print(item.get_data())
    extract_data(data)


if __name__ == '__main__':
    main()
