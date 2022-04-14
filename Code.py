print('Hello')
ans=input('Are you ready to play (yes/no):')
score=0
total_q=4
if ans.lower() == 'yes':
    ans=input('1. What is the best programming language ?')
    if ans.lower() == 'python':
        score+=1 
        print('correct')
    else :
        print('incorrect')
    ans=input('2. What is 2+8+9-1 ?')
    if ans == '18':
        score+=1 
        print('correct')
    else :
        print('incorrect')
    ans=input('3. What is the better 1050ti or a 1060 (graphics card) ?')
    if ans.lower() == '1050ti':
        score+=1 
        print('correct')
    else :
        print('incorrect')
    ans=input('4. Who came second in the stanely cup finals ?')
    if ans.lower() == 'nights' or ans.lower() == 'vegas':
        score+=1 
        print('correct')
    else :
        print('incorrect')
print('Thank you for playing ,you got',score,"question correct.")
mark=(score/total_q)*100 
print("Mark:",mark)
print('Goodbye')
