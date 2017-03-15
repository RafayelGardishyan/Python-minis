print ("This is a simple calculator.")
count = 0
while (count < 5):
    a = int(input('Input A :'))
    b = int(input('Input B :'))
    c = input('Input + - * / :')
    
    if c == '+' :
      d = a + b
    elif c == '-' :
      d = a - b
    elif c == '*' :
      d = a * b
    else :
      d = a / b
    
    print (d)
    count = count + 1
