#lests learn how to read one line from a file 
#In previous video we learned about open() function

f = open("/home/ahmaday/doc1st.txt", "r")
print(f.readline())  # This will read one line from the file. If we want to print two lines, then call this function twice
print(f.readline())  # We can also print limited characters. It print 6 characters including the empty space
f.close()  #Its a good practice to close a file after opening it.



