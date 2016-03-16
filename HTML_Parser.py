import urllib
import itertools
import codecs
import sys
from bs4
import BeautifulSoup
url = r "/root/data/en/articles/your_input_file.html"
page = open(url)
soup = BeautifulSoup(page.read())
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
data_lines = []
for i in lines:
    if len(i) != 0:
    3
data_lines.append(i)
actual = []
for i in data_lines:
    if len(i) != 1:
    actual.append(i)
words = []
for line in actual:
    words.append(line.strip().split(''))
merged = list(itertools.chain( * words))
with codecs.open("/root/sample.txt", "w", encoding = "utf-8") as f:
    for i in merged:
    f.write(i + '\n')