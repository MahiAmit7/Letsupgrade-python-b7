#  ------------------------------- List Datatype  ---------------------# 


lst = ["Amit" , 10 , 45.98, 9876 , [1 , 2 , 3]]
lst.append("Shaw")
print(lst)

#for index
print(lst.index(10))

#for extend
lst.extend(["aman" , 42])
print(lst)

#for insert
lst.insert(1 , "Shaw")
print(lst)

# for remove
lst.remove("aman") 
print(lst)

# for pop
lst.pop()
print(lst)

# for clear
lst.clear()
print(lst)

#extending the loist as the list is cleared
lst.extend([54 , 42 , 56 , 54 , 96 , 648 , 8365,])
print(lst)

# for count
print(lst.count(96))
 
#for sort 
lst.sort()
print(lst)

# # for reverse
lst.reverse()
print(lst)

#for copy
lst1 = lst.copy()
print(lst1)

#  --------------------------------Dictionary Datatype--------------  #

dct = {"Name" : "Amit" , "Age" : "19" , "City" : "Kolkata" , "Religion" : "Indian"}

#For get function-------
print(dct.get("Name")) # Returns the value of specified keys

#For fromkeys---------
print(dct.fromkeys("Amit")) #returns a dictionary with specified key characters as value none

#For items
print(dct.items()) #returns a list conatining a pair of each value pair

#For keys
print(dct.keys()) #returns the list of all keys in the dictionary

#For pop
dct.pop("Name") #Removes the element of the specified key
print(dct)

#For popoitem
dct.popitem() # Removes the last key value ue pair
print(dct)

#For setdefault
print(dct.setdefault("Name"))  #It will give us the value of the key entered if the key doesnot exist it creates that keys with a nono value

#For values
print(dct.values()) #return the list of all values in the dictionaries

#for copy
dct1 = dct.copy() #copies the key value pair int another dictionarise as specified
print(dct1)

#for clear
dct.clear() #Clears the dictionary
print(dct)


#  ------------------------------ Set datatype ----------------------------#
st = {"amit" , 1 , 1 , 5 , 3456 , 9 , 4 , 2 , 1 }

#For pop
st.pop() #Removes the first first element in the set
print(st)

#For discard
st.discard(2) # removes the specified items
print(st)

#For intersection
st1 = {1 , 2 , 3 , 2 , 9 , 2 , 1 , 0 }
print(st.intersection(st , st1))

#For intersection_update
print(st.intersection_update(st , st1)) # removes the item in this set which are not specified in other specifiedset

#For issubset
print(st.issubset(st1) )# returns whether another set contains this  set or not

#For isdisjoint
print(st.isdisjoint(st1)) # returns whether teo sets have intersection or not

# For issuperset 
print(st.issuperset(st1)) # Returns whether this set contains another set or not

# For remove
st.remove(9) # Removes the specified element from the set 
print(st)

# For symmetric difference
print(st.symmetric_difference(st1)) # returns the sets with the symmetric difference of two sets

# For union
print(st.union(st1)) # Returns the set containing te unionof two set

# For update
st.update(st1) # Returns the set with the union of this set and another 
print(st)

# For symmetric difference update
print(st.symmetric_difference_update(st1)) # inserts the symmetric difference from this set and another
print(st)

#for add
st.add(9)
print(st)

#for clear
st.clear()
print(st)

#----------------------------Tuples datatype-----------------------------#

tup = ("Amit" , "Kumar" , "Shaw" , "54" , "98" , "@gmail.com" , "Amit")

# For count
print(tup.count("Amit")) # Returns the number of specified element present in the tuple

# For index

print(tup.index("Amit")) # Returns the index of the specified element ij the tuple 


# ---------------------------String datatype -----------------------------#

stri = "Amit Kumar"
stri1 = "Shaw"

# For index
print(stri.index("K")) # Rteurns the index of the specified character in the string

# For isalnum
print(stri.isalnum()) # Checks alphanumeric character

# For capatalize
print(stri.capitalize()) # Converts the first letter in capital form if it is not in capital 

# For casefold
print(stri.casefold()) # Converts string into lower case

# For center
print(stri.center(0)) # returns a centered strig

# For count
print(stri.count('m')) # Retuens the number of times the entered valuen is present in the string

# For encode()
print(stri.encode()) # returns an encoded version of string

#For endswith
print(stri.endswith('r')) # returns true if the given string ends with the specified value

# For expandtabs
print(stri.expandtabs(2)) # Sets the tab size of the string

# For find
print(stri.find("u")) # searches the string for a specified valueb and returns the index 

# For format
print(stri.format("a")) # formats specified values in the string

# For index
print(stri.index("a")) # returns the index of the specified value in th string 

#For isalpha
print(stri.isalpha()) # returns true if every character in the string is alphabet

#For decimal
print(stri.isdecimal()) # returns true if every character in the string is decimal

#For isdigit
print(stri.isdigit()) # Returns true if every character in the string is digit

# For identifier
print(stri.isidentifier()) # Returns true if sytring in an identifier

# For isower
print(stri.islower()) # Returns true if every character in th estring is lower case

# For isspace
print(stri.isspace()) # Returns true if all the character in the string is white space

# For istitle
print(stri.istitle()) # Returns true if string follows the rule of the title

# For isupper
print(stri.isupper()) # Returns true if all the character in the string is in upper case

# For join
print(stri.join("kumar")) # joins character by character the arguement to the end of the string

# For ljust
print(stri.ljust(0)) # Returns qa left justified version of the string

# For lower
print(stri.lower()) # Convertsv the string into lower case

# For lstrip
print(stri.lstrip()) # Returns a left trimmed version of the string


# For partition
print(stri.partition("t")) # returns a tuple where the string is parted into threee parts

# For replace
print(stri.replace("m" , "M")) # Returns a string where specified value is replaced with a specified value

# For rfind
print(stri.rfind("t")) # searches a specified value in the string and returns the last index

# For rindex 
print(stri.rindex("i")) #  searches a specified value in the string and returns the last index


# For  partition
print(stri.rpartition("A")) # returns a tuple where the string is parted into threee parts

# For rsplit
print(stri.rsplit()) # splits the string at the specified separator and returns a list

# For rstrip
print(stri.rstrip()) # Returns a right trimmed version of the string

# For splitliness
print(stri.splitlines()) # splits the string at the line breaks and returns a list

#For startswith
print(stri.startswith('r')) # returns true if the given string starts with the specified value

# For strip
print(stri.strip()) # Returns a trimmed version of the string

# For swapcase
print(stri.swapcase()) # Lower case becomes uppercase and vice versa

# For title
print(stri.title()) # Converts the first character of the string in uppercase


# For upper
print(stri.upper()) # Converts the string into upper case

 



