PATH = 'chromedriver.exe'

LINK = ['https://www.sec.gov/edgar/search/#/dateRange=custom&category=cu'
        'stom&startdt=', '&enddt=',  '&forms=DEF%252014A&page=']

KEY_WORDS_LINK = ['https://www.sec.gov/edgar/search/#/q=%2522', '%2522&dateRange=custom&category=custom&startdt'
                                                                '=2020-01-01&enddt=2020-12-31&forms=DEF%252014A&page=1']

# KEY_WORDS = ["webcasts", "lumiagm", "on24", "www.virtualshareholdermeeting.com", "Computershare",
#              "cstProxy", "viewProxy", "Kaltura", "armour", "zoom", "voteproxy", "issuerdirect", "company%2520website",
#              "proxypush", "proxydocs", "webex", "virtual", "virtually", "virtual%2520meeting"]

KEY_WORDS = ["virtual"]

XP_RESULTS = '/html/body/div[3]/div[2]/div[2]/div[1]/h5'

XP_BUTTON = ('/html/body/div[3]/div[2]/div[2]/table/tbody/tr[' + '%d' + ']/td[1]/a')
XP_XBUTTON = '/html/body/div[4]/div/div/div[3]/button'
XP_F_DATE = ('//*[@id="hits"]/table/tbody/tr[' + '%d' + ']/td[2]')
XP_R_DATE = ('//*[@id="hits"]/table/tbody/tr[' + '%d' + ']/td[3]')
XP_NAME = ('/html/body/div[3]/div[2]/div[2]/table/tbody/tr[' + '%d' + ']/td[4]')
XP_LINK = '/html/body/div[4]/div/div/div[3]/a[1]'

