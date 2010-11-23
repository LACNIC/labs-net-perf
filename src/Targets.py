#
################################################################################
# TARGET management
#
################################################################################

# import modules
import MySQLdb
from DbAccess import DbAccess

def target_crud_main(w_cmd, w_opts, w_args):
    # target_crud
    if w_cmd == "list":
        # list targets
        target_list()
        return
        
    if w_cmd == "del":
        # delete target
        target_del(w_opts)
        return
        
    if w_cmd == "add":
        # add target
        target_add(w_opts)
        return
    
    if w_cmd == "update":
        # update target
        target_update(w_opts)
        return
        
    print "Invalid command! %s" % (w_cmd)
## END target_crud

# target list
def target_list():

    db = DbAccess()
    print "# Listing targets"
    print "#"
    
    db.cursor.execute("SELECT * FROM targets ORDER BY `target-handle` DESC")
    
    cnt = 0
    print "{0:5} | {1:14} | {2:20} | {3:20} | {4:30} | {5:15} | {6:20}". \
        format("id","target-handle", "target-description", "create-datetime", "domain", "ipv4", "ipv6")
    while True:
        row = db.cursor.fetchone()
        if row == None:
            break
        print "{0:5} | {1:14} | {2:20} | {3:20} | {4:30} | {5:15} | {6:20}". \
            format(row["id"], row["target-handle"], row["target-description"],
                   str(row["create-datetime"]), row["domain"], 
                   row["ipv4"], row["ipv6"])
        cnt = cnt + 1
    
    print "#"
    print "# Total targets %s" % (cnt)
    
    db.conn.close()
# END target list

# target add
def target_add(w_parms):
    # target add
    # print "Adding target -- opts %s " % str(w_parms)
    sql = """INSERT INTO targets (`target-handle`, `create-datetime`, `target-description`, ipv4, ipv6, domain) VALUES (%s, NOW(), %s, %s, %s, %s)"""
    #
    values = {"target-handle":"", "target-description":"", "ipv4":"", "ipv6":"", "domain":""}
    print "Adding target:"
    for el in w_parms:
        if el[0]=="-f":
            el0parts = el[1].partition('=')
            if el0parts[1] != "":
                values[el0parts[0]] = el0parts[2]
    print "Values: %s" % str(values)
    # connect to DB
    db = DbAccess()
    db.cursor.execute(sql, (values["target-handle"], values["target-description"], values["ipv4"], values["ipv6"], values["domain"] ))
    db.conn.close()
# END target add

# target update
def target_update(w_parms):
    # target add
    # print "Adding target -- opts %s " % str(w_parms)
    sql = """UPDATE targets SET """
    #
    # values = {"target-description":"", "ipv4":"", "ipv6":"", "domain":""}
    values = {}
    print "Adding target:"
    for el in w_parms:
        if el[0]=="-f":
            el0parts = el[1].partition('=')
            if el0parts[1] != "":
                values[el0parts[0]] = el0parts[2]
                sql = sql + "`{0}` = %({1})s, ".format(el0parts[0], el0parts[0])
    sql = sql[0:len(sql)-2] + " WHERE `target-handle`=%(target-handle)s"
    print "Values: %s" % str(values)
    # print "Sql: %s" % (sql)
    # connect to DB
    db = DbAccess()
    db.cursor.execute(sql, values)
    db.conn.close()
# END target update

# target del
def target_del(w_parms):
    sql1 = """DELETE FROM targets WHERE id = %s"""
    sql2 = """DELETE FROM targets WHERE target-handle = %s"""
    print "Deleting targets"
    values = {}
    print "Adding target:"
    for el in w_parms:
        if el[0]=="-f":
            el0parts = el[1].partition('=')
            if el0parts[1] != "":
                values[el0parts[0]] = el0parts[2]
    
    rk = values.popitem()
    print "Deleting targets where: %s" % str(rk)
    db = DbAccess()
    if rk[0] == "id":
        db.cursor.execute(sql1, (rk[1]) )
    if rk[1] == "target-handle":
        db.cursor.execute(sql2, (rk[1]) )
    print "Affected rows %s" % (db.cursor.rowcount)
    db.conn.close()
# END target del

################################################################################