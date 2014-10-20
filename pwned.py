#!/usr/bin/env python
# -*- coding: utf-8 -*-

############ Version information ##############
__version__ = "0.2"
__program__ = "pwned v" + __version__
__description__ = 'Automatic "haveibeenpwned.com" checker'
__author__ = "Jan Rude"
__licence__ = "BSD Licence"
###############################################

import sys
import json
import urllib2
import datetime
import argparse
from os.path import isfile

# Main
def main(argv):
	parser = argparse.ArgumentParser(usage='pwned.py [options]')
	parser.add_argument('-f', '--file', dest='file', default='test.txt', help='File with a list of usernames/emails')
	args = parser.parse_args()

	try:
		if not isfile(args.file):
			if colorama:
				print(Fore.RED + "\nFile not found: " + args.file + "\nAborting..." + Fore.RESET)
			else:
				print("\nFile not found: " + args.file + "\nAborting...")
			sys.exit(-2)
		else:
			with open(args.file, 'r') as f:
				for line in f:
					checkIfPwned(line.strip('\n'))
					print ''

	except KeyboardInterrupt:
		if colorama:
			print Fore.RED + "\nReceived keyboard interrupt.\nQuitting..." + Fore.RESET
		else:
			print "\nReceived keyboard interrupt.\nQuitting..."
		exit(1)
	except Exception, e:
		import traceback
		print ('generic exception: ', traceback.format_exc())
	
	finally:
		print '\n'
		now = datetime.datetime.now()
		print __program__ + ' finished at ' + now.strftime("%Y-%m-%d %H:%M:%S") + '\n'
		if colorama:
			Style.RESET_ALL
		return True

def checkIfPwned(input):
	pwned = []
	try:
		response = urllib2.urlopen('https://haveibeenpwned.com/api/v2/breachedaccount/' + input)
		data = json.load(response)
		for i in range(0, len(data)):
			result = data[i]['Title']
			pwned.append(str(result))
		if colorama:
			print Fore.RED + input + ' - pwned!' + Fore.RESET
		else:
			print input + ' - pwned!'
		print pwned

	# getting back 404
	except:
		# you are not in a breach - phew
		# but maybe in a pastebin? - lets check!
		try:
			response = urllib2.urlopen('https://haveibeenpwned.com/api/v2/pasteaccount/' + input)
			data = json.load(response)
			for i in range(0, len(data)):
				result = data[i]['Title']
				pwned.append(str(result))
			
			if colorama:
				print Fore.RED + input + ' - pwned!' + Fore.RESET
			else:
				print input + ' - pwned!'
			print pwned
		# congrats, you are not pwned!
		except:
			if colorama:
				print Fore.GREEN + input + ' - no pwnage found!' + Fore.RESET
			else:
				print input + ' - no pwnage found!'

if __name__ == "__main__":
	try:
		from colorama import init, Fore, Style
		init()
		print Style.BRIGHT
		colorama = True
	except:
		colorama = False
	print('\n' + 54*'*')
	print('\t' + __program__ )
	print('\t' + __description__)
	print('\t' + '(c)2014 by ' + __author__)
	print(54*'*' + '\n')
	sys.exit( not main( sys.argv ) )
