import re
import string

from bs4 import BeautifulSoup

from scraper.scraper import Scraper
from util import persist_to_file


class GlossaryScraper(Scraper):
    def __init__(self):
        super().__init__(url='http://www.aptest.com/glossary.html')

    @property
    @persist_to_file('glossary')
    def glossaries(self):
        self.scrape()
        return list(self.parse())

    def parse(self):
        soup = BeautifulSoup(self.web_content, 'lxml')
        paragraphs = soup.find('div', id='main').findAll('p')
        for p in paragraphs:
            keyword_node = p.find('b')
            if hasattr(keyword_node, 'text'):
                keyword_text = keyword_node.text.strip()

                # Remove punctuation and abbreviations
                # e.g. 'User Test (UT): ' => 'User Test'
                reg_obj = re.match(r'([\w\s-]+)[^{}]'.format(re.escape(string.punctuation)), keyword_text)
                if reg_obj:
                    yield reg_obj.group().strip()
