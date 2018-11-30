#CHALLENGE 1: REVERSE STRING
'''
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
'''

def reverse_string(string):
    return string[::-1]
    
##############################################################

#CHALLENGE 2: LIST CHECK

'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''

def list_check(lst):
    for x in lst:
        if type(x)!= list:
            return False
    return True

##############################################################

#CHALLENGE 3: REMOVE EVERY OTHER

'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''

def remove_every_other(lst):
    new_list = []
    go = "yes"
    for x in lst:
        if go == "yes":
            new_list.append(x)
            go = "no"
        else:
            go = "yes"
    return new_list
    
##############################################################

CHALLENGE 4: SUM PAIRS

'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''

def sum_pairs(lst1, num):
    lst = lst1
    for x in lst1:
        if num-x in lst1:
            return[x,num-x]
        else:
            lst.remove(x)
    return []

##############################################################

CHALLENGE 5: VOWEL COUNT

'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''

def vowel_count(string):
    lst = []
    dct = {}
    for x in string.lower():
        if x in "aeiou":
            lst.append(x)
    for x in lst:
       dct[x] = lst.count(x)
       
       
    return(dct)
    
##############################################################

CHALLENGE 6: TITLEIZE

'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''

def titleize(string):
    return " ".join([x[0].capitalize()+x[1:] for x in string.split(" ")])

##############################################################

CHALLENGE 7: FIND FACTORS

'''
find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]
find_factors(412146) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
'''

def find_factors(num):
    return [x for x in range(1, num+1) if num%x==0]
    
##############################################################

CHALLENGE 8: INCLUDES

'''
includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 
includes({ 'a': 1, 'b': 2 }, 1) # True 
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''

def includes(coll, val, index=0):
    if type(coll) == list or type(coll) == str:
        return val in coll[index:]
    elif type(coll) == dict:
        return val in coll.values()
    
##############################################################

CHALLENGE 9: TRUNCATE

'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''

def truncate(string, num):
    if num < 3:
        return "Truncation must be at least 3 characters."
    elif len(string)<num-3:
        return string
    return("{}...".format(string[:num-3]))
        
##############################################################


    
    
    
    
