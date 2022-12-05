
# Get degrees Celsius from user
celsius = float( input("Enter a temperature value in degrees Celsius: " ))  
  
# Converting Celsiuse to Fahrenheit 
fahrenheit = float(9/5)* celsius + 32
    
# Display result
print ((format(celsius, ' .1f')) , "degrees Celsius is equal to", (format( fahrenheit, '.1f')), "degrees Fahrenheit.")