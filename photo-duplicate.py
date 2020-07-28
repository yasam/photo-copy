#!/usr/bin/python3

import argparse
import os
from io import StringIO
from os.path import isfile, join
import hashlib



def main():
	argparser = argparse.ArgumentParser()
	argparser.add_argument("-s", "--source", help="source dir",  default="", required=True)

	args = argparser.parse_args()

	if args.source == "" :
		print("Enter source file parameter!!!")
		return

	files = dict()
	srcfiles = os.listdir(args.source)
	for f in srcfiles:
		fname = join(args.source, f)
		size = os.path.getsize(fname)
		if size not in files:
			files[size] = []
		files[size].append({"name":fname})


	for k in files.keys():
		if len(files[k]) <= 1 :
			continue

		hashes = dict()
		for e in files[k]:
			f = open(e["name"], 'rb')
			filehash = hashlib.md5(f.read()).hexdigest()
			f.close()
			if filehash not in hashes:
				hashes[filehash] = e["name"]
			else:
				print(e["name"]+" duplicates "+hashes[filehash] + " size:" + str(k) + " hash:"+filehash)

if __name__ == "__main__":
	main()
