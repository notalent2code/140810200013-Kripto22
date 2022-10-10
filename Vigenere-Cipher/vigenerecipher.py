import os

def char_to_num(char):
    if char.isupper():
        number = ord(char) - 65
    elif char.islower():
        number = ord(char) - 97
    return number

def num_to_char(number, isUpper):
    if isUpper:
        char = chr(number + 65)
    else:
        char = chr(number + 97)
    return char

def vigenere_cipher(text, method):
    key = input("Masukkan key\t\t: ").upper()
    extended_key = key
    
    while (len(extended_key) < len(text)):
        extended_key += key
    
    if (len(extended_key) > len(text)):
        n = len(text) - len(extended_key) 
        extended_key = extended_key[0:n]
    
    output = ""
    
    if method == 'enkripsi' :
        for i in range(len(text)):
            output += num_to_char((char_to_num(text[i]) + char_to_num(extended_key[i])) % 26, text[i].isupper())
    elif method == 'dekripsi' :
        for i in range(len(text)):
            output += num_to_char((char_to_num(text[i]) - char_to_num(extended_key[i])) % 26, text[i].isupper())
    
    return output

if __name__ == "__main__":
    while True :
        os.system("cls")
        print("Program Vigenere Cipher")
        print("1. Enkripsi\n2. Dekripsi\n3. Keluar")
        choice = input("Pilihan [1-3]\t\t: ")

        if choice == '1':
            plaintext = input("Masukkan Plaintext\t: ").replace(" ", "")
            output = vigenere_cipher(plaintext, "enkripsi")
            print(f"Hasil Enkripsi\t\t: {output}")
            input("\nTekan tombol enter untuk lanjut...")
            
        elif choice == '2':
            ciphertext = input("Masukkan Ciphertext\t: ").replace(" ", "")
            output = vigenere_cipher(ciphertext, "dekripsi")
            print(f"Hasil Dekripsi\t\t: {output}")
            input("\nTekan tombol enter untuk lanjut...")
            
        elif choice == '3':
            exit(0)