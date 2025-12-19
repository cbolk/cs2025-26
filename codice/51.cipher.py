ALPHALEN = 26  # alphabet chars
REVERSE = 'R'
UPPER = 'U'
LOWER = 'L'
SWAP = 'W'
SHIFT = 'S'

OPS = [REVERSE, UPPER, LOWER, SWAP, SHIFT]

def shift_char(base_string, shift):
    """Shift each character by shift positions"""
    
    new_string = ""

    for ch in base_string:
        if ch.isupper():
            shift_ch = chr((ord(ch) - ord('A') + shift) % ALPHALEN + ord('A'))
        elif ch.islower():
            shift_ch =  chr((ord(ch) - ord('a') + shift) % ALPHALEN + ord('a'))
        else:
            shift_ch = ch
        
        new_string += shift_ch
    return new_string


def apply_swap(text):
    """Swap every pair of characters"""
    result = ""
    for i in range(0, len(text), 2): 
        if i + 1 < len(text):
            result += text[i+1]
        result += text[i]
    return result

def encode(text, code):
    """Apply transformations in order"""
    result = text
    codelen = len(code)
    i = 0
    while i < codelen:
        # Reverse
        if code[i] == REVERSE:
            result = result[::-1]        
            i += 1
        # To upper
        elif code[i] == UPPER:
            result = result.upper()  
            i += 1
        # Lower
        elif code[i] == LOWER:
            result = result.lower()  
            i += 1
        # Swap
        elif code[i] == SWAP:
            result = apply_swap(result)
            i += 1
        # Shift
        elif code[i] == SHIFT:
            i += 1
            shift_str = ''
            while i < codelen and code[i].isdigit():
                shift_str += code[i]
                i += 1
            if shift_str:  # Added :
                shift = int(shift_str)  
            else:
                shift = 0
            result = shift_char(result, shift)
        else:
            print(f"Code {code[i]} not recognized!")
            i += 1
    return result

def decode(text, code):
    """Reverse the transformations"""
    operations = []
    i = 0
    while i < len(code):
        if code[i] in OPS[:-1]:
            operations.append(code[i])
            i += 1
        elif code[i] == SHIFT:
            i += 1
            # Extract shift value
            shift_str = ''
            while i < len(code) and code[i].isdigit():
                shift_str += code[i]
                i += 1
            if shift_str:  
                shift = int(shift_str)  
            else:
                shift = 0
             # Store as tuple
            operations.append((SHIFT, shift)) 
        else:
            print(f"Code {code[i]} not recognized!")
            i += 1
    
    # Apply inverse operations in reverse order
    result = text
    for op in operations[::-1]:

        # Reverse
        if op == REVERSE:
            result = result[::-1]  # Reverse is its own inverse
        
        # Uppter / Lower
        elif op == UPPER or op == LOWER:
            # Can't reverse case changes without original:
            # "HELLO" might came from "hello" (all lowercase)
            # "HELLO" might came from "Hello" (mixed case)
            # "HELLO" might came from "HELLO" (already uppercase)
            pass
        
        # Swap
        elif op == SWAP:
            result = apply_swap(result)  # Swap is its own inverse

        # Shift
        else: # Must be tuple ('S', shift)
            result = shift_char(result, -op[1])  # Negative shift
    
    return result