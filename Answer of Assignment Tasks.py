#Task 1: Comprehensive Data Types and Operations
x = 25 #Integer
y = 3.14 #Float
z = "Advanced Python" #String
is_active = False # Boolean
# Concatenate an integer converted to a string with a string
result = str(x) + z
# Perform division of x by y and print the result
print(x / y)  # Output: 7.961783439490445
# Print the concatenated string stored in 'result'
print(result) # Output: 25Advanced Python
# Print the boolean variable 'is_active'
print(is_active) # Output: False


# Task 2: String Manipulations and Lists
text =  "Python programming is powerful and versatile."
# Split the string into a list of words
lst_words = text.split()
# Print the second word in the list
print(lst_words[1])
# Print the list of words
print(lst_words) # Output: ['Python', 'programming', 'is', 'powerful', 'and', 'versatile.']
# Join the list of words into a single string with '-' as the separator
print('-'.join(lst_words)) #output: Python-programming-is-powerful-and-versatile.

# Define a list of numbers
num_lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create a new list containing the squares of each number in num_lst
Squares = [num ** 2 for num in num_lst]

 #print the result.
print(Squares) #output: [100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100, 10000]

# Define a tuple `coordinates` with the values
my_tuple = (34.0522,-118.2437)

# Iterate over the elements of the tuple and print each element
for num in my_tuple:
    
    #print the result.
    print(num) #output: 34.0522
                        #-118.2437

# Define a dictionary for a student
student = {
    "name" : "Alice", 
    "age" : 24,
    "courses" : ["Math", "Science", "English"],
    }

# Add a new key-value pair to the dictionary
student.update({"graduate" : False,}) # {'name': 'Alice', 'age': 24, 'courses': ['Math', 'Science', 'English'], 'graduate': False}

# Update the value of an existing key
student["age"] = 25 

# Print the final dictionary
print(student) #output:{'name': 'Alice', 'age': 25, 'courses': ['Math', 'Science', 'English'], 'graduate': False}

# Define a set of unique numbers
unique_numbers =  {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} # {1, 2, 3, 4, 5} (duplicates are automatically removed in a set)
# Add a new element to the set
unique_numbers.add(6) 
# Remove an element from the set
unique_numbers.remove(2)
# Check if an element exists in the set and print the set
if 3 in unique_numbers:
    print(unique_numbers) #Output: {1, 3, 4, 5, 6}
    
    
#Task 4: Conditional Statements and Loops

    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1: #Any number less than or equal to 1 is not a prime number.
            return False
        for i in range(2, n):
            if n % i == 0:  
                return False # If n is divisible by i, it's not a prime number.
        return True  # If no divisors were found, n is a prime number.
    # Example usage:
    print(is_prime(21)) # Output: False
    
    # Use this function to print all prime numbers between 1 and 50.
    def is_prime():
        """Check if a number is prime."""
        for i in range(2, 51): # Iterate through numbers from 1 to 50.
            for x in range(2, i):
                if i % x == 0:
                    break # If factor found, not prime, so break the loop
            else:
                print(i) # If no factor found, prime number, so print it
    print("Prime number between 1 to 50 are: ")
    is_prime()
    
    #Create a list of integers from 1 to 15. Iterate through the list and perform the following:
    my_lst = list(range(1, 16))
    
    # Iterate through the list and perform operations
    for num in my_lst:
        if num % 3 == 0 and num % 5 == 0: #Checks if the number is divisible by both 3 and 5
            print("FizzBuzz")
        if num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else: #If none of the above conditions are true, prints the number itself.
            print(num)
        