#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
names_list = []

with open("Input/Names/invited_names.txt",mode="r+") as names:
    index = 0
    names_cont = names.read()
    temp = []
    while index < len(names_cont):
        temp.append(names_cont[index])
        if names_cont[index] == "\n":
            temp.remove(names_cont[index])
            res = "".join(temp)
            names_list.append(res)
            temp = []
        index += 1

print(names_list)
with open("Input/Letters/starting_letter.txt",mode="r+") as file:
    content = file.read()
    for name_len in range(len(names_list)):
        send_file = open(f"Output/ReadyToSend/{names_list[name_len].strip()}_letter.txt",mode="w+")
        i = 0
        while i < len(content):
            f = 0
            if content[i] == "[":
                i += 1
                send_file.write(f"{names_list[name_len].strip()},")
                while content[i + f] != ",":
                    f += 1
                name_len += 1
            else:
                send_file.write(f"{content[i]}")
            i += (1 + f)
        send_file.close()