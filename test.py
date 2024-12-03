import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"D:/Applications/instantclient-basic-windows.x64-23.5.0.24.07/instantclient_23_5")

try:
    
    connection = cx_Oracle.connect("junepixs@outlook.com", "77512345qscAB!", "m8ou38cqhsri49ol_medium" )
    # connection = cx_Oracle.connect('junepixs@outlook.com/77512345qscAB!@188.211.163.8:1522/g2441ea3151a447_m8ou38cqhsri49ol_medium.adb.oraclecloud.com' )
    print("successfully connected")
except cx_Oracle.DatabaseError as e:
    print("failed info: ", e)