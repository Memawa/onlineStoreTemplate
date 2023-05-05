from authentication.authTools import hash_password
from authentication.authTools import username_exists
from authentication.authTools import update_passwords
from authentication.authTools import login_pipeline
from authentication.authTools import check_password

def test_hash_password_generates_salt():
    """
    Tests that the hash_password function generates a salt when one is not provided.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """
    salt, _ = hash_password("password")
    if salt is None:
        error = f"Error in test_hash_password_salt_generation: Salt was not generated.\n  - Actual: {salt}"
        return False, error
    else:
        return True, "Salt was generated."


def test_salt_length():
    """
    Tests that the salt is 32 characters long. Change this test if you change the salt length.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    salt, _ = hash_password("password")
    if len(salt) != 32:
        error = f"Error in test_salt_length: Salt is not 16 characters long.\n  - Actual: {len(salt)}"
        return False, error
    else:
        return True, "Salt is 16 characters long."


def test_hash_password_returns_given_salt():
    """
    Tests that the hash_password function returns the given salt when one is provided.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    first_salt, _ = hash_password("password")
    second_salt, _ = hash_password("password", first_salt)

    if first_salt != second_salt:
        error = f"Error in test_hash_password_returns_given_salt: Salt was not returned.\n  - Actual: {second_salt}"
        return False, error
    else:
        return True, "Salt was returned correctly."


def test_hash_password_uses_given_salt():
    """
    Tests that the hash_password function returns different hashes when given the same password and salt.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    salt, first_hash = hash_password("password")
    _, second_hash = hash_password("password", salt)

    if first_hash != second_hash:
        error = f"Error in test_hash_password_returns_different_hashes: Hashes are not the same.\n  - Expected: {first_hash}\n  - Actual: {second_hash}"
        return False, error
    else:
        return True, "Hashes are different."

def test_username_exist():

    fake = username_exists("RonaldMcdonald")
    if fake == True:
        error =f"Error in test_username_exist {fake} is not there and show not show up"
        return False, error
    else: 
        return True, "Username was not found (Was what it was looking for)"
    
def test_update_passwords():
    
   new_pass = update_passwords("lamron", "rand" , "saltron")
   ccfile = open("authentication/passwords.txt", "r")
   correct 
   for aline in ccfile:
     values = aline.split()
     if values == new_pass:
         correct = True
         return True, "Code updated properly"
     else:
         error = "The password did not update" 
         correct= False, error

    
   ccfile.close()

def test_check_password():
    wrong_pass = check_password("randomly", "fsdf", "dsadf")

    test 
    if wrong_pass == False:
        test = True
        return test, "Password did not match so it works"
    else :
        error = "The password should be wrong and its still shows up true "
        return False , error

def test_login_pipeline():
    wrong_combo = login_pipeline("Ranran" , "paswirrd")
    
    works
    if wrong_combo == False:
        works = True
        return works, "Shows up wrong as it should, Test complete"
    else : 
        works =False
        error = "Comes up as true even though it should not"
        return works, error