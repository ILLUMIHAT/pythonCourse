import re
import requests


def get_subhead(url):
    response = requests.get(url)
    html = response.text
    pattern = r'<h3(?:\s+.*?)*?>(.*?)</h3>'
    subhead = re.findall(pattern, html)
    return subhead


url = 'http://www.columbia.edu/~fdc/sample.html'
subhead = get_subhead(url)
print(subhead)