#
################################################################################
# Web6Discovery
# (c) Carlos@LACNIC.net 20101130
################################################################################

import sys
from TestingFramework import *
from dns.resolver import *
from DnsHelper import *
import time

# BEGIN Web6Discovery
class Web6Discovery(NetPerfTest):
    
    w6hints = ['','www.', 'www6.', 'w6.', 'www.v6.', 'ipv6.', 'www.ipv6.', '6.']
    
    # init
    def __init__(self):
        self._loadTargetList("`target-handle` like '%gub%' AND domain != ''")
    # end init
    
    # performTest on a single target
    def performTest(self, w_target, w_testingMode = False):
        start_time = time.time()
        myres = DnsHelper("v4only.resolv.conf")
        result_values = {}
        dom_discovered = []

        result_values["test-handle"]   = "v6-serv-disc"
        result_values["target-handle"] = w_target["target-handle"]
        result_values["status"] = "FAIL"
            
        # try to get AAAA's by prefixing well known hints
        for pr in self.w6hints:
            target_domain = pr + w_target["domain"]
            printd("trying to get AAAA for {0}".format(target_domain), w_testingMode)
            ans2 = myres.query(target_domain, "AAAA")
            if ans2["answers"] != None:
                dom_discovered.append(target_domain)
                result_values["status"] = "OK"
                printd("   discovered!! ", w_testingMode)
            else:
                printd("   not found", w_testingMode)

        # join discoveries
        if len(dom_discovered) > 0:
            result_values["str01"] = ",".join(dom_discovered)

        # record time
        stop_time = time.time()
        result_values["real02"] = (stop_time - start_time)*1000
        
        # update db
        if not w_testingMode:
            self._storeTestResult(result_values)
        else:
            print "Not updating DB"        
        
        # return
        return result_values
    # end performTest
# END Web6Discovery

## Top Level Script Block
if __name__ == "__main__":
    test = Web6Discovery()
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