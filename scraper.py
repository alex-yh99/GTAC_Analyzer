import requests
from bs4 import BeautifulSoup

from conf import proxies

urls = [
    'https://developers.google.com/google-test-automation-conference/2015/presentations',
    'https://developers.google.com/google-test-automation-conference/2014/presentations',
    'https://developers.google.com/google-test-automation-conference/2013/presentations',
]


def scrape_gtac():
    titles, abstracts = None, None
    for url in urls:
        res = requests.get(url, proxies=proxies)
        titles, abstracts = zip(*parse_gtac_content(res.text))
    return titles, abstracts


def parse_gtac_content(web_content):
    soup = BeautifulSoup(web_content, 'lxml')
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
