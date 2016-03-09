from analyzer import analyze_pres, nltk_setup
from scraper import scrape_gtac

if __name__ == "__main__":
    nltk_setup(init=False)
    titles, abstracts = scrape_gtac()
    analyze_pres(abstracts)
