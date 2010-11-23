#!/usr/bin/python26
################################################################################
# NET-PERF
# (c) CarlosM carlos@lacnic.net
################################################################################

# import needed internal modules
import getopt
import sys

# import interal modules
import Targets

# main
print "NET-PERF (c) CarlosM carlos@lacnic.net"
# parse cmd line
options = "t:hf:"
long_options = ["target=","help"]

try:
    opts, args = getopt.gnu_getopt(sys.argv[1:], options, long_options)
except Exception:
    print "Error!!"
    sys.exit(-1)

for o,a in opts:
    if o in ("-h", "--help"):
        print "Usage: ./net-perf.py [--target=cmd]\r\n"
        sys.exit(0)
    if o in ("-t", "--target"):
        print "Calling net-perf target %s" % a
        Targets.target_crud_main(a, opts, args)
        sys.exit(0)
        
print "END RUN: net-perf"
################################################################################