def main():

    
    words = input("Enter some words:")
    
    if (("a" in words) and ("r" in words) and ("e" in words)):
        a_index = words.find("a")
        r_index = words.find("r")
        e_index = words.find("e")

        if a_index < r_index < e_index:
            print("True")
        else:
            print("False")
    else:
        print("False")
    


main()