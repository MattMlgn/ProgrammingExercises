import sys
from bs4 import BeautifulSoup, SoupStrainer
import requests
import time

url = "https://www.oxfordlearnersdictionaries.com/definition/english/" + \
    sys.argv[1] + "?q="+sys.argv[1]


type = []
plural = []

headers = requests.utils.default_headers()

headers.update(
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    }
)

response = requests.get(url, headers=headers)

data = response.text
soup = BeautifulSoup(data, 'html.parser')

type.append(soup.find_all('<span class="pos" hclass="pos" htag="span"></span>'))
print(type)
