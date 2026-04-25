import streamlit as st
st.title("Password Analysis Using Streamlit")
st.write("Check your password strength here: ")

email = st.text_input("Enter your email: ")
password = st.text_input("Enter your password: ", type="password")

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
    passed_checks = [i for i in range(len(score)) if score[i] == True]

    checks = ["Password Length", "Uppercase", "Lowercase", "Digits", "Special Character"]
    failed_checks_names = [checks[i] for i in failed_checks] 
    passed_checks_names = [checks[i] for i in passed_checks]
    sum_score = sum(score)
    if sum_score <= 2:
        strength =  "Weak"
    elif sum_score == 3:
        strength = "Medium"
    elif sum_score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"    
    return  (strength, passed_checks_names,failed_checks_names)

if st.button("Check Password"):
    if password == "":
        st.write("Please enter a password.")
    else:
        strength, passed_check_names, failed_checks_names = passStrengthCheck(password)
        if strength == "Weak":
            st.error("Weak")
        elif strength == "Medium":
            st.warning("Medium")
        elif strength == "Strong":
            st.success("Strong")
        else:
            st.success("Very Strong")
        if(passed_check_names):
            st.write("Passed Checks: \n")
            for i in passed_check_names:
                st.success(f"- {i}")
        if len(failed_checks_names) == 0:
            st.success("No failed checks.")
        else:
            st.write("Failed Checks: \n")
            for i in failed_checks_names:
                st.error(f"- {i}")