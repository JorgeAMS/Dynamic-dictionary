chars=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z")


def check_email(email):
    email= email.lower()

    name_and_domain=email.split("@")

    email_is_valid= "@" in email and "." in name_and_domain[1] and not email.startswith("@") and email.endswith(chars) and email.startswith(chars) and not email.find(" ")>=1

    if email_is_valid:
        valid="valid"
    else:
        valid="not valid"

    print(f"The email {email} is {valid}")
