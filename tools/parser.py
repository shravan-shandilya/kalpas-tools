import sys

if len(sys.argv) == 2:
	file = sys.argv[1]
log = open("malformed_data.txt","w+")	

text_file = open(file,"r")
num = 0
warnings = 0
errors = 0
success = 0

for line in text_file.readlines():
	num += 1
	try:
		segments = line.split(",")
		len_seg = len(segments)
		if len_seg not in [6,7]:
			log.write("ERROR:: Malformed data in line #"+str(num)+"::Segment length:"+str(len_seg)+"::Line contents::"+line+"\n")
			errors += 1
		name = segments[0].replace(" ","")
		ingredients = segments[1].replace(" ","")
		karmas = segments[2].replace(" ","")
		anupana = segments[3].replace(" ","")
		if len(segments) == 6:
			log.write("WARNING:: Assuming 'adhikara' as nil for line#"+str(num)+" as there are only "+str(len_seg)+"segments \n\n Line Contents::"+line+"\n")
			adhikara = ""
			warnings += 1
		else:
			adhikara = segments[4].replace(" ","")
			success += 1
		
	except IndexError:
		log.write("INDEX_ERROR:: Line #"+str(num)+"\n Line Contents:"+line)
		errors += 1
print "Results: \nSuccesfully parsed %d entries\nEncountered %d warnings and %d errors.\nWrote warnings and errors to 'malformed_data.txt'"%(success,warnings,errors)		
