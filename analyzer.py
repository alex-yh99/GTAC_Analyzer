import re
from operator import itemgetter
from string import punctuation

import nltk
from nltk import word_tokenize, FreqDist
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from conf import proxies, nltk_packages
from scraper.glossary_scraper import GlossaryScraper
from util import plot


def nltk_setup(init=False):
    if init:
        nltk.set_proxy(proxies['http'])
        for p in nltk_packages:
            nltk.download(p)


def get_word_frequencies(content: list, most_common: int):
    content_str = ' '.join(content)

    # Tokenize
    tokens = word_tokenize(content_str)

    # Strip punctuation off the tokens
    tokens_striped = [w.strip(''.join(punctuation)) for w in tokens
                      if w not in punctuation]

    # Remove empty string and stop words, such as 'the', 'a', 'and'
    stop_words = stopwords.words('english')
    tokens_filtered = [w for w in tokens_striped
                       if w.strip() and w.lower() not in stop_words]

    # Combine singular and plural, such as 'test' / 'tests'
    # Convert all tokens to lowercase
    lemmatizer = WordNetLemmatizer()
    tokens_combined = [lemmatizer.lemmatize(w).lower() for w in tokens_filtered]

    return FreqDist(tokens_combined).most_common(most_common)


def analyze_test_info(data: list, title: str, graph_name: str):
    data_str = ' '.join(data)
    total_count = 20
    glossary = GlossaryScraper()

    freq_words = [(w, len(re.findall(w, data_str, re.IGNORECASE))) for w in glossary.glossaries]
    sorted_freq_words = sorted(freq_words, key=itemgetter(1), reverse=True)

    fig1 = plot(sorted_freq_words[0: total_count],
                '{} (Test Topics)'.format(title), 'Word Counts')
    fig1.savefig('{}_glossaries.png'.format(graph_name))

    fig2 = plot(get_word_frequencies(data, total_count),
                '{} (Word Frequencies)'.format(title), 'Word Counts')
    fig2.savefig('{}_word_frequencies.png'.format(graph_name))
