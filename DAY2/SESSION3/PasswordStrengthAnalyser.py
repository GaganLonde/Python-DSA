def passStrengthCheck(password):
    def passlength(password):
        return len(password) >= 8
    def hasUpper(password):
        return any(c.isupper() for c in password)
    def hasLower(password):
        return any(c.islower() for c in password)
    def hasDigit(password):
        return any(c.isdigit() for c in password)
    def has_special_char(password):
        return any(c in ['!','@','#','$','%','^','&','*'] for c in password)
    
    score = [passlength(password), hasUpper(password), hasLower(password), hasDigit(password), has_special_char(password)]
    failed_checks = [i for i in range(len(score)) if score[i] == False]
    checks = ["Password Length", "Uppercase", "Lowercase", "Digits", "Special Character"]
    failed_checks_names = [checks[i] for i in failed_checks] 
    sum_score = sum(score)
    if sum_score <= 2:
        print("Weak")
    elif sum_score == 3:
        print ("Medium")
    elif sum_score == 4:
        print("Strong")
    else:
        print("Very Strong")
    print("Score: ", sum_score)    
    print("Failed Checks: ", failed_checks_names)

password = input("Enter the password: ")
passStrengthCheck(password)