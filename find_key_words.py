import time

from main import *


def extract_data(data):
    with open('final_data.txt', 'w+') as f:
        for item in data:
            f.write(item.out_data() + "\n")


def load_data():
    arr = []
    with open('data.txt', 'r') as f:
        for line in f:
            item = line.split('>>')
            if len(item) >= 5:
                item[4] = item[4].replace('\n', '')
                arr.append(item)
    return arr


def turn_data_to_proxy(data):
    arr = []
    for item in data:
        arr.append(Proxy(item[0], item[1], item[2], item[3], item[4], item[5].replace("\n","")))
    return arr


def get_new_link(key):
    return KEY_WORDS_LINK[0] + key + KEY_WORDS_LINK[1]


def get_proxy_by_keyword(driver, key):
    data = []
    link = get_new_link(key)
    results = int(amount_of_results(driver, link))
    num_of_pages = (results // 100) + 1
    last_entry = results % 100
    for i in range(1, num_of_pages+1):
        print("Page num:", str(i), end=" \\ ")
        page_link = link[:-1] + str(i)
        if i == num_of_pages:
            if last_entry != 0:
                get_page_data(driver, page_link, data, last_entry)
        else:
            get_page_data(driver, page_link, data)
    return data


def add_key_words(files, temp_files, key):
    for temp_item in temp_files:
        for file in files:
            if temp_item == file:
                file.add_key_word(key)


def main():
    data = load_data()
    files = turn_data_to_proxy(data)
    # for item in files:
    #     print(item.out_data())
    driver = webdriver.Chrome(PATH)
    for key in KEY_WORDS:
            try:
                temp_files = get_proxy_by_keyword(driver, key)
                add_key_words(files, temp_files, key)
                extract_data(files)
                print(key, " - worked")
            except:
                print(key, " - didnt work")
    for item in files:
        if item.key_words != []:
            print(item.out_data())



if __name__ == '__main__':
    main()