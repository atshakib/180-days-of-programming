def keyboard(shift: str, input: str) -> str:
    listInput = []
    keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
    
    for char in input:
        if char in keyboard:
            index = keyboard.index(char)
            if shift == 'R':
                listInput.append(keyboard[index - 1])
            elif shift == 'L':
                listInput.append(keyboard[(index + 1)])
        else:
            listInput.append(char)  
    
    return ''.join(listInput)

shift = input()
input = input()
print(keyboard(shift , input))
