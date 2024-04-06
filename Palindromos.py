def is_palindrome(mistring):
    mistring = mistring.replace(" ", "")
    for indice in range(len(mistring) // 2): 
        print(mistring[indice] + " --> " + mistring[-(indice +1)])
        if mistring[indice] != mistring[-(indice + 1)]:
            return False
    return True 