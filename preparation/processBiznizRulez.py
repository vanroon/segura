import csv
#import MySQLdb

#files and databases
fname = '/home/evroon/stack/SEGURA/BiznizRulez2.txt'
fileName = '/home/evroon/Development/segura/docker/init_config/provision/segura_provision_bizniz_rulez.sql'
rulez_dict = {}

#read all lines and add to dict
def process_bizniz_rulez():

	#load all lines in list
	with open(fname) as f:
		content = f.readlines()

	for line in content:
		if line[0] != '#' and line.strip():
			line_list = line.rstrip().split('\t')
			rulez_dict[line_list[0]] = line_list[1]
	return rulez_dict

#for each entey create  query toninsert it
def createInsertQuery(dict):
	qry = "INSERT INTO public.tbl_bizniz_rulez (categorycode, categorycodedescription) VALUES"
	counter = 0
	for key in dict:
		counter += 1
		if counter != len(dict):
			qry_row = "('%s', '%s'),\n" % (key, dict[key])
		else:
			qry_row = "('%s', '%s')" % (key, dict[key])
		qry += qry_row
	return qry

def createFile(fileName):
    f = open(fileName, 'w')
    f.close()

def writeQueryToFile(qry, fileName):
    with open(fileName, 'w') as f:
        f.write(qry)
        f.close

def main():
	dictionary = process_bizniz_rulez()
	qry = createInsertQuery(dictionary)
	createFile(fileName)
	writeQueryToFile(qry, fileName)

main()
