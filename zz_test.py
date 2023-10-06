"""I use this file to test new things that I learn"""
x = 5
y = 6

if x == 5:
    print("a")

    if y == 6:
        print("b")
else:
    print("c")

    if y == 10:
        print("d")

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

# def number_n(number, tense):

#     verb_sen = get_verb(number, tense)
#     noun_sen = get_noun(number)
   
#     sentence_1_past = noun_sen(1).captalize() + "" + verb_sen(1, "past")
#     sentence_2_future = noun_sen(2).captalize() + "" + verb_sen(2, "future")
#     return sentence_1_past, sentence_2_future 

#main() 


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



#////////////
# from datetime import datetime
# birth = input("birth data : ")
# birth_date = datetime.strptime(birth, "%Y-%m-%D")

# age = datetime.now() - birth_date
# print(age)
# #26*09*2023
# from datetime import datetime

# def funtion_name_data_color(x, y):
#     print()
#     print(datetime.now())
#     math = x * y
#     return math

# #or :

 # def funtion_name_data_color(x, y):
 #     print()
 #     print(datetime.now())
#     print (x * y) 
    
    
# print("Part one!")
# print("jdsjdkslfjjkdlsjfkdsljfdksl")
# print("jdsjdkslfjjkdlsjfkdsljfdksl")
# print("jdsjdkslfjjkdlsjfkdsljfdksl")
# print("jdsjdkslfjjkdlsjfkdsljfdksl")
# print("jdsjdkslfjjkdlsjfkdsljfdksl")
# print("jdsjdkslfjjkdlsjfkdsljfdksl")
# print("x * y")
# fir = int(input("say a number to fir(x): "))
# sec = float(input("say a nother number to sec(y): "))
# math_one = funtion_name_data_color(fir, sec)
# print(math_one)
# #or
# #funtion_name_data_color(fir, sec )


# print()
# print("Part two!")
# print("jdsjdkslfjjkdlsjfkdsljfdksl")
# print("jdsjdkslfjjkdlsjfkdsljfdksl")
# print("jdsjdkslfjjkdlsjfkdsljfdksl")
# print("jdsjdkslfjjkdlsjfkdsljfdksl")
# print("jdsjdkslfjjkdlsjfkdsljfdksl")
# print("jdsjdkslfjjkdlsjfkdsljfdksl")
# print("jdsjdkslfjjkdlsjfkdsljfdksl")
# print()
# pri = int(input("say a number to pri(x): "))
# seg = float(input("say a nother number to seg(y): "))
# math_two = funtion_name_data_color(pri, seg)
# print(math_two)
# #or
# #funtion_name_data_color(pri, seg)

#25/09/2023 # file = open("teste.txt")

# for x in file:
#     part = x.split(",")
#     x = x.strip()
#     print(x[1])
#     print(part[3])
# goodbye = "I don't Know y you're saynig goodbye"
# from datetime import datetime
# curent_date = datetime.now()
# with open("teste.txt", "at") as adding:
#     print(f"{curent_date:%d/%m/%Y}", file=adding)
#     print("hello hello", file=adding)
#     print(goodbye, file=adding)

#25/09/3023 #Here We inported datetime 
# from datetime import datetime

# #Here we 
# current_date_and_time = datetime.now()
# day_of_week = current_date_and_time.weekday()

# print(day_of_week)
# print(current_date_and_time)

#18/09/2023: I learned to use the object "sep=" in print.

# x = "moon" 
# y = "sun" 
# print(x, y, sep="|")