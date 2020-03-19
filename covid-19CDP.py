from lxml import html
import requests
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

class district:
  id = '00' 
  name = 'district_name'
  url = 'https://www.test.com'
  scrab_function = 0
  pre = ''
  post = ''
  xpath = ''

def scrab_xpath(url, xpath, pre, post):
  page = requests.get(url)
  tree = html.fromstring(page.content)
  result = tree.xpath(xpath)[0]
  if not pre=='':
    offset = result.find(pre)
    result = result[len(pre)+offset:]

  value = ''
  for c in result:
    if not c.isdigit():
      break
    value += c
  
  print(value)
  return value

with open('districts.json', 'r') as file:
    data = file.read()
districts = json.loads(data)


for d in districts:
  if d.scrab_function ==0:
    scrab_xpath(d.url, d.xpath, d.pre, d.post)

#url = 'https://www.kreis-re.de/Inhalte/Buergerservice/Gesundheit_und_Ernaehrung/Infektionsschutz/Coronavirus.asp'
#scrab_xpath(url, '//*[@id="id35557"]/ul[1]/li/strong/text()')
url = 'http://www.aachen.de/DE/stadt_buerger/notfall_informationen/corona/aktuelles/index.html'
pre = "Aktuell "
scrab_xpath(url, '//*[@id="rahmeninhalt"]/div[3]/div[1]/div/div/read/ul[2]/li[1]/p/text()', pre, '')



#r = requests.get(url)
#print(r.text)
#value = ''.join(filter(str.isdigit, str(result)))
