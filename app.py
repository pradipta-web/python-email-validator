import re
from colorama import init, Fore

init(autoreset=True)


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if not email:
        return False, "Email cannot be empty."

    if not re.match(pattern, email):
        return False, "Invalid email format."

    if ".." in email:
        return False, "Email cannot contain consecutive dots."

    return True, "Email format is valid."


def main():
    print("=" * 45)
    print("              EMAIL VALIDATOR")
    print("=" * 45)

    while True:
        print("\nEnter email (or type 'exit' to quit):")
        email = input("> ").strip()

        if email.lower() == "exit":
            print("\nThank you for using Email Validator!")
            break

        is_valid, message = validate_email(email)

        print("\n" + "-" * 45)

        if is_valid:
            print(Fore.GREEN + "Status: VALID")
        else:
            print(Fore.RED + "Status: INVALID")

        print(f"Message: {message}")
        print("-" * 45)


if __name__ == "__main__":
    main()