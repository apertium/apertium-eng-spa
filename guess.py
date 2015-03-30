
import os,sys,subprocess

analysed = open(sys.argv[1],'r')
#guessed = open(sys.argv[2],'w+')
#f1 = open('/tmp/tt','w+')

for line in analysed :
	unk = []
	temp = line.split()

	for word in temp:
		#word = word.strip()
		if '/*' in word:
			unk.append(word)
#			f1.write(word)
#			f1.write("\n")
	for unks in unk:
		pos = unks.find('*')
		pos2 = unks.find('$')
		tok = unks[pos+1:pos2]
#		print tok

		inp = subprocess.Popen(['echo', tok],stdout=subprocess.PIPE)
		out = subprocess.Popen(['lt-proc','es-noun-guess.bin'],stdin=inp.stdout,stdout=subprocess.PIPE)
		#NOTE: multiwords will fail/propogate-error from the below line
		guess = out.stdout.read().strip()
		#print out.stdout.read()

		line = line.replace(unks,guess)
	print line,
#f1.close()
analysed.close()	
