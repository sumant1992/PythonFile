import mysql.connector 
  
  
# Connecting from the server 
conn = mysql.connector.connect(user = 'root',
	                           password = 'root',
                               host = 'localhost', 
                              database = 'test6') 
  
print(conn) 
print("COnnected sucessfully")
  
# Disconnecting from the server 
conn.close() 