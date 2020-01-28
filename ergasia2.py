def Bad_Words(fin):     #create a function and for parameters i put the file
    bad_letters = fin.read().replace(' ','\n').replace('(','').replace(')','').replace(',', '\n').splitlines()
    #assign the file into bad_letters (the name of the list) and i put the replace method in some symbols
    Bad_Letters=["f","c","k","r","F","C","K","R"]    #create another list with my bad consonants
    sum_Good=0  #thats my counter for the good vowels/consonants
    for i in range(len(bad_letters)):   #create a loop for the file/list
        sum_Bad=0   #thats my counter for my bad consonants
        for j in range(len(Bad_Letters)):   #thats my second loop for the my second list
            if Bad_Letters[j] in bad_letters[i]:    #if the elements of the list with the bad consonants are inside the elements of the file/list  
                      sum_Bad=sum_Bad+1 #add by 1
                                 
        sum_Good=len(bad_letters[i])-sum_Bad    #now i subtract the elements lenght of file/list with bad consonants counter   
        if sum_Bad>=sum_Good:   #if the bad consonants are more or equals the subtraction
          print bad_letters[i],"Hey!Watch your mouth!"
        else:
          print bad_letters[i],"Hey!Thats good!"

fin = open("Askhsh2.txt", "w+")     #create a file (not external)
fin.write("fUCK\nfuCk\nlOVe\nFUUUCK\n(fuck)\n fuCCCckk\nFIfa\nf$ck\nf!ck it\nF4cKin\nf!!!cr,FIsh")  #wrote some words 
fin.close() #close the file 

fin = open("Askhsh2.txt", "r+")  #we open the file with the read methhod
char1 = fin.read(1)     #get the first character
while True:     #check the elements of the file with a loop
  if not char1:     #if it don't find the first character
    print "Your file is empty, please write something!"  
    fin.close()     #we close the file
    break   #stops the flow of the loop
  else:
    fin = open("Askhsh2.txt", "r")  #open again the file with the read method
    Bad_Words(fin)  #call the Bad_Words(fin)function
    fin.close()  #we close the file again
    break   #stops the flow of the loop

#sources:
#https://stackoverflow.com/questions/14271216/beginner-python-reading-and-writing-to-the-same-file <-- How to write and read a file
#https://www.youtube.com/watch?v=walXPsausPI <--This is a video of how to create a text file in python
#https://stackoverflow.com/questions/2507808/how-to-check-whether-a-file-is-empty-or-not <--How to check a file is empty
#http://ebooks.edu.gr/modules/document/file.php/DSEPAL
#-C219/%CE%94%CE%B9%CE%B4%CE%B1%CE%BA%CF%84%CE%B9%CE%BA%CF%8C%20%CE%A0%CE%B1%CE%BA%CE%AD%CF%84%CE%BF/
#%CE%A3%CE%B7%CE%BC%CE%B5%CE%B9%CF%8E%CF%83%CE%B5%CE%B9%CF%82%20%CE%9C%CE%B1%CE%B8%CE%B7%CF%84%CE%AE/24-0601-01_
#Programmatismos-Ypologiston_G-EPAL_Simeioseis-Mathiti.pdf <--eleghos orthothtas, eisagwgh ston programmatismo, vivlio epal,page 54
#https://stackoverflow.com/questions/3925614/how-do-you-read-a-file-into-a-list-in-python/3925701
#https://www.w3schools.com/python/ref_list_count.asp <--Count the list

