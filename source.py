# This file is required. Use the same name, "source.py".
# All of your *foundational* code goes here, meaning the functions and classes
# that can be used to build larger processes. For example, the class you
# created for the OOP assignment would go here.

print('Welcome to Jobe Balancer 3000. Kindly input your reactants and products below when prompted. Elements should be kept within the parenthesis and their coefficient numbers outside of the parenthesis. For example follow the format: "(X)2+(Y)5"')
print('What are your reactants? :')
reactants = input()
print('Your reactants are: '+ reactants)
print('What are your products? :')
products = input()
print('Your products are : ' + products)

print(reactants)
print(products)

finRe = []
finProd = []

def elemList (reOrProd):    #takes the reactants or products and gives back a list of reactants/products
    lst = []
    i = 0
    st = ''
    while i < len(reOrProd):
        if reOrProd[i].isalnum():
            st += reOrProd[i]
        if reOrProd[i]== '+' or i == (len(reOrProd)-1):
            lst.append(st)
            st = ''
        i+=1
    return lst

def elems (reOrProd):                #also takes reactants or products and gives back a dictionary of reactants/products and number of atoms
    dic = {}
    i = 0
    st = ''
    #for i in range(len(reactants)):
    while i < len(reOrProd):
        if reOrProd[i].isalpha():
            st += reOrProd[i]
        elif reOrProd[i].isdigit():
            dic[st] = int(reOrProd[i])
            st = ''
        i+=1
    return dic

reDict = elems(reactants)
prodDict = elems(products)
reList = elemList(reactants)
prodList = elemList(products)
print("before: ")
print(reDict)
print(prodDict)
print(reList)
print(prodList)

"""
make sure the type of letters(elements) on each side are the same
if not tell user its an invalid equation
-> if it is valid then
compare the number attributed to each element on the same side. they should ===
the same thing. eg 2 Ns in reDict you want 2 Ns on prodDict.
if everything is the same then equation is balanced and display output. If its not the same
then using common denominators/numerators find the whole number needed to multiply each side etc to give
a balanced equation
"""

def balanceHelper(reDict, prodDict, key):        #function with two functions in it to help balance equation
    print("HELPER CALLED")
    #reList
    #prodList
    s = ''
    #print ('pd + rd')
    #print (prodDict[key])
    #print(reDict[key])
# 2 Na + 2 HCl ->  2 NaCl + 1 H2
#Na + HCl -> NaCl + H2 
# {'Na': 2, 'H': 2, 'Cl': 2}
# {'Na': 2, 'Cl': 2, 'H': 2}
    def bigProd(reDict, prodDict, key):                    #helper function to ensure the chosen element (key) has the same number of atoms in reactants and products
        for x in range(len(reList)):
            if key in reList[x]:
                l= []
                k = ''
                for i in reList[x]:
                    if i.isalpha():
                        k+=i
                    else:
                        l.append(k)
                        k = ''
                print(l)
                print(reDict)
                print(key)
                print(reDict[key])
                s = str(prodDict[key]/reDict[key]) + reList[x]
                finRe.append(s)
                 #figure out where s goes in reList
                print(s) # 2* no of H
                for elem in l: 
                    if elem in reDict:
                        mul = int(prodDict[elem]/reDict[elem])
                        for item in l:
                            print('mul:')
                            print(mul)
                            if item in reDict:
                                reDict[item] = mul * reDict[item]
                                print('re')
                                print(item)
                                print(reDict[item])
                        break
        
    def bigRe(reDict, prodDict, key):                  #same as bigProd but when no of atoms in reactants > no of atoms in products
        for x in range(len(prodList)):
            if key in prodList[x]:
                l= []
                k = ''
                for i in prodList[x]:
                    if i.isalpha():
                        k+=i
                    else:
                        l.append(k)
                        k = ''
                #print(l)
                print(prodDict)
                print(reDict)
                #print(key)
                #print(prodDict[key])
            #if key in prodList[x]:
                s = str(reDict[key]/prodDict[key])+prodList[x] 
                finProd.append(s)
                print(s)
                for elem in l :
                    if elem in prodDict: #HERE
                        print("LOOK HERE")
                        print(reDict[elem])
                        print(prodDict[elem])
                        mul = int(reDict[elem]/prodDict[elem])
                        for item in l:
                            print(item)

                            print('mul:')
                            print(mul)
                            if item in prodDict:
                                prodDict[item] = mul * prodDict[item]#int(reDict[elem]/prodDict[elem])
                                print('pr')
                                print(item)
                                print(prodDict[item])
                        break
        

    if prodDict[key] > reDict[key]:                  #calls bigProd or bigRe depending on which side has more atoms of the element
        print('callin bigProd')
        print(reDict, prodDict, key)
        bigProd(reDict, prodDict, key)
        print( 'after bigProd')
        print(reDict, prodDict, key)
        if prodDict[key] < reDict[key]:
            bigRe(reDict, prodDict, key)

    if prodDict[key] < reDict[key]:
        print('callin bigRe')
        print(reDict, prodDict, key)
        bigRe(reDict, prodDict, key)
        print('after bigRe')
        print(reDict, prodDict, key)
        if prodDict[key] > reDict[key]:
            bigProd(reDict, prodDict, key)

 
def balance(reDict, prodDict):                       #first checks if equation is already balanced, if not balanced it calls the balance helper function to balance it
    balanced = False
    rkeys = sorted(list(reDict.keys()))
    pkeys = sorted(list(prodDict.keys()))
    r = sorted(list(reDict.items()))
    p = sorted(list(prodDict.items()))
    #print(rkeys)
    #print(pkeys)
    if rkeys != pkeys:
        print('You did not input the correct reactants/products. Please try again')
        return -1
    if r == p:
        print('balanced')
        balanced = True
        return 0
    else:                             
        
        for key in reDict:
        #while balanced == False:
            if reDict[key] != prodDict[key]:
                print(reDict, prodDict, key)
                balanceHelper(reDict, prodDict, key)
         
                #key = keys[i]


balance(reDict, prodDict)
print('after: ')
print(reDict)
print(prodDict)


print('Your balanced reactants are: ')
print(finRe)
print('Your balanced products are: ')
print(reList)
print(prodList)
print(finProd)
#Final Output:            
#2Na + 2HCL -> 2NaCl + H2
