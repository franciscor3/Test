#!/usr/bin/python
import sys
#obtain the number of the arguments to check if it has a file name.
#if there is no argument it show a message to insert the file name as an argument.
argNum = len(sys.argv)

if(argNum == 1):
    print "Please enter the name of the file to read as an argument"
else:
    fileName = sys.argv[1]
    """in this part import the url library depends if it is python 2.X the most
       popular or python 3.X the newest version.
     The library request the image from the URL and put it in the local disk,
     with the name obtained in the URL.
    """
    try:
        from urllib.request import urlretrieve  # Python 3
    except ImportError:
        from urllib import urlretrieve  # Python 2

        #Open the file in read mode only.
        file = open(fileName, 'r')

        #read each line of the file
        #then obtain the last part of the URL to put the name of the image
        #it makes the request and store the image locally with the same name as in the URL.
    for line in file:
        imgName = line.rsplit('/',1)[1]
        imgName = imgName[:-1]
        print imgName
        urlretrieve(line, imgName)

    #Make free all resources from the file.
    file.close()
