a = {"milk": 1.20,
     "yogurt": 1.00, 
     "cornflakes": 2.20,
     "chips": 1.80}#That's my dictionary

shopping_list=[]#That's an empty list of the user

proionta=raw_input("Write the products that you want to buy (one by one) ")
#Ask the user what does he/she want to buy
athroisths=0 #Thats my adder

def Ypologismos(athroisths):
#Thats my function, calculates the sum with the tax    
    tax = 0.24
    synolo = athroisths*tax+athroisths
    synolo = round(synolo,2)#Make a float number a round
    return synolo

while proionta != "":#As the user doesn't give null/enter
    
    if proionta in a.keys():
    #if the user wrote one of the products of the dictionary
        athroisths+=a[proionta]#the sum of the products
        print "Added to your shopping list!"
        shopping_list.append(proionta)#adds the product to the shopping list
        shopping_list.append(a[proionta])#adds the value of the product
        print shopping_list
    else:#if the user didn't write one of the products that included the dictionary
        print "We can't find the product that you are looking for, please try again!"
    proionta=raw_input("Write the products that you want to buy per one (if you finished, press enter) ")

print "The total of your products is", Ypologismos(athroisths), "€"
#calls the Ypologismos(athroisths) function

#sources:
#https://www.w3schools.com/python/python_dictionaries.asp <-- How to create a dictionary
#https://www.tutorialgateway.org/python-program-to-check-if-a-given-key-exists-in-a-dictionary/ <-- Check if an input exist in a dictionary
#https://www.w3schools.com/python/ref_func_round.asp <-- Make a float number a round

