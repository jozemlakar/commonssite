#########################
## Veris Power Monitor ##
##     Xml Parser      ##
#########################

# V .3
# Updated 2/13/14
# Written by Max B. for the Harley School
# With thanks to a random website for the auth function

# V .2 Additions:
# Added Settings File
#
# V .3 Additions:
# Moved from urllib2 to requests, faster, 2 lines of code instead of 30, so much easier
# made it so the etree object is only made once, saves computing time
# Implemented the timestamp
# Implemented a listreturn() that returns a list of headers along with a list of values (for Harley's commons logging project)
# reduced unnecessary redundant operations (imports, xml object creation, etc)

# TODO:
# Add something to show when a channel is in alarm state
# implement standard dict for main class (implemented the 2 list way, ask Richard to confirm)
# explore pythonic way to implement standard dict (not lists)

# Functions:
# -n writes over the existing data/creates the file, and then writes the headers based on the names in the xml
# -l logs a row
# --list writes out a list of headers, then a list of values
#
# Choice function:
# Allows you to choose between multiple panels
# IN THIS IMPLEMENTATION, your choices are 3 or 4
#
# uses a settings file, DO NOT RUN WITHOUT settings.py IN THE SAME DIRECTORY

# IMPORT ALL THE THINGS!!!
from settings import veris_uname, veris_password, url3, url4
import requests, sys, time
from pprint import pprint
# Import element tree on all installs of python
try:
  # Python 2.5
  import xml.etree.cElementTree as etree
  #print("running with cElementTree on Python 2.5+")
except ImportError:
  try:
    # Python 2.5
    import xml.etree.ElementTree as etree
    #print("running with ElementTree on Python 2.5+")
  except ImportError:
    try:
      # normal cElementTree install
      import cElementTree as etree
      #print("running with cElementTree")
    except ImportError:
      try:
        # normal ElementTree install
        import elementtree.ElementTree as etree
        #print("running with ElementTree")
      except ImportError:
        # Or not...
        print("Failed to import ElementTree from any known place")

# Decides which url to use
def url(choice):
  if choice == 3:
    return url3
  elif choice == 4:
    return url4
# # Decides which file to put the logs in
# def filepath(choice):
#   if choice == 3:
#     return place3
#   elif choice == 4:
#     return place4

# used to use over 20 lines of code here (urllib2)
# yay for requests!
def getpage(theurl, veris_uname, veris_password):
  print 'Getting data'
  get = requests.get(theurl, auth=(veris_uname, veris_password))
  return get.text

# writes over whatever was there and writes the header line based off of the xml provided
def csvwriteheaders(xmltree, place):
  biglist = []
  biglist.append('Time')
  for thing in xmltree.findall('.//point'):
    biglist.append(thing.attrib['name'] + ' (' + thing.attrib['units'] + ')')
  with open(place, 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(biglist)

def returnheaders(xmltree):
  biglist = []
  biglist.append('Time')
  for thing in xmltree.findall('.//point'):
    biglist.append(thing.attrib['name'] + ' (' + thing.attrib['units'] + ')')
  return biglist

# generates a line of logging from xml provided
def loglist(xmltree):
  biglist = []
  time = xmltree.find('.//time')
  biglist.append(time.text + ' ' + time.attrib['zone'])
  for thing in xmltree.findall('.//point'):
    biglist.append(thing.attrib['value'])
  return biglist

# appends to a csv file based on list provided
def csvwriter(thelist, place):
    with open(place, 'ab') as csvfile:
      writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      writer.writerow(thelist)

# returns a list of headers along with a list of values
def listreturn(choice):
  choice = int(sys.argv[2])
  theurl = url(int(choice))
  thepage = getpage(theurl, veris_uname, veris_password)
  etreeobject = etree.fromstring(thepage)
  headerlist = returnheaders(etreeobject)
  loginlist = loglist(etreeobject)
  return headerlist, loginlist



# ties it all together
if __name__ == '__main__':
  cla = sys.argv[1]
  choice = int(sys.argv[2])
  if cla == '--list':
    pprint(listreturn(choice))