import random
import string

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print(" Welcome to Password Generator ")
    
    while True:
        try:
            length = int(input("Enter desired password length (e.g., 8, 12, 16): "))
            if length <= 0:
                print("Length must be a positive number!")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
