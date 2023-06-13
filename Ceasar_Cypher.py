from Alphabet import alphabet 
def cypher(code, shift,direction):
    if(direction == "d"):
        shift *= -1
    code = list(code)
    for i in range (len(code)):
        if code[i] in alphabet:
            index = alphabet.index(code[i])+shift
            code[i] = alphabet[index]
    return "".join(code)

while(True):
    direction = input("Enter E for encoding and D for decoding: ").lower()
    code = input("Enter the string: ").lower()
    shift = int(input("Enter the shift: "))
    print(cypher(code,shift,direction))
    call = input("Enter Y to continue and N to stop: ").lower()
    if(call == "n"):
        break
