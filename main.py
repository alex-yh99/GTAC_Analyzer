from analyzer import nltk_setup, analyze_test_info
from scraper.google_test_blog_scraper import GoogleTestBlogScraper
from scraper.gtac_scraper import GTACScraper

if __name__ == "__main__":
    nltk_setup(init=False)

    # GTAC
    gtac = GTACScraper()
    gtac_data = []
    for y in gtac.years:
        gtac_data.extend(gtac.get_data(year=y)['abstracts'])
    analyze_test_info(gtac_data, 'GTAC', 'gtac')

    # Google Test Blog
    gtbs = GoogleTestBlogScraper()
    analyze_test_info(gtbs.get_data()['posts'], 'Google Test Blog', 'google_test_blog')
