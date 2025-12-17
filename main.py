def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("=== Console Text Encryption Tool ===")
    print("1. Encrypt Text")
    print("2. Decrypt Text")

    choice = input("Choose an option (1/2): ")

    text = input("Enter your text: ")
    shift = int(input("Enter shift value (number): "))

    if choice == "1":
        print("Encrypted Text:", encrypt(text, shift))
    elif choice == "2":
        print("Decrypted Text:", decrypt(text, shift))
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
