def largest_word(fin): #We create a function
    split_sentence = fin.split(' ') #it creates a list which includes the file 
    largest_word = ''#the longest length of a word 
    split_sentence.sort(key=len) #it sorts the list
    split_sentence.reverse() #prints the list
    
    for i in range(len(split_sentence)): #it runs the length of the list
      if len(split_sentence[i]) > len(largest_word): #compares the length of the elements throught the list
        largest_word = split_sentence[i]#assigns the longest word in the empty value 'largest_word'
        
    for i in range(0,5):#We create a loop from the first element
     try:#its like the if attribute
        word = split_sentence[i].replace('a','').replace('e','').replace('i','').replace('o','').replace('u','').replace('y','').replace('A','').replace('E','').replace('I','').replace('O','').replace('U','').replace('Y','')#We used the .replace() attribute to replace the vowels with null
        print word[::-1]#We reverse the string
     except:
        print "Your file is empty, please write something!"#in case the file is empty
     else:
        pass#I want just carry on the program even when are not written 5 or more words 
    
fin=open('Askhsh1.txt' ,'r').read()#we open the file,way access is read 
fin = fin.replace('\n',' ').replace(',','').replace('.','').replace('(','').replace(')','')#inside the file replaces the line change into space and the comma, dot and parenthesis into null 
largest_word(fin)#calls the largest_word(fin) function

#Phges:
#https://stackoverflow.com/questions/1192881/how-to-find-the-longest-word-with-python <-- For the def()function
#https://stackoverflow.com/questions/6116978/how-to-replace-multiple-substrings-of-a-string <-- For the split() attribute 
#https://thispointer.com/python-how-to-sort-a-list-of-strings-list-sort-tutorial-examples/ <-- For the list sort
#https://stackoverflow.com/questions/14532875/creating-for-loop-until-list-length <-- For the second loop
#https://stackoverflow.com/questions/6116978/how-to-replace-multiple-substrings-of-a-string <-- For the replace() attribute
#https://www.w3schools.com/python/python_howto_reverse_string.asp <-- How to reverse a string
#https://www.w3schools.com/python/python_try_except.asp <-- For the Try/Except/else method
