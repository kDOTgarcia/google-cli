from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
import argparse
import webbrowser
import http.client

google = 'http://www.google.com/search?q='
parser = argparse.ArgumentParser()
parser.add_argument('term', help='term to search by')

tbmgroup = parser.add_mutually_exclusive_group()
tbmgroup.add_argument(
    '-i', '--image', help='search for images', action="store_true")
tbmgroup.add_argument(
    '-v', '--video', help='search for videos', action="store_true")
tbmgroup.add_argument(
    '-n', '--news', help='search for news', action="store_true")

tbsgroup = parser.add_mutually_exclusive_group()
tbsgroup.add_argument(
    '-d', '--day', help='from the last day', action="store_true")
tbsgroup.add_argument(
    '-w', '--week', help='from the last week', action="store_true")
tbsgroup.add_argument(
    '-m', '--month', help='from the last month', action="store_true")
tbsgroup.add_argument(
     '-y', '--year', help='from the last year', action="store_true")

args = parser.parse_args()

term = '/search?q=' + args.term.replace(" ", "+")

if args.image:
    term = term + '&tbm=isch'
if args.video:
    term = term + '&tbm=vid'
if args.news:
    term = term + '&tbm=nws'

if args.day:
    term = term + '&tbs=qdr:d'
if args.week:
    term = term + '&tbs=qdr:w'
if args.month:
    term = term + '&tbs=qdr:m'
if args.year:
    term = term + '&tbs=qdr:y'

connection = http.client.HTTPSConnection(google)

connection.request('GET', term, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
})

response = connection.getresponse()

soup = BeautifulSoup(response.read(), 'html.parser')

if args.image:
    results = soup.find_all('a', attrs={'class': 'VFACy kGQAp'})
    for element in results[:20]:
        header = element.find_all('div', attrs={'class': 'WGvvNb'})
        link = element['href']
        if header != []:
            print(Fore.RED + header[0].getText())
        print(Style.RESET_ALL)
        print(link + "\n\n")
elif args.video:
    results = soup.find_all(
        'div', attrs={'class': 'isv-r PNCib MSM1fd BUooTd'})
    print(results)
    for element in results:
        header = element.find_all('h3')
        link = element.find_all('a')
        if header != []:
            print(Fore.RED + header[0].getText())
        if link != []:
            print(Style.RESET_ALL)
            print(link[0]['href'] + "\n\n")
elif args.news:
    results = soup.find_all(
        'div', attrs={'class': 'isv-r PNCib MSM1fd BUooTd'})
    print(results)
    for element in results:
        header = element.find_all('h3')
        link = element.find_all('a')
        if header != []:
            print(Fore.RED + header[0].getText())
        if link != []:
            print(Style.RESET_ALL)
            print(link[0]['href'] + "\n\n")
else:
    results = soup.find_all('div', attrs={'class': 'rc'})
    for element in results[:20]:
        header = element.find_all('h3')
        link = element.find_all('a')
        if header != []:
            print(Fore.RED + header[0].getText())
        if link != []:
            print(Style.RESET_ALL)
            print(link[0]['href'] + "\n\n")

# mac
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# windows
#chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
#webbrowser.get(chrome_path).open(google + term)
