from datetime import date

def validate_signup(first_name, surname, day, month, year, gender, contact):
    
# check if name fields are empty
    if first_name == '' or surname == '':
        return 'Error: First name and surname are required.'

    # calculate age 
    today = date.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day

    age = current_year - year

# if birthday hasn't come yet this year, subtract 1 from age
    if (current_month, current_day) < (month, day):
        age = age - 1

    if age < 13:
        return 'Error: You must be at least 13 years old to sign up.'
    elif age > 120:
        return 'Error: Please enter a valid date of birth.'

# check gender field
    if gender == '' or gender == 'Select your gender':
        return 'Error: Please select your gender.'

# check contact field (email or phone number)
    if contact == '':
        return 'Error: Please enter your mobile number or email.'

    elif '@' in contact:
        # basic email check
        after_at = contact.split('@')[-1]
        if '.' not in after_at:
            return 'Error: Please enter a valid email address.'

    elif contact.isdigit():
 # basic phone number check
        if len(contact) < 10 or len(contact) > 15:
            return 'Error: Please enter a valid phone number.'

    else:
        return 'Error: Please enter a valid email or phone number.'

    return 'Success! Your account details look good.'


# --- test the function ---
result = validate_signup('Pranto', 'Foysal', 5, 7, 2005, 'Male', 'foysalpranto2002@gmail.com')
print(result)