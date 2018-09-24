#!/usr/bin/python
# http://www.tutorialspoint.com/python/python_command_line_arguments.htm

import os
import sys
import getopt

def main(arguments):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(arguments,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print '\n %s -i <inputfile> -o <outputfile>\n' % os.path.basename(__file__)
        exit()
    for opt, arg in opts:
        if opt == '-h':
            print '\n %s -i <inputfile> -o <outputfile>\n' % os.path.basename(__file__)
            exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print 'Input file is "%s"' % inputfile
    print 'Output file is "%s"' % outputfile

if __name__ == "__main__":
    main(sys.argv[1:])
    #main(sys.argv[1:])
