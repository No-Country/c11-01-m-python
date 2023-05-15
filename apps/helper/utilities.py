def pkgen():
    import string    
    import random # define the random module  
    S = 8 # number of characters in the string.  
#    call random.choices() string module to find the string in Uppercase + numeric data.  
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k= S))
    return str(ran)