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

def elemList (reOrProd):
    lst = []
    i = 0
    st = ''
    while i < len(reOrProd):
        if reOrProd[i].isalnum():
            st += reOrProd[i]
            print(st)
        if reOrProd[i]== '+' or i == (len(reOrProd)-1):
            print ('APPEND!')
            lst.append(st)
            st = ''
        i+=1
    return lst

def elems (reOrProd):
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

def balanceHelper(reDict, prodDict, key):
    print("HELPER CALLED")
    #reList
    #prodList
    s = ''
    print ('pd + rd')
    print (prodDict[key])
    print(reDict[key])
# 2 Na + 2 HCl ->  2 NaCl + 1 H2
#Na + HCl -> NaCl + H2 
# {'Na': 2, 'H': 2, 'Cl': 2}
#{'Na': 2, 'Cl': 2, 'H': 2}
    if prodDict[key] > reDict[key]:
        for x in range(len(reList)):
            if key in reList[x]:
                s = str(prodDict[key]/reDict[key]) + reList[x] #figure out where s goes in reList
                print(s) # 2* no of H
                for elem in reList[x]: 
                    if elem in reDict:
                        reDict[elem] = (prodDict[elem]/reDict[elem])
                        print('re')
                        print(elem)
                        print(reDict[elem])
                        #break
        
    elif prodDict[key] < reDict[key]:
        for x in range(len(prodList)):
            if key in prodList[x]:
                s = str(reDict[key]/prodDict[key])+prodList[x] #figure out where s goes in prodList
                print(s)
                for elem in prodList[x] :
                    if elem in prodDict:
                        prodDict[elem] = (reDict[elem]/prodDict[elem])
                        print('pr')
                        print(elem)
                        print(prodDict[elem])
                        #break
 
def balance(reDict, prodDict):
    balanced = False
    rkeys = sorted(list(reDict.keys()))
    pkeys = sorted(list(prodDict.keys()))
    r = sorted(list(reDict.items()))
    p = sorted(list(prodDict.items()))
    print(rkeys)
    print(pkeys)
    if rkeys != pkeys:
        print('You did not input the correct reactants/products. Please try again')
        return -1
    if r == p:
        print('balanced')
        balanced = True
        return 0
    else:
        """
        for key in reDict:
        #while balanced == False:
            if reDict[key] != prodDict[key]:
                balanceHelper(reDict, prodDict, key)
        """
        keys = list(reDict.keys())
        print('keys:')
        print(keys)
        i = 0
        key = keys[i]
        while balanced == False and (i < len(keys)):
            print('ke')
            print(key)
            balanceHelper(reDict, prodDict, key)
            if reDict[key] == prodDict[key]:
                key = keys[i]
            else:
                i +=1
                #key = keys[i]


#balance(reDict, prodDict)
print('after: ')
print(reDict)
print(prodDict)


#figure out a way to keep calling balance helper till eqn is balanced
#deal with floating pt stuff

print('Your balanced reactants are: ')
print('Your balanced products are: ')
print(reList)
print(prodList)
            

