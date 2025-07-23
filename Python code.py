from caesar_cipher_logo import logo
print(logo)

#function to perform encryption or decryption
def caesar_cipher(text, shift, encode_or_decode):
    result = ""

    if encode_or_decode == "decode":
        shift *= -1

    for char in text:
        if char.isalpha():
            base_value= ord("A") if char.isupper() else ord("a")
            shifted_value= (ord(char)-base_value+shift)%26+base_value
            shifted_text=chr(shifted_value)
            result+=shifted_text
        else:
            result+=char #keeps punctuation,spaces,special characters etc.

    print(f"Here is your result: ",result )
#function for bruteforce
def bruteforce(text):
    decoded_keys = []
    for decode_shift in range(1, 26):
        decoded_text = ""
        for i in text:
            if i.isalpha():
                base_ord_value = ord("A") if i.isupper() else ord("a")
                shifted_alph = (ord(i) - base_ord_value - decode_shift) % 26 + base_ord_value
                decoded_text += chr(shifted_alph)
            else:
                decoded_text += i
        decoded_keys.append(decoded_text)
    for shift_v, variant in enumerate(decoded_keys, start=1):
        print(f"Shift {shift_v}: {variant}")

#Using While loop to execute the program
game_runs=True
while game_runs:

    direction= str(input("Do you want to encode or decode? Type encode for encryption and decode for decryption.\nOr do you want to Brute-Force the key? Type Bruteforce.")).lower().strip().replace(" ", "")

    if direction=="encode" or direction=="decode":
        user_text = input("Enter your text: ")
        while True:
            try:
                user_shift = int(input("Enter shift value: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        user_shift%= 26

        caesar_cipher(text=user_text, shift=user_shift, encode_or_decode=direction)

        rerun = input("Do you want to restart? Type 'Yes' or 'No'.").lower().strip()
        if rerun == "no":
            game_runs = False
            print("THANK YOU FOR PLAYING. SEE YOU SOON!")

    elif direction=="bruteforce":
        encry_text=input("Enter your Encrypted text here: ")
        bruteforce(text=encry_text)
        rerun = input("Do you want to restart? Type 'Yes' or 'No'.").lower().strip()
        if rerun == "no":
            game_runs = False
            print("THANK YOU FOR PLAYING. SEE YOU SOON!")
    else:
        print("INVALID INPUT!! PLEASE ENTER THE CORRECT DIRECTION.")


