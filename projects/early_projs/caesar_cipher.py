logo = """
,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88 
"""

print("\n*************************** welcome to ***************************")
print(f"{logo}")

def encode(alphabet, message, shift_num, result):
    for i in range(0,len(message)):
        for f in range(0,len(alphabet)):
            if(alphabet[f] == message[i]):
                if((f + shift_num) <= 26):
                    result.append(alphabet[f + shift_num])
                else:
                    position = (shift_num + f) - 26
                    if(position < 0 or position > 26):
                        result.append(alphabet[position - 26])
                    else:
                        result.append(alphabet[position])

def decode(alphabet, message, shift_num, result):
    num_list = list(range(0,26))
    for i in range(0,len(message)):
        for f in range(0,len(alphabet)):
            if(alphabet[f] == message[i]):
                if((f - shift_num) >= 0):
                    result.append(alphabet[f - shift_num])
                else:
                    position = 26 - (shift_num - f)
                    result.append(alphabet[26 - (shift_num - f)])

        
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
end_game = 1
while end_game == 1:
    check_mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message: \n")
    shift_num = int(input("Type the shift number: \n"))
    result = []
    if(check_mode == "encode"):
        encode(alphabet, message, shift_num, result)
        print(f"Here's the encoded result: \n{''.join(result)}")
    else:
        decode(alphabet, message, shift_num, result)
        print(f"Here's the decoded result: \n{''.join(result)}")
    check_end = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if not(check_end =="yes"):
        end_game = 0
print("Thank you for using caesar_cipher")
    

