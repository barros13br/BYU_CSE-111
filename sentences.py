import random

def main():
   
    quantity = ""
    tense = ""
    sentence_1_past = creating_sentence(1, "past")
    sentence_1_present = creating_sentence(1, "present")
    sentence_1_future = creating_sentence(1, "future")
    sentence_2_past = creating_sentence(2, "past")
    sentence_2_future = creating_sentence(2, "future")
    sentence_2_present = creating_sentence(2, "different")
 
    print()
    print(sentence_1_past)
    print(sentence_1_present)
    print(sentence_1_future)
    print(sentence_2_past)
    print(sentence_2_present)
    print(sentence_2_future)
    print()

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one","the"]
    else:
        words = ["some", "many", "the"]
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        noun_word = [ "young man", "person", "young gril", "cheef", "friend"]
    else:
        noun_word = ["gentlemens","Womens", "Mens", "classmates", "giraffes"]
    noun_word_random = random.choice(noun_word)
    return noun_word_random

def get_verb(quantity, tense):
    if quantity == 1 and tense == "past":
        verb = ["ate","ran", "wrote", "painted", "cried", "sleept", "fainted", "worked"]
    elif quantity == 1 and tense == "present":
        verb = ["eats", "runs", "writes", "paints", "crys", "sleeps", "faints", "works"]

    elif quantity == 1 and tense == "future":
        verb = ["will eat", "will run", "will write", "will paint", "will cry", "will sleep", "will work", "will faint"] 
    
    else: #quantity != 1 and tense == "present"
        verb = ["eat", "run", "write", "paint", "cry", "sleep", "faint", "work"]
    verb_random = random.choice(verb)
    return verb_random

def creating_sentence(quantity, tense):
    #here I invoke the functions and I gave the values that maches with the propouses that I wanted 
    determiner_sen_1 = get_determiner(1)
    determiner_sen_2 = get_determiner(2)
    noun_sen_1 = get_noun(1)
    noun_sen_2 = get_noun(2)
    verb_sen_past = get_verb(1, "past")
    verb_sen_present = get_verb(1, "present")
    verb_sen_future = get_verb(1, "future")
    verb_sen_plural_present = get_verb(2, "different")
    #Here I rote how the sentence would be constructed
    if quantity == 1 and tense == "past":
        sentence = f"{determiner_sen_1.capitalize()} {noun_sen_1} {verb_sen_past}"
    elif quantity == 1 and tense == "present":
        sentence = f"{determiner_sen_1.capitalize()} {noun_sen_1} {verb_sen_present}"
    elif quantity == 1 and tense == "future":
        sentence = f"{determiner_sen_1.capitalize()} {noun_sen_1} {verb_sen_future}"
    elif quantity != 1 and tense == "past":
        sentence = f"{determiner_sen_2.capitalize()} {noun_sen_2} {verb_sen_past}"
    elif quantity !=1 and tense == "future":
        sentence = f"{determiner_sen_2.capitalize()} {noun_sen_2} {verb_sen_future}"
    else:
        sentence = f"{determiner_sen_2.capitalize()}  {noun_sen_2}  {verb_sen_plural_present}"
    return sentence
main()