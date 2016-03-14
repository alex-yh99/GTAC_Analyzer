import atexit
import json
import os

from matplotlib import pyplot


# Inspired by: http://stackoverflow.com/a/16464555/1045475
def persist_to_file(file_name, extra_param=''):
    file_path = os.path.join('cache', file_name)
    try:
        cache = json.load(open(file_path, 'r'))
    except (IOError, ValueError):
        cache = {}

    atexit.register(lambda: json.dump(cache, open(file_path, 'w')))

    def decorator(func):
        def f(*args, **kwargs):
            key = file_name + '_' + kwargs.get(extra_param, '')
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]

        return f

    return decorator


def plot(data: list, title: str, xlabel: str):
    data_range = range(len(data))
    data_labels = [x[0] for x in data]
    data_values = [x[1] for x in data]

    fig = pyplot.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.grid(True)
    ax.set_title(title)
    rects = ax.barh(data_range, data_values, height=0.4, align='center', color='gray')
    ax.axvline(1.0 * sum(data_values) / len(data_values), color='b', linestyle='dashed')
    ax.set_ylim(-1, len(data))
    ax.set_yticks(data_range)
    ax.set_yticklabels(data_labels)
    ax.set_xlabel(xlabel)
    for idx, rect in enumerate(rects):
        ax.text(
            (rect.get_x() + rect.get_width()) * 1.1,
            rect.get_y() + rect.get_height() / 2.,
            '({})'.format(str(data[idx][1])),
            va='center', size='small', color='gray'
        )
    fig.tight_layout()

    return pyplot
