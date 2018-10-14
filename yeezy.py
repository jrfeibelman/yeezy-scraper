import json, re
from tweepy import Cursor, OAuthHandler, API
from pandas import DataFrame, read_csv
from selenium import webdriver
import numpy, requests
import bs4 as bs
from time import clock

class YeezusBot:

    # Load credentials from json file
    def __init__(self):
        with open("twitter_credentials.json", "r") as file:
            self.__creds = json.load(file)
        self.__auth = OAuthHandler(self.__creds['CONSUMER_KEY'], self.__creds['CONSUMER_SECRET'])
        self.__auth.set_access_token(self.__creds['ACCESS_TOKEN'], self.__creds['ACCESS_SECRET'])
        self.api = API(self.__auth)

    @staticmethod
    def get_url_from(st):
        if st.__contains__('https') == False:
            return ''
        else:
            return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', st)[0].split(' ')

    @staticmethod
    def clean_urls(link_arr):
        links = []
        for x in range(len(link_arr)):
            links.append(bot.parse_url(link_arr))
        return links

    @staticmethod
    def parse_url(url):
        index = url.find('\\')
        return url

    def get_statuses(self, user_name, item_number):
        dates = []
        txts = []
        urls = []
        for status in Cursor(method=self.api.user_timeline, screen_name=user_name).items(item_number):
            status_str = json.dumps(status._json)
            text = status_str.split('text')[1].split('truncated')[0][4:-4]
            # if r'Yeezy' in text: # or r'RESTOCKED' in text:
            if r'4D' in text:
                date = status_str.split('created_at')[1].split('id')[0][4:-15]
                dates.append(date)
                txts.append(text)
                if text.__contains__('https') == True:
                    urls.append(YeezusBot.get_url_from(text))
                else:
                    urls.append('')
        data = ({'TimeStamp':dates,'Text':txts,'URL':urls})
        return DataFrame(data, columns=['TimeStamp','Text','URL'])

    def print_links(self, df):
        count1 = 0
        test_links = []
        for url_list in df['URL']:
            print('URL_LIST %d ' % count1)
            count1 = count1 + 1
            count2 = 0
            for url in url_list:
                if re.search('^https:', url) == False:
                    print('FALSE')
                    continue
                print('URL %d' % count2)
                count2 = count2 + 1
                print(str(url))
                test_links.append(str(url))

    def create_new_backtests(self, path, frame):
        frame.to_csv(path)

    def get_backtests(self, path):
        return read_csv(path)


class YeezusBrowser:

    def __init__(self, url):
        self.url = url
        # self.request = requests.get(url, stream=True)
        self.driver = webdriver.Chrome(executable_path='/Users/jfeibs/Desktop/YeezyBot/ENV/bin/chromedriver')
        self.driver.get(self.url)
        self.base_page = self.driver.page_source
        s = bs.BeautifulSoup(url)
        print(s.)
        print(self.driver.page_source)
        self.run()

    def run(self):
        print('running')
        print(self.base_page)
        delta_time = 1 # updates every 1 second
        start = clock()
        while True:
            now = clock()
            print(now)
            if now - start >= delta_time:
                print(self.driver.page_source)
                start = clock()

    def add_to_cart(self, url):
        self.driver.get(url)



# SCRIPT

bot = YeezusBot()
df = bot.get_statuses(user_name='adidasalerts', item_number=100)
back_tests = bot.get_backtests('backtests.csv')
# bot.print_links(df)

links = back_tests['URL'][45].split('https:')
test_links = []
for x in range(len(links)):
    if links[x].startswith('/') == True:
        start = 'https:' + links[x]
        index = start.find('\\')
        test_links.append(start[:index])
print(test_links)


# print(df['URL'][14])
# print(df['URL'][31])
l = 'https://www.adidas.com/us/nmd_r1-stlt-primeknit-shoes/CQ2391.html?pr=oos_rr&slot=1'
browser = YeezusBrowser(l)   # test_links[0])
# browser.run()
#
# print('x')

# ans = str
# for line in driver.page_source:
# 		if '\xe0' in line or '\u010c' in line or '\u0161' in line:
# 			line = " "
# 		ans = "%s%s" % (ans,line)

# dimesLinesFile = open('twitter.txt','w')
# dimesLinesFile.write(ans)
# dimesLinesFile.close()







# Enter your keys/secrets as strings in the following fields
# credentials = {}
# credentials['CONSUMER_KEY'] =
# credentials['CONSUMER_SECRET'] =
# credentials['ACCESS_TOKEN'] =
# credentials['ACCESS_SECRET'] =
#
# # Save the credentials object to file
# with open("twitter_credentials.json", "w") as file:
#     json.dump(credentials, file)





# from kitchen.text.converters import getwriter
# import sys
# from selenium import webdriver
# import time
#
# # driver = webdriver.Firefox()
# # driver.get("https://twitter.com/adidasalerts?lang=en")
#
# # ans = str
# # for line in driver.page_source:
# # 		if '\xe0' in line or '\u010c' in line or '\u0161' in line:
# # 			line = " "
# # 		ans = "%s%s" % (ans,line)
#
# # dimesLinesFile = open('twitter.txt','w')
# # dimesLinesFile.write(ans)
# # dimesLinesFile.close()
#
# import twitter
# api = twitter.Api()
# a = api.GetUser("adidasalerts")
# print([s.text for s in a])

