#!/usr/local/bin/python
import sys

if len(sys.argv) == 2:
	file = sys.argv[1]
log = open("malformed_data.txt","w+")	

text_file = open(file,"r")
parsed_data = open("parsed_data.csv","w+")
num = 0
warnings = 0
errors = 0
success = 0
parsed_data.write("name,ingredients,karmas,indications,anupana,adhikara\n")
for line in text_file.readlines():
	num += 1
	try:
		segments = line.split(",")
		len_seg = len(segments)
		if len_seg == 6:
			log.write("ERROR:: Malformed data in line #"+str(num)+"::Segment length:"+str(len_seg)+"::Line contents::"+line+"\n")
			errors += 1
		
		name = segments[1].replace(" ","")
		ingredients = segments[2].replace(" ","")
		karmas = "_"+segments[3].replace(" ","")+"_"
		indications = "_"+segments[4].replace(" ","")+"_"
		anupana = segments[5].replace(" ","")
		adhikara = segments[6].rstrip().replace(" ","")
		if len_seg == 8:
			print num
		parsed_data.write(name.lower()+","+ingredients.lower()+","+karmas.lower()+","+indications.lower()+","+anupana.lower()+","+adhikara.lower()+"\n")
	except IndexError:
		log.write("INDEX_ERROR:: Line #"+str(num)+"\n Line Contents:"+line)
		errors += 1
print "Results: \nSuccesfully parsed %d entries\nEncountered %d warnings and %d errors.\nWrote warnings and errors to 'malformed_data.txt'"%(success,warnings,errors)		
