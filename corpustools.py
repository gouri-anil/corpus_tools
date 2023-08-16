import toolsmenu

option="yes" #base value for while loop to function

while option.lower()=="yes":

    #first menu to choose tools
    print("MENU\n")
    print ("1. String Replacer \nAutomates search and replace operations in text. \nEffortlessly modify strings within documents, code, or any text data using specified patterns.\n")
    print ("2. Word Length Matcher \nSwiftly identifies words matching a user-defined length in text. \nSimplifies linguistic analysis by locating specific-length words in documents or corpora.\n")
    print ("3. Concordance Tool \nGenerates word context insights. \nDisplays word occurrences within context, aiding linguistic analysis by showing surrounding text snippets in which a word appears.\n")

    print ("Choose a tool by entering 1,2 or 3 :: ")
    tool=input()

    #second menu to choose corpus
    print("\n\nLIST OF CORPORA AVAILABLE\n")
    print ("1. Gone With the Wind, chapter 1.")
    print ("2. To Kill A Mockingbird, chapter 7.")
    print ("3. Pride and Prejudice, chapter 10.")
    print ("4. The Great Gatsby chapter 5.")
    print ("5. Jane Eyre, chapter 20.")

    print ("Choose a corpus by entering the respective serial number :: ")
    corpora=input()

    filename=""

    #assigning file path according to chosen corpus
    if corpora=="1":
        filename="GONE WITH THE WIND (CHAPTER 1).txt"
    elif corpora=="2":
        filename="TO KILL A MOCKINGBIRD (CHAPTER 7).txt"
    elif corpora=="3":
        filename="PRIDE AND PREJUDICE (CHAPTER 10).txt"
    elif corpora=="4":
        filename="THE GREAT GATSBY (CHAPTER 5).txt"
    elif corpora=="5":
        filename="JANE EYRE (CHAPTER 20).txt"
    else:
        print("Choose an available corpus.")

    
    #calling specific functions in the toolsmenu module
    if tool== "1":
        toolsmenu.tool_a(filename)
    if tool== "2":
        toolsmenu.tool_b(filename)
    if tool== "3":
        toolsmenu.tool_c(filename)
    else:
        print("Choose an available tool.")

    
    print ("Would you like to continue using the tools? Answer with yes or no :: ")
    
    option=input()
        
