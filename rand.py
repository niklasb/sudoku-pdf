import sys
import os
import random
dir = os.path.join("sudokus",sys.argv[1])
files = os.listdir(dir)
random.shuffle(files)
for f in files[:6]:
  print "".join(open(os.path.join(dir,f)).readlines()[:9])
