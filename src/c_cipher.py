import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    output = "" 
    len_flag = len(email) == 6
    anum_flag = email[:3] != 'abc' or email[3:] != '012' 

    email_lst = ["a", "b", "c", "0", "1", "2"]
    email_str = string(email_lst)
    # TODO: complete line(s) below, convert EACH new element into a string
    new_ascii = ord(email_lst[0]) + 3    
    email_lst[0] = chr(new_ascii)        
    if len(email_lst) != 6:
        output += "Email must be 6 characters long."
        logging.info(output)
    elif email_lst:
        output += "Email must have 3 letters followed by 3 digits."
    else:
        logging.info(output)
        print(output)     
    
      
    # TODO: fix line below, convert list into a string
email_str = "dbc012"
   
retVal = email_str
print(retVal) 

def decrypt(email="def345"):
    output = "" 
    
len_flag = len(email) == 6
anum_flag = email[:3] != 'def' or email[3:] != '345' 
if len(email_lst) != 6:
        output += "Email must be 6 characters long."
        logging.info(output)
elif email_lst:
    output += "Email must have 3 letters followed by 3 digits."
else:
    logging.info(output)
    print(output)

   
retVal = "aef345"
print(retVal)
