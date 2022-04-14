print('Hello')
A=input('Are you ready to play (yes/no):')
score=0
total_q=4
if A == 'yes':
    print('All the best for this Quiz')
    A=input('1. Python is a programming language or not ?')
    if A == 'yes':
        score+=1 
        print('correct')
    else :
        print('incorrect')
    A=input('2. What is 2+8+9-1 ?')
    if A == '18':
        score+=1 
        print('correct')
    else :
        print('incorrect')
    A=input('3. How many operators are in Python ?')
    if A == '3':
        score+=1 
        print('correct')
    else :
        print('incorrect')
    A=input('4. Which oprator have higher precedence in Python?')
    if A == 'arithmetic operator':
        score+=1 
        print('correct')
    else :
        print('incorrect')
print('Thank you for playing ,you got',score,"question correct.")
marks=(score/total_q)*100 
print("Marks:",marks)
print('Goodbye')
