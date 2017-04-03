print ("This is a simple calculator.")
print ("The calc. will be do A (+,-,*,/) B")
count = 0
while (count < 50):
    a = int(input('Input A :'))
    b = int(input('Input B :'))
    c = input('Input + - * / :')
    
    if c == '+' :
      d = a + b
    elif c == '-' :
      d = a - b
    elif c == '*' :
      d = a * b
    elif c == '/' :
      d = a / b
    else :
      print ('Error try again !')
    
    print (d)
