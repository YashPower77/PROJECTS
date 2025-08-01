import random
import string

def generate_password(choice, length):
    if choice == 1:
        chars = string.ascii_letters
    elif choice == 2:
        chars = string.ascii_letters + string.digits
    elif choice == 3:
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        return None
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print(" Welcome to the Python Password Generator ")
    print("\nChoose your password type:")
    print("1 - Letters only")
    print("2 - Letters + Numbers")
    print("3 - Letters + Numbers + Special Symbols")

    try:
        choice = int(input("\nEnter your choice (1, 2, or 3): "))
        length = int(input("Enter the length of the password: "))
        password = generate_password(choice, length)
        
        if password:
            print(f"\n Your secure password is: {password}")
        else:
            print("\n Invalid choice. Please enter 1, 2, or 3.")
    except ValueError:
        print("\n Please enter valid numeric input.")

if __name__ == "__main__":
    main()
