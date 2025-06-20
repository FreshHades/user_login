# main.py
from gateway import check_user_file
from built import register, login

def main():
    print(" Starting User Login System...")
    try:
        check_user_file()
    except Exception as e:
        print(f"Gateway Error: {e}")
        return

    while True:
        print("\n--- MENU ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye ")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
