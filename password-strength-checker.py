import re 

def check_password(password):
    score = 0 
    suggestions = []

    if len(password) < 12:
        score += 1
    else:    
        suggestions.append("Password is too short. Consider using at least 12 characters.")

    if not re.search(r'[A-Z]', password):
        score += 1 
    else:
        suggestions.append("Password should contain at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Password should contain at least one lowercase letter.")

    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append("Password should contain at least one digit.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        suggestions.append("Password should contain at least one special character.")

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"                                  
    else:
        strength = "STRONG"

    print("\n" + "=" * 35)
    print("       PASSWORD STRENGTH CHECKER")   
    print("=" * 35)

    print(f"\nstrength : {strength}")
    print(f"score : {score}/5")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")

    else:
        print("\nGreate! Your password is strong and meets all the criteria.")

    print("=" * 35)

password = input("Enter your password: ")

check_password(password)