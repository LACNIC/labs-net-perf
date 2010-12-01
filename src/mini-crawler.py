#
####################################################################################################
# SimpleCrawler
# (c) carlos@lacnic.net 20101201
####################################################################################################


from harvestman.apps.spider import HarvestMan
from harvestman.lib.common.macros import *
from harvestman.lib import logger
import sys
from urlparse import urlparse

class MyCustomCrawler(HarvestMan):
	""" A custom crawler """

	size_threshold = 4096
	file = None
	tld = None
	url_list = {}

	## begin __init__
	def __init__(self):
		url_parms = self.get_url_parms(sys.argv[1])
		self.file = open("urls_"+url_parms["netloc"], "w")
		
		# get TLD
		self.tld = url_parms["tld"]
		print "%%%%%%%%%%%%%% Opa! TLD es %s" % str(self.tld)
		
		# init father
		HarvestMan.__init__(self)
	## end __init__

	## begin save_this_url
	def save_this_url(self, event, *args, **kwargs):
		""" Custom callback function which modifies behaviour of saving URLs to disk """
		# Get the url object
		url = str(event.url)
		url_parms = self.get_url_parms(url)
		if url_parms["tld"] == self.tld:
			print "%%%%%%%%%%%%%% Opa! domain found %s" % str(url_parms["netloc"])
			self.file.write(url_parms["netloc"]+'\n')
		# never save
		return True
	## end save_this_url
	
	def get_url_parms(self, url):
		url_parms = {}
		p_url = urlparse(url)
		url_parms["netloc"] = p_url.netloc
		p_url_netloc = p_url.netloc.split(".")
		url_parms["tld"] = p_url_netloc[len(p_url_netloc)-1]
		return url_parms	
	
## END MyCustomCrawler

# Set up the custom crawler
if __name__ == "__main__":
    crawler = MyCustomCrawler()
    crawler.init()
    # Get the configuration object
    config = crawler.get_config()
    config.set_option('fetchlevel_value',4)
    config.set_option('depth_value',2)
    config.set_option('verbosity', 2)
    config.add(url=sys.argv[1])
    config.setup()
    # Register for 'save_url_data' event which will be called
    # back just before a URL is saved to disk
    crawler.register('save_url_data', crawler.save_this_url)
    # Run
    crawler.main()
