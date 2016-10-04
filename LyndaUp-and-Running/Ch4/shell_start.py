#
# Example file for working with filesystem shell methods
#

import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile


def main():

  # make a duplicate of an existing file
  if path.exists("newfile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("newfile.txt");

    # separate the path part from the filename
#    head, tail = path.split(src)
#    print "path: " + head
#    print "file: " + tail

#    dst = src + ".bak"
#    shutil.copy(src, dst)
    # copy over the permissions, modification times, and other info
#    shutil.copystat(src, dst)

    # rename the original file
#    os.rename("textfile.txt", "newfile.txt")
    
    # now put things into a ZIP archive
#    root_dir,tail = path.split(src)
#    shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip","w") as newzip:
      newzip.write("newfile.txt")
      newzip.write("textfile.txt.bak")

if __name__ == "__main__":
  main()
