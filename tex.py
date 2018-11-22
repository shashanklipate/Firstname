#L
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 ) and row != 0) or ((row == 6) and (column > 1 and column < 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#A
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );


#K
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 ) ) or ((row == 0) and (column == 5)) or ((row == 1) and (column == 4)) or ((row == 3) and (column == 2)) or ((row == 2) and (column == 3)) or ((row == 4) and (column == 3)) or ((row == 5) and (column == 4)) or ((row == 6) and (column == 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#S
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if ((row == 0 or row== 3 or row == 6 ) and (column > 0 and column < 6) or (column == 1 and (row == 1 or row == 2 or row == 5)) or (column == 5 and (row == 1 or row == 4 or row == 5)) ):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#H
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 3) and (column > 1 and column < 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#M
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 3) and (column == 3)) or ((row == 2) and (column == 2 or column == 4))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );


#I
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 3 ) and row != 0) or ((row == 6 or row == 1) and (column > 0 and column < 6))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#B
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and (row != 0 or row != 6)) or ((row == 0 or row == 3 or row ==6) and (column > 1 and column < 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#C
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 ) and row != 0) or ((row == 6 or row == 1) and (column > 0 and column < 6))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#D
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 ) ) or ((row == 6 or row == 0) and (column > 0 and column < 5)) or ((column == 5) and (row > 0 and row < 6)) ):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );


#E
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 )) or ((row == 6 or row == 0 or row == 3) and (column > 0 and column < 6))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#F
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 )) or ((row == 0 or row == 3) and (column > 0 and column < 6))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#G

#J


#N

#O
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5 )) or ((row == 0 or row == 6) and (column > 0 and column < 6))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#P
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1)) or ((row == 0 or row == 3) and (column > 0 and column < 6)) or (column == 5 and row < 3)):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#Q
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5 ) and row < 5) or ((row == 0 or row == 5) and (column > 0 and column < 6)) or (column == 3 and row > 3)):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#R
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1)) or ((row == 0 or row == 3) and (column > 0 and column < 6)) or (column == 5 and row < 3)):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#T
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 3 ) and row != 0) or ((row == 1) and (column > 0 and column < 6))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );


#U
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5 ) and row != 0) or ((row == 6 ) and (column > 0 and column < 6))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#V
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((row == 6 ) and (column == 3)) or (row == 5 and (column == 2 or column == 4)) or (row < 5 and (column == 1 or column == 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#W
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((row == 6 ) and (column == 3)) or (row == 6 and (column == 2 or column == 4)) or (row < 6 and (column == 1 or column == 5 or column == 3))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#X
#Y
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((row == 4 ) and (column == 3)) or (row == 3 and (column == 2 or column == 4)) or (row > 4 and (column == 3)) or ((row == 1 or row == 2) and (column == 1 or column == 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
print("   " );

#Z


