# ip to asn mapping from cymru DNS
# carlos@lacnic.net 20111209
#
# changes:
# 20120120 handle ipv6 localhost ('::1') correctly

from DnsHelper import DnsHelper
import sys

# make dns query to cymru
def iptoasn(p_ip_addr):
    dh = DnsHelper('/etc/resolv.conf')
    rv = None
    
    if p_ip_addr.find('.') > 0:
        # ipv4 address
        p_ip_addr_PARTS = p_ip_addr.split('.')
        p_ip_addr_PARTS.reverse()
        dns_name = "%s.origin.asn.cymru.com" % ( ".".join(p_ip_addr_PARTS) )
        pass
    elif p_ip_addr.find(':') >= 0:
        #i ipv6 address
        # get pfx only
        p_ip_addr_PARTS = p_ip_addr.split('::')
        pfx = p_ip_addr_PARTS[0]
        # split pfx and fill with zeros
        pfx_PARTS = pfx.split(':')
        pfx_PARTS = [c.zfill(4) for c in pfx_PARTS]
        # join and get nibbles in reverse order
        nibbles = list( "".join(pfx_PARTS) )
        nibbles.reverse()
        #
        dns_name = "%s.origin6.asn.cymru.com" % (".".join(nibbles))
        # raise Exception("Query for IPv6 address not yet implemented")
        pass
    else:
        raise Exception("Wrong IP address format: %s" % (p_ip_addr) )
    
    rv = dh.query(dns_name, "TXT")
    
    # further process answer
    rv['pfx'] = None
    rv['cc'] = None
    rv['rir'] = None
    rv['allocated'] = None
    rv['asn'] = None
    if rv['answers'] != None:
        ans_parts = rv['answers'][0].__str__().split("|")
        rv['asn'] = ans_parts[0].strip('"').strip()
        rv['pfx'] = ans_parts[1].strip()
        rv['cc'] = ans_parts[2].strip()
        rv['rir'] = ans_parts[3].strip()
        rv['allocated'] = ans_parts[4].strip('"')
        #
    return rv
## END ipto asn ######################

# make dns query to get full asn info ##
def asninfo(p_asn):
    dh = DnsHelper()
    rv = None
    
    dns_name = "AS%s.asn.cymru.com" % ( p_asn) 
    rv = dh.query(dns_name, "TXT")
    
    # further process answers
    rv['asn'] = None
    rv['cc'] = None
    rv['rir'] = None
    rv['allocated'] = None
    rv['org'] = None
    if rv['answers'] != None:
        ans_parts = rv['answers'][0].__str__().split("|")
        rv['asn'] = ans_parts[0].strip('"').strip()
        rv['cc'] = ans_parts[1].strip('"')
        rv['rir'] = ans_parts[2].strip()
        rv['allocated'] = ans_parts[3].strip()
        rv['org'] = ans_parts[4].strip('"').strip()

    return rv
## END full asn info ###################
     
## simple test case
if __name__ == "__main__":
    # print "My PYTHONPATH is %s" % (sys.path)
    if sys.argv.__len__()>2:
        cmd = sys.argv[1]
        val = sys.argv[2]
        if cmd == "ip":
            print "Querying IP to ASN mapping for IP %s " % (val)
            map = iptoasn(val)
        elif cmd == "asn":
            print "Querying ASN full info for ASN %s" % (val)
            map = asninfo(val)
        else:
            print "Wrong command!"
        #
        if map['answers'] != None:
            print map['answers'][0]
            # print map['org']
        else:
            print "No mapping info found"
        print "Query time was %s msec" % (map['query_time_msec'])
    else:
        print "Usage: iptoasn_cymru.py [ip 1.2.3.4] | [asn 28000]"
