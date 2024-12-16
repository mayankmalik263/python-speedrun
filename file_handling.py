p = 'a_test.txt'

with open(p, 'r') as f:
    # print(f.readlines()) # reading all the lines in the file in a single line 
    # Well we have to comment out the above line to run the other because when we use readline the cursor goes from start to the very end
    # so the below statement just prints a space
    print(f.read()) # it will print the content of the file as it is (raw string)
    f.close() # this will close the file that we have opened above
    print("-----------------")
    
with open(p, 'r') as f:
    for line in f:
        print(line) # it will print each line of the file on a new line
                    # but if you want to remove the lines between the lines so just strip them up (remove them)
    print("------------------")
with open(p, 'r') as f:
    for line in f:
        print(line.rstrip()) # this will remove the lines between the lines and print them just in the next line

# why do we want this method BECAUSE consider you have a big file to read then it all will be loaded in the memory at once and that
# might take a lot of your time and something even crash your pc.
# so reading them by this method line-by-line is kind of good for you

