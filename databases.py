#use mysql
import mysql
import mysql.connector
cnx = mysql.connector.connect(user='username', password='PASSWORD', host='localhost', database='db')
cursor = cnx.cursor()

#inserting
# dict_of_dict contains data we want to load to table
columns = ['col1','col2',col3'] #list of column names
start_time = time.time()
for id_,(k,g) in enumerate(dict_of_dict.items()):
	if id_%100==0:
    #commit after every 100 insert
		print(id_ , str(round((time.time() - start_time)/60.,2)))
		start_time=time.time()
		cnx.commit()
	values = ','.join(['"' + str(g.get(f,'')) + '"' for f in columns])
	query='replace into %s (%s) values (%s);' %('tablename',','.join(columns),values)
	cursor.execute(query)

#fetching
cursor.execute('select col1,col2,col3,col4 from tablename where col1 in ("val1","val2");')
outList = cursor.fetchall()
#outList = {val[0]:val for valueList in outList}


