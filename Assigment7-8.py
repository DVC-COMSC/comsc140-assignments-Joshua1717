def main():

    
    words = input("Enter some words:")
    
    if (("p" in words) and ("r" in words) and ("o" in words)):
        a_index = words.find("p")
        r_index = words.find("r")
        e_index = words.find("o")

        if a_index < r_index < e_index:
            print("True")
        else:
            print("False")
    else:
        print("False")
    


main()