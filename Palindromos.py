def is_palindrome(mistring):
    for indice in range(0, len(mistring)):
        print(mistring[indice] + " --> " + mistring[-(indice +1)])
        if mistring[indice] != mistring[-(indice +1)]:
            print("False")
            return False
        
    return True