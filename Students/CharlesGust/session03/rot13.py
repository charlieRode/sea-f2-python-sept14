def rot13(str):
    return str.encode("ROT13")

if __name__ == "__main__":
    user_input = raw_input("What would you like to ROT13?")
    print rot13(user_input)

