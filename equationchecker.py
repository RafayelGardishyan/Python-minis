print ('Choose the equation')
print ('c1 = a > b')
print ('c2 = a < b')
e = input()

if e == 'c1':
  print ('The equation is a > b')
  print ('Input a')
  a = input()
  print ('Input b')
  b = input()
  if a > b :
    print ('Success! :)')
  else :
    print ('Try Again :(')
elif e == 'c2':
  print ('The equation is a < b')
  print ('Input a')
  a = input()
  print ('Input b')
  b = input()
  if a < b :
    print ('Success! :)')
  else :
    print ('Try Again :(')  
