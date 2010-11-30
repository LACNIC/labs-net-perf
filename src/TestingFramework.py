#
################################################################################
# TESTING FRAMEWORK management
# (c) Carlos@LACNIC.net 20101123
################################################################################

import DbAccess
import datetime
import time

class NetPerfTest:
    "NetPerfTest: (c) Carlos 20101123"
    
    ## Variables
    _targetList = None
    
    # constructor
    def __init__(self):
        pass
    ## END constructor
    
    # load target list
    def _loadTargetList(self, w_whereCond):
        db = DbAccess.DbAccess()
        sql = "SELECT * FROM targets WHERE {0}".format(w_whereCond)
        try:
            db.cursor.execute(sql)
            self._targetList = db.cursor.fetchall()
        except:
            print "ERROR! sql was: %s" % sql
        db.conn.close()
    ## END loadTargetList
    
    # store test result
    def _storeTestResult(self, w_values):
        db = DbAccess.DbAccess()
        w_values["test-datetime"] = time.strftime("%Y-%m-%d %H:%M:%S")
        db.autoInsert("test-results", w_values)
        db.conn.close()
    ## END storetestresult
    
    ## test a single target
    def performTest(self, w_target):
        pass
    ## END test a single target
    
    ## test all targets
    def testAllTargets(self):
        cnt = 0
        for target in self._targetList:
            print "[{0:3}] Testing target {1}".format(cnt, target["target-handle"])
            self.performTest(target)
            # print "[{0:3}] target is: {1}".format(cnt, str(target))
            cnt = cnt + 1
    ## END testAllTargets
## END NetPerfTest

__x_msgCount = 0

def printd(w_msg, w_testingMode):
    global __x_msgCount
    if w_testingMode:
        print "%% {0:3}:{1}".format(__x_msgCount, w_msg)
        __x_msgCount = __x_msgCount + 1
    else:
        # do not print anything
        pass


## TOP Level Script
if __name__ == "__main__":
    print "NetPerfTest: no tests implemented"

## END TESTING FRAMEWORK