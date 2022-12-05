# Get the number of male and females students
males = int(input("How many males are in your class?"))
females = int(input("How many females are in your class?"))
 
 # Calculate the total number of students
total = males + females

 # Calulate the percentage of male and female students
pct_males = float(format((males / total),'.2f' ))
pct_females = float(format((females / total),'.2f' ))

 # Display the data
print (" ")
print ("****************************************")
print (" ")
print("There are", males,"male students.")
print("There are", females,"female students.")
print("There are a total of", total,"students.")
print("The class has", format(pct_males,'.0%'),"male students.")
print("The class has", format(pct_females,'.0%'),"female students.")