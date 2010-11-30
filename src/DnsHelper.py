#
################################################################################
# DnsHelper
# (c) Carlos@LACNIC.net 20101126
################################################################################

import sys
from dns.resolver import *
import time

# BEGIN DnsHelper
class DnsHelper:
    resolver = None
    
    def __init__(self, w_file=None):
        self.resolver = Resolver(w_file)
    ## END init
        
    def query(self, w_rname, w_rtype):
        result_values = {"answers": None}
        start_ts = time.time()
        
        try:
            answers = self.resolver.query(w_rname, w_rtype)
            stop_ts = time.time()
            result_values["status"]  = "OK"
            result_values["answers"] = answers
        except Timeout:
                stop_ts = time.time()
                result_values["status"] = "Timeout"
        except NXDOMAIN:
                stop_ts = time.time()
                result_values["status"] = "NXDOMAIN"
        except NoAnswer:
                stop_ts = time.time()
                result_values["status"] = "NoAnswer"
        except NoNameservers:
                stop_ts = time.time()
                result_values["status"] = "NoNameservers"
        
        result_values["query_time_msec"] = (stop_ts - start_ts) * 1000
                
        return result_values
    ## END query
    
# END DnsHelper