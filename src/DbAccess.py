#
################################################################################
# DB access management
# 2010 11 22
# (c) Carlos@lacnic.net
################################################################################

# from MySQLdb import *
import MySQLdb
import sys

class DbAccess:
    
    conn = ""
    cursor = ""
    e = ""
    
    ## init ##
    def __init__(self):
        try:
            self.conn = MySQLdb.connect( host="localhost",
                                    user="root",
                                    passwd="Js$z::VR8x",
                                    db="net-perf")
            self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        except MySQLdb.Error(self.e):
            print "DB Error %s %s" % (self.e.args[0], self.e.args[1])
    ## -- ##
    
    ## getCursor ##
    def getCursor(self):
        return self.cursor
    ## -- ##
    
    ## filterValues
    def _filterValues(self, w_tableName, w_values):
        w_filteredValues = {}
        
        # load column names from database
        self.cursor.execute("DESC `{0}`".format(w_tableName))
        while True:
            row = self.cursor.fetchone()
            if row == None:
                break
            # print str(row)
            colname = row["Field"]
            if w_values.has_key(colname):
                w_filteredValues[colname] = w_values[colname]
        
        return w_filteredValues
    ## end filterValues
    
    # autoInsert
    def autoInsert(self, w_tableName, w_values):
        sql = "INSERT INTO `{0}` ".format(w_tableName)
        w_values = self._filterValues(w_tableName, w_values)
        # print str(w_values)
        # sys.exit()
        
        
        sqlCols = " ("
        sqlVals = " VALUES ("
        for k in w_values.keys():
            sqlCols = sqlCols + "`{0}`, ".format(k)
            sqlVals = sqlVals + "%({0})s, ".format(k)
        sqlCols = sqlCols[0:len(sqlCols)-2] + ")"
        sqlVals = sqlVals[0:len(sqlVals)-2] + ")"
        
        sql = sql + sqlCols + sqlVals
        
        # print "autoInsert sql %s" % sql
        self.cursor.execute(sql, w_values)
    ## END autoInsert

## if top level script
if __name__ == "__main__":
    print "== Test #1: autoInsert SQL"
    db = DbAccess()
    db.autoInsert("test-results", {"target-handle":"uy-tld", "int01":"100"})

################################################################################
