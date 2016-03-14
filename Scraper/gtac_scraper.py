import sys

from bs4 import BeautifulSoup

from scraper.scraper import Scraper
from util import persist_to_file


class GTACScraper(Scraper):
    def __init__(self):
        self.years = ['2013', '2014', '2015']
        self._url = 'https://developers.google.com/google-test-automation-conference/{}/presentations'
        super().__init__()

    @persist_to_file('gtac', extra_param='year')
    def get_data(self, year=''):
        if year not in self.years:
            sys.exit('[ERROR]: Only GTAC {} is available for scraping'.format(','.join(self.years)))
        self.url = self._url.format(year)
        self.scrape()
        titles, abstracts = zip(*self.parse())
        return {'titles': titles, 'abstracts': abstracts}

    def parse(self):
        soup = BeautifulSoup(self.web_content, 'lxml')
        sections = soup.find('div', 'devsite-article-body').findAll('section')
        for section in sections:

            # Get title content
            title_node = section.find('h2')
            title_text = title_node.text.strip() if hasattr(title_node, 'text') else ''

            # Get abstract content
            abstract_text = ''
            for abstract_node in section.findAll('p'):
                if len(abstract_node) == 1 and hasattr(abstract_node, 'text'):
                    abstract_text = abstract_node.text.strip()

            yield title_text, abstract_text
