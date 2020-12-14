# CE-UY 3013 Project Template

*This file presents a description of the final project. For your submission,*
*this file must serve as the documentation of your project, how your program*
*should be used along with examples.*

This program was designed to be capable of balancing simple chemical equations with two reactants and two products. The user would simply input the reactants and the products when prompted. Note that the number of atoms should follow the element right after (even if the coefficient is 1). There should be no spaces. For example: "Na1+H1Cl1" as reactants and "Na1Cl1+H2" as products.

The program will create dictionaries of the separated elements and their number of atoms in each given compound. It then incorporates balancing functions that keep running until each side of the equation (reactants and products) have the same number of atoms of each element.
Here is an example of what would take place in the program

"Please input your reactants here:" Na1+H1Cl1
"Please input your products here:" Na1Cl1+H2

Now the program would creates two dictionaries. One for reactions that tells us that there is 1 Na, 1 H, and 1Cl atom. The other dictionry for products would tell us that there is 1 Na, 1Cl and 2 H2 atoms.

The program would then compare the number of atoms between each dictionary. If the numbers are the same, the equation is already balanced. If they are not, it would check if there are more atoms on the reaction side than on the product side. If so, it would use the reactionbalance helper to equal out the elements. If there are more atoms on the product side than on the reaction side, it would use the product balance helper to equal out the elements. 

The end result would have 2 Na, 2H, and 2Cl on both sides of the reaction. This would produce something along the lines of:
Reactants: 2Na1 + 2H1Cl1
Products: 2Na1Cl1 + 1H2

So the user would know the output is 2Na + 2HCl -> 2NaCl + H2