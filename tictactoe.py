a = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

print("---------") 

for i in range(0,3):
    
  print('\n|',a[i][0],a[i][1],a[i][2],'|')
  
print("\n---------")



o ='X'
k = 0
nx = 0
ny = 0

while(k == 0):
    
  if a[0][0] != " "and  a[0][1] != " " and  a[0][2] != " " and  a[1][0] != " " and a[1][1] != " " and a[1][2] != " " and a[2][0] != " " and a[2][1] != " "and  a[2][2] != " ":
      
    print("Draw")
    break
  if(a[0][0] == a[0][1] ==a[0][2]   == 'X' or a[0][0] == a[1][1] == a[2][2] == 'X' or a[0][0] == a[1][0] == a[2][0] == 'X'or a[1][1] == a[0][0] == a[2][0] == 'X'or a[2][2] == a[2][1] == a[2][0] == 'X'or a[1][0] == a[1][1] == a[1][2] == 'X'or a[0][2] == a[1][2] == a[2][2] == 'X'or a[2][1] == a[0][1] == a[1][1] == 'X') :
        print("X wins") 
        break  


  elif (a[0][0] ==a[0][1] ==a[0][2]   == 'O' or a[0][0] == a[1][1] == a[2][2] == 'O' or a[0][0] == a[1][0] == a[2][0] == 'O'or a[1][1] == a[0][0] == a[2][0] == 'O'or a[2][2] == a[2][1] == a[2][0] == 'O'or a[1][0] == a[1][1] == a[1][2] == 'O'or a[0][2] == a[1][2] == a[2][2] == 'O'or a[2][1] == a[0][1] == a[1][1] == 'O') :    
    print("O wins")
    break
  

      

  x,y = input("Enter the coordinates: ").split()
  x = int(x)
  y = int(y)
  if x <=3 and x>= 1 and y <= 3 and y>=1:
    if a[x-1][abs(y-3)] != ' ' :
      print("This cell is occupied! Choose another one!")
      continue
    else :
       
      a[x-1][abs(y-3)] = o
      if o == 'X' :
           o = '0'
           nx += 1  
      else :
            o = 'X'
            ny += 1   
       
     # break
  elif x >=3 and x<= 1 or y >= 3 or y<=1:
    print("Coordinates should be from 1 to 3!")
    continue
  else :
    print("You should enter numbers!") 
    continue

    
  print("---------") 
  for i in range(0,3):
  
    print('\n|',a[ i ][ 0 ],a[i][1],a[i][2],'|')
  print("\n---------") 

