

# def get_tickers(name):
#     if ("(" in name) and (")" in name):
#         tickers = name[name.find("(")+1:name.find(")")]
#         return list(tickers.split(" "))
#     else:
#         return ['NO_TICKER']
#
#
# lst = ["a","b","c","a"]
# full_str = ','.join([str(elem) for elem in set(lst)])
# print(full_str)

def extract_data(data):
    with open('final_data.txt', 'w+') as f:
        for item in data:
            full_str = '>>'.join([str(elem) for elem in item])
            f.write(full_str + "\n")


def load_data():
    arr = []
    with open('data.txt', 'r') as f:
        for line in f:
            item = line.split('>>')
            if len(item) >= 5:
                item[4] = item[4].replace('\n', '')
                arr.append(item)
    return arr


data = load_data()
for item in data:
    item.append('')

extract_data(data)




