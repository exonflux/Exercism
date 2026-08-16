def response(hey_bob):

    
    if not hey_bob.strip():
        return "Fine. Be that way!"
    
    if hey_bob.endswith("?") and hey_bob.isupper() == True:
        return "Calm down, I know what I'm doing!"
        
    if hey_bob.strip().endswith("?") and hey_bob.isupper() == False:
        return "Sure."

    if hey_bob.isupper() == True:
        return "Whoa, chill out!"


    
    return "Whatever."