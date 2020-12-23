# CE-UY 3013 Project Template

*This file presents a description of the final project. For your submission,*
*this file must serve as the documentation of your project, how your program*
*should be used along with examples.*

This program was designed to be capable of balancing simple chemical equations with two reactants and two products. The user would simply input the reactants and the products when prompted. Note that the number of atoms should follow the element right after (even if the coefficient is 1). There should be no spaces. For example: "C2H4+O2" as reactants and "C1O2+H2O1" as products.

The program will create dictionaries of the separated elements and their number of atoms in each given compound. It then incorporates balancing functions that keep running until each side of the equation (reactants and products) have the same number of atoms of each element.
Here is an example of what would take place in the program

"Please input your reactants here:" C2H4+O2
"Please input your products here:" C1O2+H2O1

Now the program would creates two dictionaries. One for reactions that tells us that there are 2 C, 4 H, and 2O atoms. The other dictionary for products would tell us that there is 1C, 2H and 3O atoms.

The program would then compare the number of atoms between each dictionary. If the numbers are the same, the equation is already balanced. If they are not, it would check if there are more atoms on the reaction side than on the product side. If so, it would use the reactionbalance helper to equal out the elements. If there are more atoms on the product side than on the reaction side, it would use the product balance helper to equal out the elements. 

The end result would have 2 C, 4H, and 6O on both sides of the reaction. This would produce something along the lines of:
Reactants: C2H4 + 3O2
Products: 2CO2 + 2H2O

So the user would know the output is C2H4 + 3O2 -> 2CO2 + 2H2O