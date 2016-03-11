import atexit
import json
import os


# Inspired by: http://stackoverflow.com/a/16464555/1045475
def persist_to_file(file_name, extra_param=''):
    file_path = os.path.join('data', file_name)
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
