import sys
from rpmUtils.miscutils import splitFilename

if len(sys.argv)<2:
  print "No argument provided. Exiting."
  exit()
filename=sys.argv[1]
with open(filename, 'r') as handle:
    for line in handle:
      (n, v, r, e, a) = splitFilename(line)
      print n
