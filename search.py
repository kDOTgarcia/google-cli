import argparse
import webbrowser

google = 'http://www.google.com/search?q='
parser = argparse.ArgumentParser()
parser.add_argument('term', help='term to search by')

tbmgroup = parser.add_mutually_exclusive_group()
tbmgroup.add_argument('-i', '--image', help='search for images', action="store_true")
tbmgroup.add_argument('-v', '--video', help='search for videos', action="store_true")
tbmgroup.add_argument('-n', '--news', help='search for news', action="store_true")

tbsgroup = parser.add_mutually_exclusive_group()
tbsgroup.add_argument('-d', '--day', help='from the last day', action="store_true")
tbsgroup.add_argument('-w', '--week', help='from the last week', action="store_true")
tbsgroup.add_argument('-m', '--month', help='from the last month', action="store_true")
tbsgroup.add_argument('-y', '--year', help='from the last year', action="store_true")


args = parser.parse_args()

term = args.term
#mac
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

#windows
#chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

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

webbrowser.get(chrome_path).open(google + term)