import sys
import urllib.request as req
import urllib.parse as parse

if len(sys.argv) <= 1:
    print("usage: download-forecast-argv <region number>")
    sys.exit()
    
region_number = sys.argv[1]

api_url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId' : region_number
}

params = parse.urlencode(values)
url = api_url + "?" + params
print("url = ", url)

data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)