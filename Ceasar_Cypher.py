from Alphabet import alphabet 
def encode(code, shift):
    code = list(code)
    for i in range (len(code)):
        index = alphabet.index(code[i])+shift
        if index>25:
            index -=26
        code[i] = alphabet[index]
    return "".join(code)
def decode(code, shift):
    code = list(code)
    for i in range (len(code)):
        code[i] = alphabet[alphabet.index(code[i])-shift]
    return "".join(code)

while(True):
    call = input("Enter E for encoding and D for decoding: ").lower()
    if(call == "e"):
        code = input("Enter the string to encode: ").lower()
        shift = int(input("Enter the shift: "))
        print(encode(code,shift))
    elif(call == "d"):
        code = input("Enter the string to decode: ").lower()
        shift = int(input("Enter the shift: "))
        print(decode(code,shift))
    else:
        print("Invalid input")
    call = input("Enter Y to continue and N to stop: ").lower()
    if(call == "N"):
        break