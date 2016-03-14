from bs4 import BeautifulSoup

from scraper.scraper import Scraper
from util import persist_to_file


class GoogleTestBlogScraper(Scraper):
    def __init__(self):
        super().__init__(url='http://googletesting.blogspot.com/')

    @persist_to_file('google_test_blog')
    def get_data(self):
        urls, posts = zip(*self.parse())
        return {'urls': urls, 'posts': posts}

    def parse(self):
        self.url = self.get_latest()
        while self.url is not '':
            yield self.url, self.get_post_content()
            self.url = self.get_prev_post_url()

    def get_latest(self):
        self.scrape()
        soup = BeautifulSoup(self.web_content, 'lxml')
        start_url = ''
        try:
            main_section = soup.find('div', id='main')
            header = main_section.findAll('h2', 'title')[0]
            start_url = header.find('a')['href']
        except:
            print('Unable to Get latest archive from: ' + self.url)
        return start_url

    def get_post_content(self):
        self.scrape()
        soup = BeautifulSoup(self.web_content, 'lxml')
        post_content = soup.find('div', 'post-content')
        # Remove '<script>' tag inside post-content
        for script in post_content.find('script'):
            script.extract()
        return post_content.get_text().strip()

    def get_prev_post_url(self):
        prev_url = ''
        try:
            soup = BeautifulSoup(self.web_content, 'lxml')
            prev_url = soup.find('a', 'blog-pager-older-link')['href']
        except:
            print('Oldest archive found: ' + self.url)
        return prev_url
