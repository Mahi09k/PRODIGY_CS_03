import re
import pyfiglet
import random
import string

def assess_password_strength(password):
    # Define criteria for password strength
    criteria = {
        'Length (>= 8 characters)': len(password) >= 8,
        'Uppercase Letter': bool(re.search(r'[A-Z]', password)),
        'Lowercase Letter': bool(re.search(r'[a-z]', password)),
        'Digit': bool(re.search(r'\d', password)),
        'Special Character': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }

    # Calculate overall complexity
    passed_criteria = sum(criteria.values())
    if passed_criteria == 5:
        complexity = 'Strong'
    elif 3 <= passed_criteria < 5:
        complexity = 'Moderate'
    else:
        complexity = 'Weak'

    # Provide feedback to user
    feedback = []
    for criterion, passed in criteria.items():
        feedback.append(f'{criterion}: {"Passed" if passed else "Failed"}')

    # Additional feedback
    if not criteria['Uppercase Letter'] and not criteria['Lowercase Letter']:
        feedback.append("Consider adding both uppercase and lowercase letters.")
    if not criteria['Digit']:
        feedback.append("Consider adding numbers.")
    if not criteria['Special Character']:
        feedback.append("Consider adding special characters (e.g., !, @, #, $).")
    if criteria['Uppercase Letter'] or criteria['Lowercase Letter']:
        feedback.append("Letters are present, but consider adding numbers if not already included.")

    return complexity, feedback

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main_menu():
    title = pyfiglet.figlet_format("Password Strength Checker")
    print(title)
    print("1. Check the password strength")
    print("2. Give a random password")
    print("3. Exit")
    choice = input("Choose an option (1, 2, 3): ")
    return choice

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            password = input("Enter a password to assess: ")
            complexity, feedback = assess_password_strength(password)
            print("\nAssessment Results:")
            for line in feedback:
                print(line)
            print(f'Overall Complexity: {complexity}')
        elif choice == '2':
            length = int(input("Enter the desired length for the random password: "))
            password = generate_random_password(length)
            print(f'Generated Password: {password}')
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
