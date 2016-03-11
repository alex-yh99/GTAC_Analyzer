import re
from operator import itemgetter

from analyzer import nltk_setup
from scraper import GTACScraper, GlossaryScraper


def analyze_gtac_abstracts():
    gtac = GTACScraper()
    g = GlossaryScraper()

    abstracts = []
    for y in gtac.years:
        abstracts.extend(gtac.get_data(year=y)['abstracts'])
    abstracts_str = ' '.join(abstracts)

    freq_words = [(w, len(re.findall(w, abstracts_str, re.IGNORECASE))) for w in g.glossaries]
    sorted_freq_words = sorted(freq_words, key=itemgetter(1), reverse=True)

    print(sorted_freq_words[0: 10])


if __name__ == "__main__":
    nltk_setup(init=False)
    analyze_gtac_abstracts()
