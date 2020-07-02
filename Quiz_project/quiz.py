import random

def word_definition(st):
    st= st.strip()
    word, defination = st.split(",", 1)
    return word, defination


# to get the randon word' definition usinf word list and word_dictionary
def get_word_definition(word_list, word_dict):
    random_index = random.randrange(len(word_list))
    word = word_list.pop(random_index)
    definition = word_dict.get(word)
    return word, definition


fh = open("Vocabulary_list.csv")
wd_list = fh.readlines()
#print(wd_list)
#remove duplicates fromt he csv list
wd_list.pop(0)
wd_set = set(wd_list)
fh = open("Vocabulary_set.csv", "w")
fh.writelines(wd_set)

word_dict = {}
for sentence in wd_set:
    word , definition = word_definition(sentence)
    word_dict[word] = definition
    #print(word)


#print(word_dict)
#quiz starts
while True:
    wd_list = list(word_dict)
    choice_list = []
    for x in range(4):
        word, definition = get_word_definition(wd_list, word_dict)
        choice_list.append(definition)
    random.shuffle(choice_list)
    print(word.upper())
    print("------------------------------------------")
    for idx, choice in enumerate(choice_list):print(idx+1, choice)
    choice = int(input("Enter your Choice 1,2,3,4 & 0 to Exit: \n\n"))
    if choice_list[choice -1] == definition:print("Correct Answer!\n")
    elif choice ==0: exit(0)
    else:print("OOPX Incorrect Answer\n\n")   

