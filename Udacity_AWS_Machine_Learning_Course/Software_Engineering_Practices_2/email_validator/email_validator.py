def email_validator(email):
    if email.count("@") == 1 and email.count(".") == 1:
        return True
    else:
        return False 
