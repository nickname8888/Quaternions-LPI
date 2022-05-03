import re
alphanumeric = {"A","B","C","D","E","F","G","g","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"}

state_code = ""
dist_code = ""
char_code = ""
digits = ""
buffer = ""


def removeSpecial(s):
    temp = ""
    for i in s:
        if i in alphanumeric:
            temp  += i
    return temp

    



def toUpper(s):
    temp = ""
    for i in s:
        if i in alphanumeric:
            temp += i
    return temp


def bifurcation_1(s):
    state_code = ""
    dist_code = ""
    char_code = ""
    digits = ""
    temp_state_code = s[0:2]
    temp_dist_code = s[2:4]
    temp_char_code = s[4:-4]
    temp_digits = s[-4: :1]

    td1 = temp_digits[0]
    td2 = temp_digits[1]
    td3 = temp_digits[2]
    td4 = temp_digits[3]
    
   
    
    if temp_state_code[1] == "J" and (temp_state_code[0] == "6"):
        state_code = "GJ"
    if temp_state_code[1] == "6" and (temp_state_code[0] == "A"):
        state_code = "GA"
    elif temp_state_code[0] == "H" and temp_state_code[1] == "H":
        state_code = "MH"
    elif temp_state_code[0] == "N" and temp_state_code[1] == "H":
        state_code = "MH"
    elif temp_char_code[0] == "8" and temp_state_code[1] == "H":
        state_code = "BH"
    elif temp_state_code[0] == "A" and temp_state_code[1] == "S":
        state_code = "AS"
    else:
        state_code = temp_state_code
    dist_code_1 = temp_dist_code[0]
    dist_code_2 = temp_dist_code[1]
    if dist_code_1 == "O":
        dist_code += "0"
    if dist_code_1 == "Z" or dist_code_1 == "L":
        dist_code += "4"
    if dist_code_1 == "G":
        dist_code += "6"
    if dist_code_1 == "S":
        dist_code += "5"
    if dist_code_1 == "B":
        dist_code += "8"
    if dist_code_1 == "g":
        dist_code += "9"
    if dist_code == "":
        dist_code += dist_code_1

    if dist_code_2 == "O":
        dist_code += "0"
    if dist_code_2 == "Z" or dist_code_2 == "L":
        dist_code += "4"
    if dist_code_2 == "G":
        dist_code += "6"
    if dist_code_2 == "S":
        dist_code += "5"
    if dist_code_2 == "B":
        dist_code += "8"
    if dist_code_2 == "g":
        dist_code += "9"
    if len(dist_code)== 1:
        dist_code += dist_code_2

    


    if td1 == 'O' or td1 == 'D':
        td1 = '0'
    if td1 == 'B':
        td1 = '8'
    if td1 =='g':
        td1 = '9'
    if td1 == 'L' or td1 =='Z':
        td1 = '4'
    if td1 == 'S':
        td1 = '5'
    else:
        pass


    if td2 == 'O' or td2 == 'D':
        td2 = '0'
    if td2 == 'B':
        td2 = '8'
    if td2 =='g':
        td2 = '9'
    if td2 == 'L' or td2 =='Z':
        td2 = '4'
    if td2 == 'S':
        td2 = '5'
    else:
        pass


    if td3 == 'O' or td3 == 'D':
        td3 = '0'
    if td3 == 'B':
        td3 = '8'
    if td3 =='g':
        td3 = '9'
    if td3 == 'L' or td3 =='Z':
        td3 = '4'
    if td3 == 'S':
        td3 = '5'
    else:
        pass

    if td4 == 'O' or td4 == 'D':
        td4 = '0'
    if td4 == 'B':
        td4 = '8'
    if td4 =='g':
        td4 = '9'
    if td4 == 'L' or td4 =='Z':
        td4 = '4'
    if td4 == 'S':
        td4 = '5'
    else:
        pass
    temp_digits = td1+td2+td3+td4
    # print(temp_digits)
    # print(td1)
    # print(td2)
    # print(td3)
    # print(td4)

    # cleaned_digits = td1 + td2 + td3 + td4
    # print(cleaned_digits)

    

    #######################################
    return state_code + dist_code + temp_char_code + temp_digits
    
        
    

def stringClean(lstOp):
    if len(lstOp) == 0:
        return ''
    clean = ""
    actual_string = ""
    length = len(lstOp)
    if length >= 2:
        actual_string = lstOp[1]
    else:
        actual_string = lstOp[0]

    actual_string = actual_string.upper()

    clean = toUpper(actual_string)
    if len(clean)<=8 or len(clean)>10:
        return ''
    return bifurcation_1(clean)
    




# print(stringClean(['WH05EEO024']) )
# print(toUpper('MH 47 CS 9160'))
# bifurcation_1('MH 47 CS 9160')

# print(removeSpecial("ABCD,@"))


    

