import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
   
    output = "" 
    len_flag = len(email) != 6
    # Implemented functionality rather than literals
    # kept all values in the anum_flag (bool) variable
    # kept len_flag for charatcer size check
    #   used anum_flag for email[:3] (check first half) and email[3:] (check second half)
    
    anum_flag =  email[:3].isalpha() and email[3:].isdecimal()
    if len_flag:
        output += ("Length check failed\n")
        output += 'Email must be 6 characters long.'
        logging.info(output)
        return output  
    elif not anum_flag:
        output += ("alpha num check failed\n")
        output += 'Email must have 3 letters followed by 3 digits.'
        logging.info(output)
        return output
    # Assigned each index with literals 
    email_lst = [email[0], email[1], email[2], email[3], email[4], email[5]]
      
   # assigned each index in email with literal to decrpty below using -3 shift ord and chr function.
   
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
    
        
    # converted list into a string and then join function back to string for decrypt
    email_str = "".join(email_lst)

    # kept all updates in the retVal (str) variablei
   
    retVal = email_str
    return retVal 

def decrypt(email="def345"):
  
    # input validation
    output = "" 
    len_flag = len(email) != 6 
    
    anum_flag = email[:3].isalpha() and email[3:].isdecimal()

    if len_flag:
        output += ("Length check failed\n")
        output += 'Email must be 6 characters long.'
        logging.info(output)
        return output 
    
    email_lst = [email[0], email[1], email[2], email[3], email[4], email[5]]
    # assigned each index in email with literal to decrpty below using -3 shift ord and chr function.
    
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
    
    if not anum_flag:
       output += ("alpha num check \n")
       output += 'Email must have 3 letters followed by 3 digits.'
       logging.info(output)
       return output
    else:
        output +=  "".join(email_lst)
        return output


