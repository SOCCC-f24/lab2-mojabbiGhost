import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """
    TODO: What is the objective? 

    Args:
        TODO: what arguments and data types are expected? (i.e., email)

    Returns:
        TODO: what varibale and data types are being returned?   
    """
    output = ""     

    if len_flag == len(email) != 6:
        print("Email must be 6 characters long.")        
    elif anum_flag == email[:3] != 'abc' or email[3:] != '012':
        print("Email must have 3 letters followed by 3 digits.")
    else print(output) 
    # TODO: fix line below, process our string into a list
    email_lst = list(email)
        
    # TODO: complete line(s) below, convert EACH new element into a string
    new_ascii = ord(email_lst[0]) + 3    
    email_lst[0] = chr(new_ascii)        
        
    # TODO: fix line below, convert list into a string
    email_str = "dbc012"

    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = email_str
    return retVal 

def decrypt(email="def345"):
    
    # input validation
    output = "" 
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B

    if len_flag == len(email) != 6:
        print("Email must be 6 characters long.")     
    elif anum_flag == email[:3] != 'def' or email[3:] != '345':
        print("Email must have 3 letters followed by 3 digits.") 
    else print(output)

    # TODO: apply the encrypt pseudocode but shift down 3
    
    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = "aef345"
    return retVal
