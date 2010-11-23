#
################################################################################
# Ipv6DnsTest
# (c) Carlos@LACNIC.net 20101123
################################################################################

import sys
from TestingFramework import *
from dns.resolver import *
import time

## class to test ipv6 dns resolvability

class Ipv6DnsTest(NetPerfTest):
    
    # constructor
    def __init__(self):
        self._loadTargetList("domain != ''")
    ## END constructor
    
    # performTest on a single target
    def performTest(self, w_target, w_updateDb = True):
        myres = Resolver("v6only.resolv.conf")
        result_values = {"test-handle": "v6-dns-resol",
                         "target-handle": w_target["target-handle"]}
        answers = []
        start_ts = time.time()
        try:
            answers = myres.query(w_target["domain"], "SOA")
            stop_ts = time.time()
            result_values["str01"]  = "QueryOK"
            result_values["status"] = "OK"
        except Timeout:
                stop_ts = time.time()
                result_values["str01"] = "Timeout"
                result_values["status"] = "FAIL"
        except NXDOMAIN:
                stop_ts = time.time()
                result_values["str01"] = "NXDOMAIN"
                result_values["status"] = "FAIL"
        except NoAnswer:
                stop_ts = time.time()
                result_values["str01"] = "NoAnswer"
                result_values["status"] = "FAIL"
        except NoNameservers:
                stop_ts = time.time()
                result_values["str01"] = "NoNameservers"
                result_values["status"] = "FAIL"
                
        # build result set
        result_values["real02"]  = (stop_ts - start_ts)*1000
        for rdata in answers:
            result_values["int01"] = rdata.serial
        
        # update db
        if w_updateDb:
            self._storeTestResult(result_values)
        else:
            print "Not updating DB"
        
        return result_values
    ## END performTest
    
## END class Ipv6DnsTest

## Top Level Script Block
if __name__ == "__main__":
    test = Ipv6DnsTest()
    if len(sys.argv) > 1:
        dn = sys.argv[1]
    else:
        dn = "www.lacnic.net"
        
    target = {"target-handle":"lac-ws", "domain": dn}
    print "## Test #1"
    print "Input: %s" % str(target)
    print "Output: %s" % str(test.performTest(target, False))
    print "## END Text #1"
## END top level script block