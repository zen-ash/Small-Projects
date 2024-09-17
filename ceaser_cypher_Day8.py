
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

go_again = True

while go_again :
    cipher = input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()


    input_msg = input("Input the message: ").lower()

    shift_no = int(input("Input shift no: "))


    new_msg = ""
    # if cipher == "encode":
    #         shift_no = shift_no

    if cipher == "decode":
            shift_no = -(shift_no)

    for char in input_msg:
            if char in alpha:
                char_index = alpha.index(char)
                new_index = (char_index+shift_no) % 26
                new_char = alpha[new_index]
                new_msg += new_char   
            else:
                  new_msg += char

    print(f'Your new message is : {new_msg}')

    try_again = input("Type 'yes' to do it again. Otherwise type 'no' :").lower()

    if try_again == 'no':
           go_again = False
           