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
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    anum_flag =  email[3].isalpha() and email[:3].isdecmial()
    if len_flag:
        return("length check failed\n")
    elif anum_flag:
        return("alpha num check failed\n")

    # TODO: fix line below, process our string into a list
    email_lst = [email[0], email[1], email[2], email[3], email[4], email[5]]
        
    # TODO: complete line(s) below, convert EACH new element into a string
    new_ascii = ord(email_lst[0]) + 3    
    email_lst[0] = chr(new_ascii)  
    new_ascii = ord(email_lst[1]) + 3    
    email_lst[1] = chr(new_ascii) 
    new_ascii = ord(email_lst[2]) + 3    
    email_lst[2] = chr(new_ascii) 
    new_ascii = ord(email_lst[3]) + 3
    email_lst[3] = chr(new_ascii)
    new_ascii = ord(email_lst[4]) + 3    
    email_lst[4] = chr(new_ascii) 
    new_ascii = ord(email_lst[5]) + 3    
    email_lst[5] = chr(new_ascii) 
    
        
    # TODO: fix line below, convert list into a string
    email_str = "".join(email_lst)

    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = email_str
    return retVal 

def decrypt(email="def345"):
    """
    TODO: What is the objective? 

    Args:
        TODO: what arguments and data types are expected? (i.e., email)

    Returns:
        TODO: what varibale and data types are being returned?   
    """
    # input validation
    output = "" 
    len_flag = len(email) != 6 
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    anum_flag = email[3].isalpha() and email[:3].isdecmial()

    if len_flag:
        return("length check failed\n")
    
    email_lst = [email[0], email[1], email[2], email[3], email[4], email[5]]
    
    
    new_ascii = ord(email_lst[0]) - 3    
    email_lst[0] = chr(new_ascii)  
    new_ascii = ord(email_lst[1]) - 3    
    email_lst[1] = chr(new_ascii) 
    new_ascii = ord(email_lst[2]) - 3    
    email_lst[2] = chr(new_ascii) 
    new_ascii = ord(email_lst[3]) - 3
    email_lst[3] = chr(new_ascii)
    new_ascii = ord(email_lst[4]) - 3    
    email_lst[4] = chr(new_ascii) 
    new_ascii = ord(email_lst[5]) - 3    
    email_lst[5] = chr(new_ascii) 
    
    if anum_flag:
        print("alpha num check \n")
    else:
        return "".join(email_lst)


