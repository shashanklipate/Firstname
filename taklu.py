#T A
result_str="";    
for row in range(0,7):    
    for column in range(0,40):    
#T	A
        if (((column == 3 ) and row != 0) or ((row == 0) and (column > 0 and column < 6)) or ((column == 9 or column == 13) and row != 0) or ((row == 0 or row == 3) and (column > 9 and column < 13))):    
            result_str=result_str+"*"    
			#K
        elif(((column == 17 ) ) or ((row == 0) and (column == 21)) or ((row == 1) and (column == 20)) or ((row == 3) and (column == 18)) or ((row == 2) and (column == 19)) or ((row == 4) and (column == 19)) or ((row == 5) and (column == 20)) or ((row == 6) and (column == 21))):      
            result_str=result_str+"*"
 #L U
        elif (((column == 25 ) and row != 6) or ((row == 6) and (column > 25 and column < 29)) or ((column == 32 or column == 36) and row != 6) or ((row == 6) and (column > 32 and column < 36))):
			result_str=result_str+"*"
        else:      
            result_str=result_str+" "   
    result_str=result_str+"\n"    
print(result_str);
print("   " );



