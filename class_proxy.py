class Proxy:

    def __init__(self, name, ticker, filed_date, reporting_date, link, kw):
        self.name = name
        self.filed_date = filed_date
        self.ticker = ticker
        self.reporting_date = reporting_date
        self.link = link
        if kw == "":
            self.key_words = []
        else:
            self.key_words = kw.split(", ")[:]

    def __eq__(self, other):
        if self.link == other.link:
            return True
        return False

    def get_data(self):
        data = self.name + ">>" + self.ticker + ">>" + self.filed_date + ">>" + self.reporting_date + ">>" + self.link
        return data

    def out_data(self):
        key_word = ', '.join([str(elem) for elem in set(self.key_words)])
        data = self.name + ">>" + self.ticker + ">>" + self.filed_date + ">>" + self.reporting_date + ">>" + self.link \
               + ">>" + key_word
        return data

    def add_key_word(self, key):
        if key == 'www.virtualshareholdermeeting.com':
            self.key_words.append('Broadridge')
        elif key == 'virtual%2520meeting':
            self.key_words.append('Virtual_meeting')
        else:
            self.key_words.append(key)
