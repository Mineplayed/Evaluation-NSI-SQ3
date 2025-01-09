words = ["bonjour", "il", "fait", "beau", "aujourd'hui", "c'est", "incroyable", "!"]

print("Question 1")
# Question 1

def question1():
    b_starter = []
    count = 0
    for i in words:    
        if i[0] == "b":
            b_starter.append(words[count])
        count = count + 1
    print(b_starter)

question1()

print("----------------------------------------")
print("Question 2")
# Question 2

def first_letter(list, letter):
    b_starter = []
    count = 0
    for i in list:    
        if i[0] == letter:
            b_starter.append(list[count])
        count = count + 1
    print(b_starter)

first_letter(words, input("Enter the starting letter : "))

print("----------------------------------------")
print("Question 3")
# Question 3

def number(list, letter):
    b_starter = []
    count = 0
    for i in list:    
        if i[0] == letter:
            count = count + 1
    print(count)
    
number(words, input("Enter the starting letter : "))