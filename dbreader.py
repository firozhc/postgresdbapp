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


# This function will read the csv file and extract the header
def readheader(filename, delim):
	
	try:

		out_dir = '/users/firoz/desktop/outfile.csv'
		
		file = open(filename, 'r')

		delim = '\t'

		csv_reader = csv.reader(file, delimiter=delim, quoting=csv.QUOTE_MINIMAL)
	
		headers = next(csv_reader, None)

		sql_head = "create table "+ filename +" ("

		sql_body = " varchar,".join(headers) +" varchar"

		sql_stmt = sql_head + sql_body + " )"

		print(sql_stmt)


	except Exception as e:
		print("Error in Reading File "+ filename + str(e))




def main():

	print("Please Enter the File Name: ")

	filename = input()

	print("Please Enter the File Delimiter: ")

	#delim = str(input().strip())

	#print(delim)

	readheader(filename, 'tab')
	




if __name__=="__main__":
	main()