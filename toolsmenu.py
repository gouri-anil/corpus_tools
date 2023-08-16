def tool_a(file): #string replacer

    print( 'This tool will replace a word with the word of your choice.')

    print('Give the string that needs to be replaced :: ')
    string=input()
    print('Give the replacing string ::')
    rep_string=input()
	
    print('RESULT:\n\n')

    corpus = open(file,'r', encoding="utf8")#encoding coverts data such as text or binary info,into specific format
                                            #for storage, transmission or manipulation by the computers
    count=0

    for line in corpus: #read each line
        word=line.split() #splitting the line into words
        for i in range(len(word)):
            if word[i]==string:
                print(rep_string, end=" ")#it prints out the output as a paragraph and not jump to a new line after every word
                count+=1
            else:
                print(word[i], end=" ")

    corpus.close()

    print ('Number of times string has been replaced :: ', count)


def tool_b(file): #len match

    print('When given a number, this tool prints out all the words with that specific number of letters.')
    print('Give a number ::')
    num=input()
    num=int(num)
    print('RESULT:\n\n')
		
    corpus = open(file,'r', encoding="utf8")#encoding coverts data such as text or binary info,into specific format
                                            #for storage, transmission or manipulation by the computers
    count=0

    for line in corpus: #read each line
        word=line.split() #splitting the line into words
        for i in range(len(word)):
            if len(word[i])==num:			
                print(word[i])
                count+=1
                
    corpus.close()

    if count==0:
        print("There are no words with that specific number of letters.")

    print ('Number of times length has been matched :: ', count) #outside the for loop
		

def tool_c(file): #concordance

    print('Give the word that you want to search for ::')
    find=input()
    print('Give the number of words to show the context ::')
    num=input()
    num=int(num)

    print('RESULT:\n\n')

    corpus = open(file,'r', encoding="utf8")#encoding coverts data such as text or binary info,into specific format
                                            #for storage, transmission or manipulation by the computers
    count=0
	
    entire=[]
    words=[]

    for each_line in corpus:
        entire.append(each_line) #creates and appends each line of the selected corpus into a list

    for each_line in entire:
        temp = each_line.split() #splits each item in the list into separate tokens into a temporary variable
        words+= temp #adds each token of the entire corpus into a list

    for i in range(len(words)): 
        if words[i]==find:
            print(count+1,")", sep="", end=" ")#prints each result in a new line with index
            for j in words[i-num:i+num+1]:
                print( j, end=' ')
            print('\n')#prints in a new line
            count+=1

    corpus.close()

    print('Number of times a match has been found =  ', count)
	
	


