Tab = [["Bel Hair", 2546972642, 26989, 85697],["DoneTsou", 2555872541, 16235, 45689628],["Chiffon&Co", 9872822489, 35604, 652571]]

print("Question 1")
# Question 1

Tab.append(["Bul2gum", 4783654829, 4560, 25231])
print(Tab)

print("----------------------------------------")
print("Question 2")
# Question 2

def calculs_pourcentages():
    for i in Tab:
        temp_value_money = i[3]
        new_value_money = temp_value_money*10/100
        i.append(new_value_money)
    
print(Tab)
calculs_pourcentages()
    
print("----------------------------------------")
print("Question 3")
# Question 3

def indemnite():
    indemnite_list = []
    for i in Tab:
        temp_value_damages = i[2]
        temp_value_pct = i[4]
        if temp_value_damages >= temp_value_pct:
            check_indemnite = True
        else:
            check_indemnite = False
        indemnite_list.append(check_indemnite)
    return indemnite_list

indemnite_list = indemnite()
print(indemnite_list)

print("----------------------------------------")
print("Question 4")
# Question 4

def beneficiaires(tableau):
    siret = []
    
    for enterprise in tableau:
        siret.append(enterprise[1])
      
    print("Siret des bénéficaires : ")
    count = 0  
    for i in indemnite_list:
        if i == True:
            print(siret[count])
        count = count + 1
            
beneficiaires(Tab)

print("----------------------------------------")
print("Question 5")
# Question 5

def add_new_line():
        specs = []
        for i in range(len(Tab)):
            if i > 0:
                specs.append(int(input("Enter a number value : ")))
            else:
                specs.append(input("Enter a string value : "))
        Tab.append(specs)
        
add_new_line()
calculs_pourcentages()
indemnite_list = indemnite()
beneficiaires(Tab)
