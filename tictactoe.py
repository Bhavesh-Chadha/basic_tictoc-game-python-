print("Enter a name for the X player:")
name1= input()
print("\nEnter a name for the Y player e r:")
name2= input()
print("Game Start:")

a = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

print("---------") 

for i in range(0,3):
    
  print('\n|',a[i][0],a[i][1],a[i][2],'|')
  
print("\n---------")
print("Who plays first?",name1,"or", name2)

input_name= input()
if (input_name != name1 and input_name != name2):
    print(input_name,"is not a registered player")

o ='row'
k = 0
nrow = 0
ncolumn   = 0

while(k == 0):
    
  if a[0][0] != " "and  a[0][1] != " " and  a[0][2] != " " and  a[1][0] != " " and a[1][1] != " " and a[1][2] != " " and a[2][0] != " " and a[2][1] != " "and  a[2][2] != " ":
      
    print("Draw")
    break
  if(a[0][0] == a[0][1] ==a[0][2]   == 'row' or a[0][0] == a[1][1] == a[2][2] == 'row' or a[0][0] == a[1][0] == a[2][0] == 'row'or a[1][1] == a[0][0] == a[2][0] == 'row'or a[2][2] == a[2][1] == a[2][0] == 'row'or a[1][0] == a[1][1] == a[1][2] == 'row'or a[0][2] == a[1][2] == a[2][2] == 'row'or a[2][1] == a[0][1] == a[1][1] == 'row') :
        print(name1, "wins") 
        break  


  elif (a[0][0] ==a[0][1] ==a[0][2]   == 'O' or a[0][0] == a[1][1] == a[2][2] == 'O' or a[0][0] == a[1][0] == a[2][0] == 'O'or a[1][1] == a[0][0] == a[2][0] == 'O'or a[2][2] == a[2][1] == a[2][0] == 'O'or a[1][0] == a[1][1] == a[1][2] == 'O'or a[0][2] == a[1][2] == a[2][2] == 'O'or a[2][1] == a[0][1] == a[1][1] == 'O') :    
    print(name2," wins")
    break
  

      

  row, column = input("Enter the coordinates: ").split()
  row = int(row)
  column = int(column)
  if row <=3 and  row >= 1 and column <= 3 and column >= 1:
    if a[row-1][abs(column - 3)] != ' ' :
      print("This cell is occupied! Choose another one!")
      continue
    else :
       
      a[row - 1][abs(column - 3)] = o
      if o == 'row' :
           o = '0'
           nrow += 1  
      else :
            o = 'row'
            ncolumn   += 1   
       
     # break
  elif row >=3 and row<= 1 or column   >= 3 or column <=1:
    print("Coordinates should be from 1 to 3!")
    continue
  else :
    print("column o u should enter numbers!") 
    continue

    
  print("---------") 
  for i in range(0,3):
  
    print('\n|',a[ i ][ 0 ],a[i][1],a[i][2],'|')
  print("\n---------") 

