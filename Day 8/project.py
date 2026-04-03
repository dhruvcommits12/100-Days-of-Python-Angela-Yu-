from art import logo
print(logo)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(direction, original_text, shift_amount):

    if direction=="decode":
        shift_amount*=-1
    
    final_result=""
    for letter in original_text:
        if letter in alphabet:
            shift_amount%=26
            final_result+=alphabet[(alphabet.index(letter)+shift_amount)]
        else:
            final_result+=letter
    
    print(f"Your {direction}d text:{final_result}")

should_continue=True

while should_continue:

    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift = int(input("Type the shift numer:\n"))
    
    caesar(direction,text,shift)

    to_continue = input("Type 'yes' if you wanna go again or else type 'no'\n:")

    if to_continue=="no":
        should_continue=False
        print("GoodBye")


    


    
