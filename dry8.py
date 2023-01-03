'''fr = open('TextData.txt' , 'r') 		
fw = open('NewFile.txt', 'w')   		
fw.write(fr.read())
fr.close()					
fw.close()				
fr1 = open('NewFile.txt', 'r+')
print(fr1.read(12))				# read and print the first 12 characters
print(fr1.tell())				# Print the read cursor position( position is 0 based)
print(fr1.write("this is the new text"))		# Write some text (length 20). This is always written at the end
print(fr1.seek(12))				# Position the cursor at 12
print(fr1.read(1))				# Read and print the next character (at cursor position 12)
print(fr1.seek(15))				# Position the cursor at 15
print(fr1.read(10))				# Read and print 10 characters from this position
print(fr1.read())		# read() always reads the entire file irrespective of cursor position and changes the cursor position to the end
fr1.close()'''


import pickle
animalDict = { 'Cat': 2, 'Dog': 7, 'Lion': 4, 'Tiger': 9, 'Leopard': 11, 'Bear': 8, 'Elephant': 15 }
outfile = open('animals','wb')
pickle.dump(animalDict, outfile)
outfile.close()
fst = open("animals", 'rb')				
data = pickle.load(fst)			         
try:					
  while(True):
    print(data)
    data = pickle.load(fst)
except:
  print("Bye")
