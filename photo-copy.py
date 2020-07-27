#!/usr/bin/python3

import argparse
import os
from io import StringIO
from os.path import isfile, join


def copy_file(src, dst):
	if isfile(dst):
		if os.path.getsize(src) == os.path.getsize(dst):
			print(dst+" exist with:"+str(os.path.getsize(dst))+", skip it.")
			return
		dst = os.path.splitext(dst)[0]+"-1"+os.path.splitext(dst)[1]
		copy_file(src, dst)
		return

	print(src + "-->" + dst)
	os.rename(src, dst)


def main():
	argparser = argparse.ArgumentParser()
	argparser.add_argument("-s", "--source", help="source dir",  default="", required=True)
	argparser.add_argument("-d", "--dest", help="dest dir",  default="", required=True)

	args = argparser.parse_args()

	if args.source == "" :
		print("Enter source file parameter!!!")
		return

	if args.dest == "" :
		print("Enter dest dir parameter!!!")
		return

	srcfiles = os.listdir(args.source)
	for f in srcfiles:
		src = join(args.source, f)
		dst = join(args.dest, f)
		copy_file(src, dst)


if __name__ == "__main__":
	main()
