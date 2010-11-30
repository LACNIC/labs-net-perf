#
################################################################################
# Ipv6DnsTest
# (c) Carlos@LACNIC.net 20101123
################################################################################

import sys
from TestingFramework import *
from dns.resolver import *
from DnsHelper import *
import time

## class to test ipv6 dns resolvability
class Ipv6DnsTest(NetPerfTest):
    
    # constructor
    def __init__(self):
        self._loadTargetList("domain != ''")
    ## END constructor
    
    # performTest on a single target
    def performTest(self, w_target, w_testingMode = False):
        start_time = time.time()
        myres = DnsHelper("v6only.resolv.conf")
        
        result_values = myres.query(w_target["domain"], "NS")
        result_values["status"] = "GENFAIL"
        
        result_values["test-handle"]   = "v6-dns-resol"
        result_values["target-handle"] = w_target["target-handle"]
                
        if result_values["answers"] != None:
            # STEP 2: if answers are not empty, we have NS records to traverse
            v6ns = {}
            for nsrec in result_values["answers"]:
                # try to get an AAAA record for each NS record
                res1 = myres.query(nsrec.target,"AAAA")
                if res1["answers"] != None:
                    # at least one ipv6 nameserver was found!!
                    for r2 in res1["answers"]:
                        printd("Found AAAA {0} / {1}".format(nsrec.target,r2), w_testingMode)
                        v6ns[r2.address] = str(nsrec.target)
                else:
                    # no ipv6 ns found, best luck with the next record
                    printd("No AAAA found for {0}".format(nsrec.target), w_testingMode)
                    pass
                
            if len(v6ns.keys()) == 0:
                # No ipv6 NS found
                result_values["status"] = "NoV6NS"
            else:
                # STEP 3: try to obtain a SOA answer
                printd("V6 ns list: {0}".format(str(v6ns)), w_testingMode)
                for v6server in v6ns.keys():
                    myres.resolver.reset()
                    myres.resolver.nameservers = []
                    myres.resolver.nameservers.append(v6server)
                    printd("Trying to get SOA from {0}".format(v6server), w_testingMode)
                    r3 = myres.query(w_target["domain"], "SOA")
                    if r3["answers"] != None:
                        result_values["status"] = "OK"
                        result_values["int01"] = r3["answers"][0].serial
                        result_values["str01"] = v6server
                        result_values["str02"] = v6ns[v6server] 
                        break
                    else:
                        result_values["status"] = "NoV6Answer"
                        result_values["int01"] = 0
                    
        else:
            # no NS at all found for domain
            result_values["int01"] = 0
            
        
        # record time
        stop_time = time.time()
        result_values["real02"] = (stop_time - start_time)*1000
        
        # update db
        if not w_testingMode:
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
        dn = "lacnic.net"
        
    target = {"target-handle":"lac-ws", "domain": dn}
    print "## Test #1"
    print "Input: %s" % str(target)
    print "Output: %s" % str(test.performTest(target, True))
    print "## END Text #1"
## END top level script block