import requests

from conf import proxies


class Scraper:
    def __init__(self, url=''):
        self.url = url
        self.web_content = ''

    def scrape(self):
        res = requests.get(self.url, proxies=proxies)
        if res.status_code == requests.codes.ok:
            self.web_content = res.text
