
# ORGANIC CHEMISTRY QUIZ IS PYTHON

print ('Welcome to the first pharmaceutical organic chemistry 1 mini quiz!')

score = 0

# Question 1 : 

answer = int(input("What is heterolytic fission?  "
" 1. unequal bond breaking "
"2. equal bond breaking "
"3. unequal nuclear seperation."
" answer =  "))

if answer == 1:
    print("correct!")
    score += 10
else:
    print("EERRRRRRRGGGGGG! WRONG U IDIOT")


# Question 2 : 

answer = int(input("What is homolytic fission?  "
" 1. unequal bond breaking "
"2. equal bond breaking "
"3. homolysis of the nucleus to form a homogenous solution. "
" answer =  "))

if answer == 2:
    print("correct!")
    score += 10
else:
    print("EERRRRRRRGGGGGG! WRONG U IDIOT")


# Question 3 : 

answer = int(input("The greater the number of resonating structures for a molecule ...  "
" 1. the greater the stability"
"2. the greater the viscosity"
"3. the lower the latent heat of vaporisation. "
" answer =  "))

if answer == 1:
    print("correct!")
    score += 10
else:
    print("EERRRRRRRGGGGGG! WRONG U IDIOT")


# Question 4 : 
answer = int(input("What is the type of hybridization in ethene?  "
" 1. sp2d2 "
"2. sp2 "
"3. sp3.  "
" answer =  "))

if answer == 2:
    print("correct!")
    score += 10
else:
    print("EERRRRRRRGGGGGG! WRONG U IDIOT")


# Question 5 : 

answer = int(input("What is the disctintive characteristic of alkanes?  "
" 1. they containe a triple bond "
"2. they are saturated hydrocarbons "
"3. they are unsaturated hydrocarbons. "
" answer =  "))

if answer == 2:
    print("correct!")
    score += 10
else:
    print("EERRRRRRRGGGGGG! WRONG U IDIOT")


# Question 6 : 

answer = int(input(" What makes a compound aromatic? "
" 1. cylic, reversed, inferior, pi electrons = 9n/3 "
"2. cyclic, conjugated, dynamic, pi electrons = 2n+1"
"3. cyclic, conjugated, flat, pi electrons = 4n+2. "
" answer =  "))

if answer == 3:
    print("correct!")
    score += 10
else:
    print("EERRRRRRRGGGGGG! WRONG U IDIOT")


# Question 7 : 

answer = int(input("Which compound is anti-aromatic?  "
" 1. cyclooctatetraene "
"2. benzene "
"3. cyclobutadiene.  "
" answer =  "))

if answer == 3:
    print("correct!")
    score += 10
else:
    print("EERRRRRRRGGGGGG! WRONG U IDIOT")



# Question 8 : 


answer = int(input("A nucleophile is ... charged."
" 1. positively "
"2. negatively"
"3. zero. "
" answer =  "))

if answer == 2:
    print("correct!")
    score += 10
else:
    print("EERRRRRRRGGGGGG! WRONG U IDIOT")




# Question 9 : 


answer = int(input("Select a valid process for direct Electrophillic aromatic substitution on benzene (EAS): "
" 1. Friedel-Crafts Acylation "
"2. mayer's oxygenation"
"3. zeus's alkylation.   "
" answer =  "))

if answer == 1:
    print("correct!")
    score += 10
else:
    print("EERRRRRRRGGGGGG! WRONG U IDIOT")




# Question 10 : 


answer = int(input("Select the correct defintion for an Electrophile: "
" 1. negatively charges, repels electrons"
"2. positively charges, attracted to positive charges "
"3. an electron beam used in spectroscopy for minimizing repulsion. "
"answer =  "))

if answer == 2:
    print("correct!")
    score += 10
else:
    print("EERRRRRRRGGGGGG! WRONG U IDIOT")


print(f"Congrats! you finished the quiz with a score of {score}!")

if score >= 50:
    print("You passed!")
else:
    print("you failed, my guy that's level 1... good luck next time")
    
