#######################################################################################################
## Program Name: db.py
## Author: Firoz Hossain Chaudhuri
## Date: 05/19/2019
## Description: This Program will pre-process csv files to load into Postgres SQL Server
##
#######################################################################################################


import csv
import shutil
import datetime
import psycopg2
import re
import filecopy


# This function will read the csv file and extract the header
def readheader(filename, delim):
	
	try:

		if delim =="t":
			delim = '\t'

		file = open(filename, 'r')

		csv_reader = csv.reader(file, delimiter=delim, quoting=csv.QUOTE_MINIMAL)
	
		headers = next(csv_reader, None)

		pattern = r'/([a-zA-Z0-9_-]*)\.(.*)'

		match = re.search(pattern,filename)

		if match:
			fname = match.group(1)

		sql_head = "create table "+ fname +" ("

		sql_body = " varchar,".join(headers) +" varchar"

		sql_stmt = sql_head + sql_body + " )"

		return (sql_stmt, filename, delim)


	except Exception as e:
		print("Error in Reading File "+ filename +" "+str(e))


def db_conn(create_table_sql, filename, delimiter):

	try:
		print(delimiter)
		pattern = r'/([a-zA-Z0-9_-]*)\.(.*)'
		match = re.search(pattern,filename)
		if match:
			fname = match.group(1)

		connection = psycopg2.connect(user = "postgres", password = "1234", host = "127.0.0.1", port = "5432", database = "postgres")
		cursor = connection.cursor()
		cursor.execute(create_table_sql)
	
		print("\nTable "+fname+" Created Successfully!")

		select_sql = "Select * from "+fname+" limit 10"

		cursor.execute(select_sql)

		c = cursor.fetchall()

		print(c)
		

		copy_sql = "COPY "+ fname+ " FROM '"+ filename+ "' DELIMITER E'"+ delimiter+"'"+ "CSV HEADER QUOTE E'\\^' ESCAPE E'\\^' ENCODING 'LATIN1' ;"
		print('\n'+copy_sql)

		cursor.execute(copy_sql)


		connection.commit()
		
		select_sql = "Select * from "+fname+" limit 10"

		cursor.execute(select_sql)

		c = cursor.fetchall()

		print(c)

	except (Exception, psycopg2.Error) as error :
		print ("Error while connecting to PostgreSQL", error)
	finally:#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")



def main():

	print("Please Enter the File Name: ")

	filename = str(input().strip())

	print("Please Enter the File Delimiter: ")

	delim = str(input().strip())

	file_name = filecopy.file_ops(filename) + filename

	tup = readheader(file_name, delim)

	print(tup)

	db_conn(tup[0],tup[1],tup[2])
	




if __name__=="__main__":
	main()