import sys
import os.path
import argparse

class Sort:
	def __init__(self):
		self.__unsorted_list = []

	def run(self):
		parser = argparse.ArgumentParser(usage='sort.py [options]', add_help=False)
		parser.add_argument('-f', '--file', dest='file')
		args = parser.parse_args()

		try:
			if args.file:
				if not os.path.isfile(args.file):
					print("\n[x] File not found: " + args.file + "\n |  Aborting...")
					sys.exit(-2)
				else:
					with open(args.file, 'r') as f:
						for line in f:
							if not(line.endswith('.') or line.endswith('-') or line.startswith('.')):
								self.__unsorted_list.append(line.split('\n')[0])
				for i in sorted(self.__unsorted_list):
					print(i)
		
		except KeyboardInterrupt:
			print("\nReceived keyboard interrupt.\nQuitting...")
			sys.exit(-1)
		
if __name__ == "__main__":
	main = Sort()
	main.run()
