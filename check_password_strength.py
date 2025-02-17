from password_strength import PasswordPolicy

# defining function to check password strength
def check_password_strength(password: str) -> bool:
    policy = PasswordPolicy.from_names(
        length=8, # mininum 8 characters
        uppercase=3, # mininum 2 uppercase characters required
        special=1, # mininum 2 special characters required
        numbers=1
    )
    return policy.test(password) == []

password = input("Enter the Password :  ")
if check_password_strength(password):
    print("password is strong")
else:
    print("password is not strong")