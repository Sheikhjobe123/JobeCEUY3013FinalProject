# This file is required. Use the same name, "source.py".
# All of your *foundational* code goes here, meaning the functions and classes
# that can be used to build larger processes. For example, the class you
# created for the OOP assignment would go here.

    print('Welcome to Jobe Balancer 3000. Kindly input your reactants and products below when prompted. Element coefficients should be added right after and there should be no spaces anywhere. For example follow the format: "C2H4+O2"')
    print('What are your reactants? :') #the user can input their reactants as C2H4+O2 (this is C2H4 and O2)
    reactants = input()
    print('Your reactants are: '+ reactants) #prints out inputted reactants
    print('What are your products? :') #the user inputs their products as C1O2 + H2O1 (this is CO2 and H2O)
    products = input()
    print('Your products are : ' + products) #prints out inputted products



    finRe = []
    finProd = []

    def elemList (reOrProd):    #a function that takes the given reactants or products and gives back a list of reactants/products
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

    def elems (reOrProd):                #a function that takes the given reactants or products and gives back a dictionary of reactants/products and number of atoms
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

    reDict = elems(reactants) #this is the reactant dictionary that should look like {'C': 2, 'H': 4, 'O': 2}
    prodDict = elems(products) #this is the products dictionary that should look like {'C': 1, 'O': 1, 'H': 2}
    reList = elemList(reactants) #created list -> ['C2H4', 'O2']
    prodList = elemList(products) # created list -> ['C1O2', 'H2O1']

    """
    make sure the type of letters(elements) on each side are the same
    if not tell user its an invalid equation
    -> if it is valid then
    compare the number attributed to each element on the same side. they should ===
    the same thing. eg if there are 2 Cs in reDict you want 2 Cs on prodDict.
    if everything is the same then equation is balanced and display output. If its not the same
    then using common denominators/numerators find the whole number needed to multiply each side etc to give
    a balanced equation
    """

    def balanceHelper(reDict, prodDict, key):        #function with two functions in it to help balance equation
        print("HELPER CALLED")                       #
        #reList
        #prodList
        s = ''
        #print ('pd + rd')
        #print (prodDict[key])
        #print(reDict[key])
    # 1 C2H4 + 3 O2 ->  2 CO2 + 2 H2O
    #C2H4 + O2 -> CO2 + H2O 
    # {'C': 2, 'H': 4, 'O': 6}
    # {'C': 2, 'H': 4, 'O': 6}
        def bigProd(reDict, prodDict, key):     #helper function to ensure the chosen element (key) has the same number of atoms in reactants and products

            for x in range(len(reList)):         #this function is called when the product elements have more atoms than the reactant elements
                if key in reList[x]:
                    l= []
                    k = ''
                    for i in reList[x]:
                        if i.isalpha():
                            k+=i
                        else:
                            l.append(k)
                            k = ''
                    
                    s = str(prodDict[key]/reDict[key]) + reList[x]
                    finRe.append(s)
                    
                    for elem in l: 
                        if elem in reDict:
                            mul = int(prodDict[elem]/reDict[elem])
                            for item in l:
                                
                                if item in reDict:
                                    reDict[item] = mul * reDict[item]
                                    
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
                    
                    #print(prodDict[key])
                #if key in prodList[x]:
                    s = str(reDict[key]/prodDict[key])+prodList[x] 
                    finProd.append(s)
                    
                    for elem in l :
                        if elem in prodDict: #HERE
                            print("LOOK HERE")
                            print(reDict[elem])
                            print(prodDict[elem])
                            mul = int(reDict[elem]/prodDict[elem])
                            for item in l:
                            
                                if item in prodDict:
                                    prodDict[item] = mul * prodDict[item]#int(reDict[elem]/prodDict[elem])
                                
                            break
            

        if prodDict[key] > reDict[key]:                  #calls bigProd or bigRe depending on which side has more atoms of the element
            
            bigProd(reDict, prodDict, key)
            
            if prodDict[key] < reDict[key]:
                bigRe(reDict, prodDict, key)

        if prodDict[key] < reDict[key]:
        
            bigRe(reDict, prodDict, key)
        
            if prodDict[key] > reDict[key]:
                bigProd(reDict, prodDict, key)

    
    def balance(reDict, prodDict):                       #first checks if equation is already balanced, if not balanced it calls the balance helper function to balance it
        balanced = False
        rkeys = sorted(list(reDict.keys()))
        pkeys = sorted(list(prodDict.keys())) #gets the keys in each dictionary
        r = sorted(list(reDict.items()))
        p = sorted(list(prodDict.items()))
        #print(rkeys)
        #print(pkeys)
        if rkeys != pkeys:
            print('You did not input the correct reactants/products. Please try again') #tells you that the equation the user input does not have matching elements on each side
            return -1
        if r == p:
            print('balanced')
            balanced = True
            return 0
        else:                             
            
            for key in reDict:
            #while balanced == False:
                if reDict[key] != prodDict[key]:
                    
                    balanceHelper(reDict, prodDict, key)
            
                    #key = keys[i]


    balance(reDict, prodDict)

    """A= np.array([[1,0,-2,0],

                [1,4,-4,-1],

                [1,2,0,-2],    #tried using arrays to solve it but this couldn't be generalised to different equations and didn't work

                [0,1,-1,0]])

    b= np.array([1,1,1,1])

    c = np.linalg.solve(A,b)
    print(c) """

    print('Your balanced reactants are: ')
    print(finRe)
    print('Your balanced products are: ')

    print(finProd)
    print("{} -> {}".format(finRe, finProd)) #prints out the final balanced equation eg shown below
    #Final Output of what it should be:            
    #C2H4 + 3O2 -> 2CO2 + 2H2O

    #but it only prints out
    # 2O2 -> 2CO2 + 2H2O implying only the products were balanced and issues were faced in balancing the reactants..