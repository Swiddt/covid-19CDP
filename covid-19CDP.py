from lxml import html
import requests

def scrab_xpath(url, xpath):
  page = requests.get(url)
  tree = html.fromstring(page.content)
  result = tree.xpath(xpath)[0]
  
  value = ''
  for c in result:
    if not c.isdigit():
      break
    value += c
  
  print(value)

url = 'https://www.kreis-re.de/Inhalte/Buergerservice/Gesundheit_und_Ernaehrung/Infektionsschutz/Coronavirus.asp'
scrab_xpath(url, '//*[@id="id35557"]/ul[1]/li/strong/text()')

#r = requests.get(url)
#print(r.text)
#value = ''.join(filter(str.isdigit, str(result)))
