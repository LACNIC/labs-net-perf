#!/usr/bin/python26
################################################################################
# NET-PERF
# (c) CarlosM carlos@lacnic.net
################################################################################

# import needed internal modules
import getopt
import sys

# import internal modules
import Targets
import TestingFramework
import Ipv6DnsTest
import Web6Discovery

# main
print "NET-PERF (c) CarlosM carlos@lacnic.net"
# parse cmd line
options = "t:hf:"
long_options = ["target=", "test=","help"]

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
    if o in ("--test"):
        if opts[0][1] == "v6-dns-resol":
            print "Performing test (%s, %s) " % (str(opts), str(args))
            tst1 = Ipv6DnsTest.Ipv6DnsTest()
            tst1.testAllTargets()
        if opts[0][1] == "v6-serv-disc":
            print "Performing test (%s, %s) " % (str(opts), str(args))
            tst1 = Web6Discovery.Web6Discovery()
            tst1.testAllTargets()            
        else:
            print "Test %s not yet implemented!" % str(opts[0][1])
        
print "END RUN: net-perf"
################################################################################