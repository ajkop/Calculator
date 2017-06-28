#!/usr/bin/env python
import sys
def gbconvert(x):
    mb = int(x) * 1024
    print mb , "MB"
def mbconvert(x):
    if int(x) % 1024 == 0:
        gb = int(x) / 1024
    else:
        gb = float(x) / 1024
    print gb , "GB"
def checkint(x):
    try:
		ix = int(x)
		return ix
    except ValueError:
       print "You did not enter an Integer   ",


def execute(x,y):
	try:
		arg1 = x
	except IndexError:
		print "Usage: [M/G] [num] , You can specify M if you want to covert into MB and G if you want to convert to GB"
		sys.exit(1)
	if x == "M" or x == "m":
		checkint(y)
		try:
            gbconvert(y)
        except:
            gbconvert(raw_input("Enter GB Amount: "))
	elif x == "G" or x == "g":
		checkint(y)
		try:
        	mbconvert(y)
        except:
            mbconvert(raw_input("Enter MB Amount: "))


if __name__ == '__main__':
     execute(sys.argv[1],sys.argv[2])
