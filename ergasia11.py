with open('askhsh11.txt', 'r') as f:
 raw_list =  f.read().split('\n')#turn my file into a list
 #open the file
 
newlist=[] #That's my big list which includes insides another lists
askhseis_choose=[] #that's my little lists which are included inside of the newlist

for i in range(len(raw_list)): #run the length of the of the list/file
   newlist.append(map(int, raw_list[i].split(','))) #i convert the strings into integers

for i in range(6): #i want my input to show 6 times
  askhseis=input("Give me 1 number (from 1-14) ") 
  askhseis_choose.append(askhseis) #append the users input into the list 

counter=0 #that's my counter

for i in range(len(newlist)): #run the length of the big list

  for j in range(len(askhseis_choose)): #run the length of the little lists

    if askhseis_choose[j] in newlist[i]: #if the elements of the little lists are inside of the big list
      counter+=1 #I increase my counter by one

      if counter == 4: #when my counter reaches the 4
        print "found a match" 
        quit() #interrupts the program

  counter=0 #and the counter goes back in 0
print "didn't find a match"

#sources:
#https://realpython.com/working-with-files-in-python/#pythons-with-open-as-pattern <--'With open/as' another method to open a file 
#https://stackoverflow.com/questions/60327954/convert-a-file-into-a-list-with-integers 
#<-- i made this question in stack overflow because when i turn the file into a list, the objects were strings and i wanted to be integers
#https://stackoverflow.com/questions/73663/terminating-a-python-script?fbclid=IwAR1OAFknwD4hxRLH-Vk2m1yhbdsWRKJ-UsMOTlpStBnwlKpp0Ymvnq309hU <-- About the quit() function
