#
#

"""
#MAIN SNIPPET:

def main():
	

if __name__ == "__main__":
	main()

"""

"""
#Files
def main():
# Open a file for writing and create it if it doesn't exist
  f = open("textfile.txt","w+")
  
# Open the file for appending text to the end
#  f = open("textfile.txt","a+")

  # write some lines of data to the file
  for i in range(10):
    f.write("This is line %d\r\n" % (i+1))
  
# close the file when done
  f.close()
  
# Open the file back up and read the contents
  f = open("textfile.txt","r")
  if f.mode == 'r': # check to make sure that the file was opened
# use the read() function to read the entire file
    contents = f.read()
	
    
    fl = f.readlines() # readlines reads the individual lines into a list
    for x in fl:
      print x
	  
  print contents
	
if __name__ == "__main__":
	main()
"""


"""
#Path Utilities
#Working with the OS

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
	# Print the name of the OS
	print os.name;
	
	print "----------next block----------"
	
	# Check for item existence and type
	print "Item exists: " + str(path.exists("textfile.txt"))
	print "Item is a file: " + str(path.isfile("textfile.txt"))
	print "Item is a directory: " + str(path.isdir("textfile.txt"))
	
	print "----------next block----------"
	
	# Work with file paths
	print "Item's path: " + str(path.realpath("textfile.txt"))
	print "Item's path and name: " + str(path.split(path.realpath("textfile.txt")))
	
	print "----------next block----------"
	
	# Get the modification time
	t = time.ctime(path.getmtime("textfile.txt"))
	print t
	print datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
	
	print "----------next block----------"
	
	# Calculate how long ago the item was modified
	td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
	print "It has been " + str(td) + " Since The file was modified"
	print "Or, " + str(td.total_seconds()) + " seconds"

if __name__ == "__main__":
	main()
"""


"""
# More OS stuff

import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

def main():
	# make a duplicate of an existing file
	if path.exists("textfile.txt"):
		# get the path to the file in the current directory
		src = path.realpath("textfile.txt");
		
		# separate the path part from the filename
		head, tail = path.split(src)
		print "path: " + head
		print "file: " + tail
		
		# let's make a backup copy by appending "bak" to the name
		dst = src + ".bak"
		# now use the shell to make a copy of the file
		shutil.copy(src,dst)
		
		# copy over the permissions, modification times, and other info
		shutil.copystat(src, dst)
		
		# rename the original file
		os.rename("textfile.txt", "newfile.txt")
		
		# now put things into a ZIP archive
		root_dir,tail = path.split(src)
		shutil.make_archive("archive", "zip", root_dir)

		# more fine-grained control over ZIP files
		with ZipFile("testzip.zip","w") as newzip:
			newzip.write("newfile.txt")
			newzip.write("textfile.txt.bak")

#this doesnt seem to work, i dont know why..........
	
if __name__ == "__main__":
	main()
"""
















