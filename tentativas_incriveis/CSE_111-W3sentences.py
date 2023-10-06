
# import random 

# def main():
#     quantity = [1,2, 3]
#     tense = ["past", "present", "future"]
    
#     determiner = get_determiner(quantity).capitalize()
#     noun = get_noun(quantity)
#     verb = get_verb(quantity, tense)
#     sentences = make_sentence(quantity, tense)

#     print(f"{sentences}")
#     print

# def get_determiner(quantity):
#     """Return a randomly chosen determiner. A determiner is
#     a word like "the", "a", "one", "some", "many".
#     If quantity is 1, this function will return either "a",
#     "one", or "the". Otherwise this function will return
#     either "some", "many", or "the".

#     Parameter
#         quantity: an integer.
#             If quantity is 1, this function will return a
#             determiner for a single noun. Otherwise this
#             function will return a determiner for a plural
#             noun.
#     Return: a randomly chosen determiner.
#     """
#     if quantity == 1:
#         words = ["a", "one", "the"]
#     else:
#         words = ["some", "many", "the"]

#     # Randomly choose and return a determiner.
#     word = random.choice(words)
#     return word

# def get_noun(quantity):
#     """Return a randomly chosen noun.
#     If quantity is 1, this function will
#     return one of these ten single nouns:
#         "bird", "boy", "car", "cat", "child",
#         "dog", "girl", "man", "rabbit", "woman"
#     Otherwise, this function will return one of
#     these ten plural nouns:
#         "birds", "boys", "cars", "cats", "children",
#         "dogs", "girls", "men", "rabbits", "women"

#     Parameter
#         quantity: an integer that determines if
#             the returned noun is single or plural.
#     Return: a randomly chosen noun.
#     """
#     if quantity == 1:
#         noun_pronoun = [ "young man", "person", "young gril", "cheef", "friend"]
#     else:
#         noun_pronoun = ["gentlemens","Womens", "Mens", "class mates", "giraffes"]
#     noun_pronouns = random.choice(noun_pronoun)
#     return noun_pronouns

# def get_verb(quantity, tense):
#     """Return a randomly chosen verb. If tense is "past",
#     this function will return one of these ten verbs:
#         "drank", "ate", "grew", "laughed", "thought",
#         "ran", "slept", "talked", "walked", "wrote"
#     If tense is "present" and quantity is 1, this
#     function will return one of these ten verbs:
#         "drinks", "eats", "grows", "laughs", "thinks",
#         "runs", "sleeps", "talks", "walks", "writes"
#     If tense is "present" and quantity is NOT 1,
#     this function will return one of these ten verbs:
#         "drink", "eat", "grow", "laugh", "think",
#         "run", "sleep", "talk", "walk", "write"
#     If tense is "future", this function will return one of
#     these ten verbs:
#         "will drink", "will eat", "will grow", "will laugh",
#         "will think", "will run", "will sleep", "will talk",
#         "will walk", "will write"

#     Parameters
#         quantity: an integer that determines if the
#             returned verb is single or plural.
#         tense: a string that determines the verb conjugation,
#             either "past", "present" or "future".
#     Return: a randomly chosen verb.
#     """

#     if quantity == 1 and tense == "past":
#         verb = ["ate","ran", "rote", "painted", "cried", "slept", "fainted", "worked"]
#     elif quantity == 1 and tense == "present":
#         verb = ["eats", "runs", "writes", "paints", "crys", "sleeps", "faints", "works"]
#     elif quantity != 1 and tense == "present":
#         verb = ["eat", "run", "write", "paint", "cry", "sleep", "faint", "work"]
#     elif quantity == 1 and tense == "future":
#         verb = ["will eat", "will run", "will write", "will paint", "will cry", "will sleep", "will work", "will faint"]
#     verbs = random.choice(verb)
#     return verbs

# def make_sentence(quantity, tense):
#     """Build and return a sentence with three words:
#     a determiner, a noun, and a verb. The grammatical
#     quantity of the determiner and noun will match the
#     number in the quantity parameter. The grammatical
#     quantity and tense of the verb will match the number
#     and tense in the quantity and tense parameters.
#     """
#     determiner = get_determiner(quantity)
#     noun = get_noun(quantity)
#     verb = get_verb(quantity, tense)

#     sentence = f"{determiner(quantity)} {noun(quantity)} {verb(quantity, tense)}" 
#     return sentence

# main()
import random

def main():
   
    # quantity = [1, 2]
    # tense = ["past", "present", "future"]
    # # sentence = creating_sentence(quantity, tense)

    # verb_sen = get_verb(quantity, tense)
    # noun_sen = get_noun(quantity)
    # determiner_sen = get_determiner(quantity)

    # sentence_constr = determiner_sen(quantity).captalize() + "" + noun_sen(quantity) + "" + verb_sen(quantity, tense)
    

    # singular_past_sen = sentence_constr(1, 1,  "past")
    # singular_present_sen = sentence_constr(1, 1, "present")
    # singular_future_sen = sentence_constr(1, 1, "future")
    # plural_past_sen = sentence_constr(2, 2, "past")
    # plural_present_sen = sentence_constr(2, 2, "present")
    # plural_future_sen = sentence_constr(2, 2, "future")
    
    # print()
    # print(singular_past_sen)
    # print(singular_present_sen)
    # print(singular_future_sen)
    # print(plural_past_sen)
    # print(plural_present_sen)
    # print(plural_future_sen)
    # print()
    quantity = ""
    tense = ""
    sentence_1_past = creating_sentence(1, "past")
    sentence_1_present = creating_sentence(1, "present")
    sentence_1_future = creating_sentence(1, "future")
    sentence_2_past = creating_sentence(2, "past")
    sentence_2_future = creating_sentence(2, "future")
    sentence_2_present = creating_sentence(2, "different")
 
    print(sentence_1_past)
    print(sentence_1_present)
    print(sentence_1_future)
    print(sentence_2_past)
    print(sentence_2_present)
    print(sentence_2_future)

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
        noun_word = ["gentlemens","Womens", "Mens", "class mates", "giraffes"]
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
    #Here I rote 
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


    #     sentence_1_sing_past = f"{determiner_sen_1.captalize()}  {noun_sen_1}  {verb_sen_past}"
    # sentence_1_sing_present = f"{determiner_sen_1.captalize()}  {noun_sen_1}  {verb_sen_present}"
    # sentence_1_sing_future = f"{determiner_sen_1.captalize()}  {noun_sen_1}  {verb_sen_future}"
    # sentence_2_plural_past = f"{determiner_sen_2.captalize()}  {noun_sen_2}  {verb_sen_past}"
    # sentence_2_plural_present = f"{determiner_sen_2.captalize()}  {noun_sen_2}  {verb_sen_plural_present}"
    # sentence_2_plural_future = f"{determiner_sen_2.captalize()}  {noun_sen_2}  {verb_sen_future}"
"""UMA PASTA SÓ PARA TESTE"""
# import random
# def main():
    
#     number = [1,2]
#     tense = ""
#     # number_p = number_n(1,1, "future") 

#     # print (number_p)
#     verb_sen_1 = get_verb(1)
#     noun_sen_1_pas = get_noun(1,"past")
   
#     print(f"{verb_sen_1} {noun_sen_1_pas}")
#     print()

# def get_verb(number):
#     if number == 1:
#         x = ["hello", "hi",]
#     elif number == 2:
#         x = ["what's up", "how are you doing"]
#     else:
#         x = ["good bye", "bye"]
#     word = random.choice(x)
#     return word

# def get_noun (number, tense):
#     if number == 1 and tense == "past":
#         x = ["hello", "hi",]
#     elif number == 1 and tense == "present":
#         x = ["what's up", "how are you doing"]
#     else:
#         x = ["good bye", "bye"]
#     word = random.choice(x)
#     return word

# # def number_n(number, tense):

# #     verb_sen = get_verb(number, tense)
# #     noun_sen = get_noun(number)
   
# #     sentence_1_past = noun_sen(1).captalize() + "" + verb_sen(1, "past")
# #     sentence_2_future = noun_sen(2).captalize() + "" + verb_sen(2, "future")
# #     return sentence_1_past, sentence_2_future 

# main() 


    # if number == 1:
    #     x = ["hello", "hi",]
    # elif number == 2:
    #     x = ["what's up", "how are you doing"]
    # else:
    #     x = ["good bye", "bye"]
    # word = random.choice(x)
    # return word

    # if quantity == 1 or 2 and tense == "past":
    #     verb = ["ate","ran", "rote", "painted", "cried", "slept", "fainted", "worked"]
    # elif quantity == 1 and tense == "present":
    #     verb = ["eats", "runs", "writes", "paints", "crys", "sleeps", "faints", "works"]
    # elif quantity != 1 and tense == "present":
    #     verb = ["eat", "run", "write", "paint", "cry", "sleep", "faint", "work"]
    # elif quantity == 1 or 2 and tense == "future":
    #     verb = ["will eat", "will run", "will write", "will paint", "will cry", "will sleep", "will work", "will faint"] 
    # verb_random = random.choice(verb)
    # return verb_random


