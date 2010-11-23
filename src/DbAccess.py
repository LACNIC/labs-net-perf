#
################################################################################
# DB access management
# 2010 11 22
# (c) Carlos@lacnic.net
################################################################################

# from MySQLdb import *
import MySQLdb

class DbAccess:
    
    conn = ""
    cursor = ""
    e = ""
    
    ## init ##
    def __init__(self):
        try:
            self.conn = MySQLdb.connect( host="localhost",
                                    user="root",
                                    passwd="pass",
                                    db="net-perf")
            self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        except MySQLdb.Error(self.e):
            print "DB Error %s %s" % (self.e.args[0], self.e.args[1])
    ## -- ##
    
    ## getCursor ##
    def getCursor(self):
        return self.cursor
    ## -- ##

################################################################################