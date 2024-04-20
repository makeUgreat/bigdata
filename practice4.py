from bs4 import BeautifulSoup
import re

html = """
<ul>
    <li><a href="hoge.html">hoge</a></li>
    <li><a href="https://example.com/fuga">fuga</a></li>
    <li><a href="https://example.com/foo">foo</a></li>
    <li><a href="https://example.com/aaa">aaa</a></li>
</ul>
"""

soup = BeautifulSoup(html, 'html.parser')
href_reg = re.compile(r"^https://")
li = soup.find_all(href=href_reg) # -> href 태그의 값이 https:// 로 시작하는 모든 태그를 가져온다. 

for e in li:
    print(e.attrs['href'])
    print(e.string)