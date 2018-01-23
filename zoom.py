# Required modules
import argparse
import requests
import json

# Just some colors and shit bro
white = '\033[97m'
green = '\033[1;32m'
red = '\033[1;31m'
yellow = '\033[1;33m'
end = '\033[1;m'
info = '\033[1;33m[!]\033[1;m'
que =  '\033[1;34m[?]\033[1;m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'
run = '\033[1;97m[~]\033[1;m'

parser = argparse.ArgumentParser() # defines the parser
parser.add_argument('-u', '--url', help='Target wordpress website') # Adding argument to the parser
args = parser.parse_args() # Parsing the arguments

print ('''%s  ____                
 /_  / ___  ___  ____ 
  / /_/ %s_ \/ _%s \/    \\
 /___/\___%s/\%s___/_/_/_/%s\n''' % (yellow, white, yellow, white, yellow, end))

if args.url:
	url = args.url # args.url contains value of -u option
	if 'http' not in url:
		url = 'https://' + url
	response = requests.get('%s/wp-json/wp/v2/users' % url).text
	if 'Sorry, you are not allowed to list users.' in response:
		print (' %s Not vulnerable' % bad)
	else:
		data = json.loads(response)
		print (' %s+--------------------------+-------------------------------+%s' % (yellow, end))
		print (' %s| Display Name             | Username                      |%s' % (yellow, end))
		print (' %s+--------------------------+-------------------------------+%s' % (yellow, end))
		for key in data:
			print (' %s|%s %-25s%s|%s %-30s%s|%s' % (yellow, end, key['name'], yellow, end, key['slug'], yellow, end))
		print (' %s+--------------------------+-------------------------------+%s' % (yellow, end))
else:
	parser.print_help()