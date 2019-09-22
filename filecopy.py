#######################################################################################################
## Program Name: db.py
## Author: Firoz Hossain Chaudhuri
## Date: 05/19/2019
## Description: This Module will pre-process csv files to load into Postgres SQL Server
##
#######################################################################################################


import csv
import shutil
import datetime



# This function will read the csv file
def readfile(filename, delim):
	
	try:

		out_dir = '/users/firoz/desktop/outfile.csv'

		file = open(filename, '+r', encoding = "ISO-8859-1")
		print(delim)
		csv_f = csv.reader(file, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
		outfile = open(out_dir, '+w')
		csv_w = csv.writer(outfile)


		start_time = datetime.datetime.now()

		for row in csv_f:
			try:
				csv_w.writerow(row)
					
			except Exception as e:
				print("Error in Reading Row "+row+"\n" + e)

		print("Execution Time: "+ str(datetime.datetime.now() - start_time))

	except Exception as e:
		print("Error in Reading File "+ filename + e)


def file_ops(filename):

	copy_to_dir = '/tmp/'
	
	copy_from_dir = '/users/firoz/downloads/' + str(filename)

	try:
		shutil.copy2(copy_from_dir, copy_to_dir) # target filename is /dst/dir/file.ext
		print("File"+" "+filename+" was successfully copied to /tmp ..")

		return copy_to_dir


		#readfile(copy_from_dir, delim)

	except Exception as e:
		print("Error in Copy File for "+filename + e)


"""

def main():

	print("Please Enter the File Name: ")

	filename = input()

	#print("Please Enter the File Delimiter: ")

	#delim = str(input().strip())

	file_ops(filename)

	



if __name__=="__main__":
	main()

"""