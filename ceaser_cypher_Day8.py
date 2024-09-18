
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("CEASER CYPHER")
def caesar(original_text, shift_amount, direction):
    new_message = ""
    for char in original_text:
        if char in alpha:
            index = alpha.index(char)
            if direction == "encrypt":
                new_index = (index + shift_amount) % 26
            elif direction == "decrypt":
                new_index = (index - shift_amount) % 26
            new_char = alpha[new_index]
            new_message += new_char
        else:
            new_message += char
        
    print(new_message)

go_on = True

while go_on:
    text = input("enter the message:")
    amount = int(input("enter  shift amount : "))
    encrypt_decrypt = input("Encrypt or Decrypt: ").lower()

    caesar(text,amount,encrypt_decrypt)
    do_again = input("Wanna do it again: ").lower()
    if do_again == "no":
        go_on = False

        # go_again = True

# while go_again :
#     cipher = input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()


#     input_msg = input("Input the message: ").lower()

#     shift_no = int(input("Input shift no: "))

#     new_msg = ""
#     # if cipher == "encode":
#     #         shift_no = shift_no

#     if cipher == "decode":
#             shift_no = -(shift_no)

#     for char in input_msg:
#             if char in alpha:
#                 char_index = alpha.index(char)
#                 new_index = (char_index+shift_no) % 26
#                 new_char = alpha[new_index]
#                 new_msg += new_char   
#             else:
#                   new_msg += char

#     print(f'Your new message is : {new_msg}')

#     try_again = input("Type 'yes' to do it again. Otherwise type 'no' :").lower()

#     if try_again == 'no':
#            go_again = False