"""------------------------------------------------------------------------------------------------
Date:       08-01-25
Notes:      CS50 Introduction to Python with David Malan - Youtube
            https://www.youtube.com/watch?v=nLRL_NcnK-4&t=15212s
Project:    Entire Courses Explame Programs 
------------------------------------------------------------------------------------------------"""
#--------------------------------32--------------------------------64



# Variables & Funcitons
"""
Questions:




1
Why does this 

name = "me"
print("Hello, ", {name})

Output: Hello, {'me'}
Shouldn't it output: Hello, {"me"} <---- with > me < in double quotes?




2




3




4




5








1 print()

    # Output:Hello World


print("Hello World")




2 input() and print()

    # This verison using a comma >,< automatically includes a space after "Hello," 
    # Output:Hello, Darren


name = input("Please enter your name: ")

print("Hello,", name)    




3 using + operator in print()

    # This version using the plus operator >+< does NOT sutomatically include a space after "Hello," 
    # Output:Hello,Darren


name = input("Please enter your name: ")

print("Hello," + name)




4 Python Documentation

    # Pythons - function - documentation can be found here: docs.python.org/3/library/functions.html
    # The - print - functions specific documentation can be found here: docs.python.org/3/library/functions.html#print
    # Which looks like this: print(*objects, sep=' ', end=/n, file=sys.stdout, flush=False) <---- Had to type / instead of the correct forward slash




5 end=''

    # Adding the end='' or end="" eliminates the seperation that would occur from the two print statements
    # Output:Hello, Darren


name = input("What's your name? ")

print("Hello, ", end="")

print(name)




6 end='???' with char's & strings

    # We can also use the end='' or end='' and include char's or str's
    # Output:Hello, ???Darren


name = input("What's your name? ")

print("Hello, ", end="???")

print(name)




7 sep='' & Sep'???'

    # Just like we can include char's or str's to end='', we can do the same with sep='' or sep=""
    # Notice that for this example there is only one print statement, this is because we removed the end=''
    # Output:Hello, ???Darren


name = input("What's your name? ")

print("Hello, ", name, sep="???")




8 Escape Char \ 

    # If we need to include the exact same comma format that we intend to also use with our strings, we can 
    # use the \ escape character which must be immediately followed by the char we need to excape
    # Output:Hello, "friend"


print("Hello, \ "friend\ "")     
               ^        ^       *** Had to add a space > < after \ or it will effect this whole script




9 Methods        - 0h 49m 
  strip()        - Which is called by using >.strip()<

    # We can add 'methods', (Which are essentially Functions), to str data types ((Maybe functions too ??))
    # Documentation - docs.python.org/3/library/stdtypes.html#string-methods
    # strip() - Will remove all of the whitespaces ffrom the left and right of the string *** Even if it includes more 
        # than one word, such as:>    darren    gibson    < - Ouput:>darren    gibson< - But does NOT remove 
        # the whiteapces in between the words
    # print(f"Hello, {name}") - Was actually used in the video, but just using print() is better for these method examples
    # Input:>    Darren     <
    # Output:Darren<


name = input("Whats your name? ")

name = name.strip()

print(name)        



                        
10 Methods - Cont       - 0h 54m 
   capitalize()         - Which is called by using >.capitalize()<

    # This will capitalize the first letter, of ONLY the first word. So, darren james gibson - will be Darren james gibson
    # Input:darren                                                                                     ^      
    # Output:Darren


name = input("What is your name? ")

name = name.capitalize()

print(name)




11 Methods - Cont       - 0h 55m
   title()              - Which is called by using >.title()<

    # This will capitalize the first letter of ALL the words
    # Input:darren james gibson
    # Output:Darren James Gibson


name = input("Whats your name? ")

name = name.title()

print(name)




12 Methods Cont
   Chaining methods

    # Turns out, we can actually chain methods together - Several examples below. Only the first input & output is listed 
    # Input:>    darren    james    gibson    <
    # Output:>Darren    James    Gibson<
    #        |       ^--!here--^       |
    #        ^---------Removed---------^


name = input("Whats your name? ")

name = name.strip().capitalize().title()
#                        ^---------^---- Really don't need both here, but it works
print(name)


*** OR *** Version 2


    # Input:>     darren     james     gibson     <
    # Output:>hello, Darren     James     Gibson, welcome<
    #               |        ^--!here--^        |
    #               ^-----------Removed---------^


name = input("Whats your name? ").strip().capitalize().title()
                                             # ^---------^---- Really don't need both here, but it works
print(f"hello, {name}, welcome")



13 Methods Cont         - 1h 2m
   split()              - Which is called by using >.split()<

    # split()    :To use the split() function, we leverage the space the USER adds during input
    # Input:>darren gibson<
    # Output:>hello, darren gibson<


name = input("Whats your first and last name:")

first, last = name.split()

print(f"Hello, {first} {last}")         # Notice, we do not need a comma between {first} and {last} unless you want it to show


    NOTES - This >name = input("Please enter your full name: ").split(" ")< will output, the input, as a list 
        Outputs>['darren', 'gibson']<
    NOTES - Using this input >darren james gibson< with this example, will display an Error 
        >ValueError: too many values to unpack (expected 2)<
        and that is because we are giving 3 arguements, but only listing 2 variables.
    NOTES - And, if we have 3 variables, and try to print all 3, and the user only enters two names >darren gibson<

        first, middle, last = name.split()
        print(f"Hello, {first} {middle} {last}")
        
        we will get a similar Error 
        >ValueError: not enough values to unpack (expected 3, got 2)<




14 int - Integers

    # Here we will look at the various ways to use integers
    # Output:3


x = 1

y = 2 

total = x + y

print(total)




15 int()            - 1h 10m
                     
    # Which is called by using >int()< and commonly used with the input() function like this: >int(input())<
    # When we use more that one function in a statement it is know as 'nesting' functions
    # Input>2
    # Output>3


x = input("What is the first number:")

y = input("What is the second number:")

total = int(x) + int(y)

print(total)


    NOTES - Trying to use >int(total)< here doesnt work, total isn't defined
    NOTES - And trying to use: Also doesnt work
        total = x + y
        int(total)
    NOTES - And neither does something like >int(print(total))< Which, is just icrazy to think that it would


    *** OR *** Version 2    Best!!


x = int(input("What is the first number:"))

y = int(input("What is the second number:"))

total = x + y

print(total)


    NOTES - Trying to declare the variable 'total', inside of 'print', like this >print(total = x + y)< doesn't work
    NOTES - But just using >print( x + y )< works just fine
    
*** OR *** Version 3    - Not Recommended, but possible

print(int(input("Whats x:")) + int(input("Whats y:")))


16 float            - 1h 20m
   float            - float is a data type, and is commonly called with the input function like this >float(input("Exampel"))<

    # 
    # Input>
    # Output>




    # 
    # Input>
    # Output>





"""

#---->  Practice Arena  <----#












#---->    Practice Arena    <----#

# Exceptions Practice & Questionable Stuff 
"""






    1
name = "Darren"
num = 42

# This Works
print(name, num)

# This works *remember, the comma will be included in this version
print(f"{name}, {num}")



    2
# NOT WORKING (both versions) - Output: NONE
# Not sure why
oth_name = "James"
second_name = print(oth_name)
print(second_name)
print(f"{second_name}")



# NOT WORKING - Output: NONE
# Wonder if it is because there are two strings
name = "Darren"
num = 42
new_name = print(name, num)      
print(new_name) 



# NOT WORKING
# Output: NONE
# Getting the name with the input function doesn't help either - suppose that makes sense anyhow
name = input("Whats your name:")
print(name)
new_name = print(name)
print(new_name)



# NOT WORKING
# Ouput: NONE
# Trying to use a string in quotes didn't help either
print("hello")
new = print("hello")
print(new)




    3







    4









"""





#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""


#
"""

"""



#
"""

"""

