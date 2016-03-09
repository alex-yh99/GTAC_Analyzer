from string import punctuation

import nltk
from matplotlib import pyplot
from nltk import word_tokenize, FreqDist
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from conf import proxies, nltk_packages


def nltk_setup(init=False):
    if init:
        nltk.set_proxy(proxies['http'])
        for p in nltk_packages:
            nltk.download(p)


def analyze_pres(content):
    abstract_str = ' '.join(content)

    # Tokenize
    tokens = word_tokenize(abstract_str)

    # Strip punctuation off the tokens
    tokens_striped = [w.strip(''.join(punctuation)) for w in tokens if w not in punctuation]

    # Remove stop words, such as 'the', 'a', 'and'
    stop_words = stopwords.words('english')
    tokens_filtered = [w for w in tokens_striped if w not in stop_words]

    # Combine singular and plural, such as 'test' / 'tests'
    lemmatizer = WordNetLemmatizer()
    tokens_combined = [lemmatizer.lemmatize(w) for w in tokens_filtered]

    fd = FreqDist(tokens_combined)
    plot(fd, 10)


def plot(fd, num=0, cumulative=False, title=None):
    # Get samples and frequencies
    samples, freq, accu = [], [], 0
    for s, f in fd.most_common(num):
        accu = accu + f if cumulative else f
        samples.append(s)
        freq.append(accu)
    # Create plot
    pyplot.grid(True, color='silver')
    if title:
        pyplot.title(title)
    pyplot.plot(freq, linewidth=2)
    pyplot.xticks(range(len(samples)), samples, rotation=45)
    pyplot.ylabel('Cumulative Counts' if cumulative else 'Counts')
    pyplot.show()
