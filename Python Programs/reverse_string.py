def reverse_words_in_place():
    input_string=str(input("Enter a string to be reversed: "))

    temp_list=input_string.split() #splitting string into words
    reverse_word_list=[] #defining empty list
    for word in temp_list:
        temp_word=word[::-1]  # reversing all the words
        reverse_word_list.append(temp_word)  #reversed words are attached to a string

    reverse_word_string=' '.join(reverse_word_list) # words are separated by space
    print(reverse_word_string)
    
reverse_words_in_place()