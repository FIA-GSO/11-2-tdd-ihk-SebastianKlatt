def prozentrechner(erreichte_punkte: int, max_punkte: int) -> int:
        
    if type(erreichte_punkte) != int or type(max_punkte) != int:
        raise TypeError

    if erreichte_punkte > max_punkte:
        raise ValueError
    
    if erreichte_punkte <0:
        raise ValueError
    
    if max_punkte <1:
        raise ValueError

    else:
        return erreichte_punkte/max_punkte*100

def notenrechner(erreichte_prozent: int) -> str:

    if type(erreichte_prozent) != int:
        raise TypeError
    
    if erreichte_prozent>100:
        raise ValueError
    
    if erreichte_prozent<0:
        raise ValueError
    
    if erreichte_prozent >=0 and erreichte_prozent <=29:
        return "ungenügend"
    
    elif erreichte_prozent >=30 and erreichte_prozent <=49:
        return "mangelhaft"
    
    elif erreichte_prozent >=50 and erreichte_prozent <=66:
        return "ausreichend"
    
    elif erreichte_prozent >=67 and erreichte_prozent <=80:
        return "befriedigend"
    
    elif erreichte_prozent >=81 and erreichte_prozent <=91:
        return "gut"
    
    elif erreichte_prozent >=92 and erreichte_prozent <=100:
        return "sehr gut"
    

if __name__ == "__main__":
    print("Das ist ein Modul")