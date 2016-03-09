### Simple Web Scraper and Data-Processing practice in Python3

- Scrape all the abstracts of presentations from [GTAC](https://developers.google.com/google-test-automation-conference/) (2014~2016)
- Find out Software Testing trends
- Visualize Topic frequency

### Dev

##### 1. Setup virtualenv and install Python dependencies

```
pyvenv GTAC_Analyzer
source GTAC_Analyzer/bin/activate
pip install -r requirements.txt
```

Detailed info about Python3 virtualenv: <https://docs.python.org/3/library/venv.html>

> Windows `.whl` packages : <http://www.lfd.uci.edu/~gohlke/pythonlibs/>

##### 2. Download NLTK packages

`main.py`

```
if __name__ == "__main__":
    nltk_setup(init=False)  # Set `init` to `True` for NLTK installation
```

Edit `conf.py` if you are behind a web proxy.

> If <https://developers.google.com/> is blocked, make sure your proxy can bypass the firewall.

##### 3. Run scraper and analyzer

```
python main.py
```

> For OSX user with Shadowsocks and proxychains4: `proxychains4 python main.py`
