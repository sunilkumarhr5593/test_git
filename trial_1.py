import pandas
import itertools
from math import log
import math
import numpy as np

# =============================================================================
#                       to calculate the prob of trigram
# =============================================================================

df_trigram = pandas.read_csv('count3l.txt',index_col=None, delim_whitespace=True, names=('trigram', 'prob'))
#print(df_trigram)

new_sum_3 = df_trigram.sum(axis = 0, skipna = False)  # sums all prob of trigram
total_prob_3 = (new_sum_3[0]) 
#print("The log value total occurence from the trigram data is: ",np.log2(total_prob_3))           # total prob of all bigram
#print()

avg_prob_3 = []

df1_3 = (df_trigram.iloc[:,1]) / (total_prob_3) #first row of data frame
avg_prob_3 = np.log2(df1_3)
#print(avg_prob_3)
#print(total_prob)  

trigram_prob = [] 
tprob= df_trigram.iloc[:,0]
trigram_prob = tprob                                                                 ##########
#print(bigram_prob)  

max_prob = max(avg_prob_3) 
#print("The log value of max prob is: ",max_prob)

dict_prob_3 = dict((trigram_prob[index], avg_prob_3[index]) for index in range(len(trigram_prob)))

import random
import string
from random import choices
from string import ascii_lowercase
from random import shuffle
import secrets

alphabets = 'abcdefghijklmnopqrstuvwxyz'
cipher = "SOWFBRKAWFCZFSBSCSBQITBKOWLBFXTBKOWLSOXSOXFZWWIBICFWUQLRXINOCIJLWJFQUNWXLFBSZXFBTXAANTQIFBFSFQUFCZFSBSCSBIMWHWLNKAXBISWGSTOXLXTSWLUQLXJBUUWLWISTBKOWLSWGSTOXLXTSWLBSJBUUWLFULQRTXWFXLTBKOWLBISOXSSOWTBKOWLXAKOXZWSBFIQSFBRKANSOWXAKOXZWSFOBUSWJBSBFTQRKAWSWANECRZAWJ"

alphabets_list = []
cipher_list = []

alphabets_list = alphabets
cipher_list = cipher.lower()
random_list = []
#random_list = random.sample((alphabets_list[i]) for i in range(len(alphabets_list)))

print("===========================First iteration=============================")

def key(stringLength=26):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.sample(letters, stringLength))

random_list = key()

key_1 = random_list
print("The initial random key is",key_1)
print()
# =============================================================================
# for i in range(len(alphabets_list)):
#     
#     random_list_1 = random.choice(random_list)
#     #random_list_1 = [i.split('\t')[0] for i in random_list] 
# =============================================================================
#print("The initial key is",key_1)
    
test_list = []

def hill_climb(key_1):
# =============================================================================
#     for i in range(len(alphabets_list)):
#     
#         random_list = random.choice(alphabets_list)
#         #random_list_1 = [i.split('\t')[0] for i in random_list] 
#         print(random_list)
# =============================================================================
    dictionary = dict((key_1[i], alphabets_list[i]) for i in range(len(key_1)))
    #print(dictionary)
    #test_list = dictionary.keys()
    #print(test_list)
    test_list_1 = []

    dic_ini = []
    for i in range(len(cipher_list)):
        
        crypt = dictionary.get(cipher_list[i])
        dic_ini = np.append(dic_ini, crypt)
    #print(dic_ini)
    res_join = " ".join(str(x) for x in dic_ini)
    res_replace = res_join.replace(" ", "")    
    #print(res_replace)
    
    n = 3
    temp = []
    out = [(res_replace[i:i+n]) for i in range(len(res_replace)+1 -n)]
    #print(out)
    temp = out
    #print(temp)  

    prob_k1 = 0
    for i in range(len(temp)):
        res = dict_prob_3.get(temp[i])
        #res1 = np.sum(res)
        prob_k1 = res+  prob_k1
        #prob_k1_list = np.append(prob_k1_list, res1)
    #print("The total prob of encrypted text is: ",add)
    #print("Prob using the key {} and the key is {}".format(prob_k1, "".join(str(x) for x in key_1)) )
    #print()
    return prob_k1
    #return prob_k1, "".join(str(x) for x in random_list)


random_list = list(random_list)
random_list[0], random_list[1] = random_list[1], random_list[0]
key_2 = random_list
#print("The next key is ","".join(str(x) for x in key_2))

print("The prob using key 1 is {} and the key is {}".format(hill_climb(key_1) ,"".join(str(x) for x in key_1)))
print("The prob using key 2 is {} and the key is {}".format(hill_climb(key_2) ,"".join(str(x) for x in key_2)))


if(hill_climb(key_1) > hill_climb(key_2)):
    #print("true")
    key_1 = list(key_1)
    key_1[1], key_1[2] = key_1[2], key_1[1]
    key_3 = key_1
    print("The prob using key 3 is {} and the key is {}".format(hill_climb(key_3) ,"".join(str(x) for x in key_3)))
    hill_climb(key_3)

else:
    #print("false")
    key_2 = list(key_2)
    key_2[24], key_2[25] = key_2[25], key_2[24]
    key_3 = key_2
    print("The prob using key 3 is {} and the key is {}".format(hill_climb(key_3) ,"".join(str(x) for x in key_3)))
    hill_climb(key_3)


if(hill_climb(key_3) > hill_climb(key_2)):
    #print("true")
    key_3 = list(key_3)
    key_3[7], key_3[8] = key_3[8], key_3[7]
    key_4 = key_3
    print("The prob using key 4 is {} and the key is {}".format(hill_climb(key_4) ,"".join(str(x) for x in key_4)))
    hill_climb(key_4)
else:
    #print("false")
    key_2 = list(key_2)
    key_2[11], key_2[12] = key_2[12], key_2[11]
    key_4 = key_2
    print("The prob using key 4 is {} and the key is {}".format(hill_climb(key_4) ,"".join(str(x) for x in key_4)))
    hill_climb(key_4)
    

if(hill_climb(key_4) > hill_climb(key_3)):
    #print("true")
    key_4 = list(key_4)
    key_4[14], key_4[15] = key_4[15], key_4[14]
    key_5 = key_4
    print("The prob using key 5 is {} and the key is {}".format(hill_climb(key_5) ,"".join(str(x) for x in key_5)))
    hill_climb(key_5) 
else:
    #print("false")
    key_3 = list(key_3)
    key_3[18], key_3[19] = key_3[19], key_3[18]
    key_5 = key_3
    print("The prob using key 5 is {} and the key is {}".format(hill_climb(key_5) ,"".join(str(x) for x in key_5)))
    hill_climb(key_5)  


if(hill_climb(key_5) > hill_climb(key_4)):
    #print("true")
    key_5 = list(key_5)
    key_5[20], key_5[21] = key_5[21], key_5[20]
    key_6 = key_5
    print("The prob using key 6 is {} and the key is {}".format(hill_climb(key_6) ,"".join(str(x) for x in key_6)))
    hill_climb(key_6)
    
else:
    #print("false")
    key_4 = list(key_4)
    key_4[21], key_4[22] = key_4[22], key_4[21]
    key_6 = key_4
    print("The prob using key 6 is {} and the key is {}".format(hill_climb(key_6) ,"".join(str(x) for x in key_6)))
    hill_climb(key_6)  


if(hill_climb(key_6) < hill_climb(key_5)):
    
    key_5 = list(key_5)
    key_5[22], key_5[23] = key_5[23], key_5[22]
    key_7 = key_5
    print("The prob using key 7 is {} and the key is {}".format(hill_climb(key_7) ,"".join(str(x) for x in key_7)))
    hill_climb(key_7)   
    
    if(hill_climb(key_7) < hill_climb(key_5)):
        key_5 = list(key_5)
        key_5[3], key_5[4] = key_5[4], key_5[3]
        key_8 = key_5
        print("The prob using key 8 is {} and the key is {}".format(hill_climb(key_8) ,"".join(str(x) for x in key_8)))
        hill_climb(key_8) 
        
        if(hill_climb(key_8) < hill_climb(key_5)):
            key_5 = list(key_5)
            key_5[7], key_5[8] = key_5[8], key_5[7]
            key_9 = key_5
            print("The prob using key 9 is {} and the key is {}".format(hill_climb(key_9) ,"".join(str(x) for x in key_9)))
            hill_climb(key_9)    
            
            if(hill_climb(key_8) < hill_climb(key_5)):
                key_5 = list(key_5)
                key_5[20], key_5[21] = key_5[0], key_5[25]
                key_10 = key_5
                print("The prob using key 10 is {} and the key is {}".format(hill_climb(key_10) ,"".join(str(x) for x in key_10)))
                hill_climb(key_10)                    
else:
    key_6 = list(key_6)
    key_6[22], key_6[23] = key_6[23], key_6[22]
    key_7 = key_6
    print("The prob using key 7 is {} and the key is {}".format(hill_climb(key_7) ,"".join(str(x) for x in key_7)))
    hill_climb(key_7)   

x1 = hill_climb(key_1)
x2 = hill_climb(key_2)
x3 = hill_climb(key_3)
x4 = hill_climb(key_4)
x5 = hill_climb(key_5)
x6 = hill_climb(key_6)
x7 = hill_climb(key_7)

y1 = "".join(str(x) for x in key_1)
y2 = "".join(str(x) for x in key_2)
y3 = "".join(str(x) for x in key_3)
y4 = "".join(str(x) for x in key_4)
y5 = "".join(str(x) for x in key_5)
y6 = "".join(str(x) for x in key_6)
y7 = "".join(str(x) for x in key_7)

test_list = x1,x2,x3,x4,x5,x6,x7

test_list_1 = y1,y2,y3,y4,y5,y6,y7

#print(test_list)
#print(test_list_1)
print()


dictionary1 = dict(zip(test_list_1, test_list))
#print(dictionary1)
print("The key with max prob is : {} and the value is : {} ".format(max(dictionary1, key=dictionary1.get),max([i for i in dictionary1.values()]) ))
#rint(max([i for i in dictionary1.values()]) )
# Create a dictionary from zip object
#dictOfWords = dict(dictionary1)
#print(dictOfWords)

y = max(dictionary1, key=dictionary1.get)
z = max([i for i in dictionary1.values()])

print(z, y)

print()
print("===========================Second iteration=============================")

def key(stringLength=26):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.sample(letters, stringLength))

random_list = key()

key_1 = random_list
print("The initial random key is",key_1)
print()
# =============================================================================
# for i in range(len(alphabets_list)):
#     
#     random_list_1 = random.choice(random_list)
#     #random_list_1 = [i.split('\t')[0] for i in random_list] 
# =============================================================================
#print("The initial key is",key_1)
    
test_list = []

def hill_climb(key_1):
# =============================================================================
#     for i in range(len(alphabets_list)):
#     
#         random_list = random.choice(alphabets_list)
#         #random_list_1 = [i.split('\t')[0] for i in random_list] 
#         print(random_list)
# =============================================================================
    dictionary = dict((key_1[i], alphabets_list[i]) for i in range(len(key_1)))
    #print(dictionary)
    #test_list = dictionary.keys()
    #print(test_list)
    test_list_1 = []

    dic_ini = []
    for i in range(len(cipher_list)):
        
        crypt = dictionary.get(cipher_list[i])
        dic_ini = np.append(dic_ini, crypt)
    #print(dic_ini)
    res_join = " ".join(str(x) for x in dic_ini)
    res_replace = res_join.replace(" ", "")    
    #print(res_replace)
    
    n = 3
    temp = []
    out = [(res_replace[i:i+n]) for i in range(len(res_replace)+1 -n)]
    #print(out)
    temp = out
    #print(temp)  

    prob_k1 = 0
    for i in range(len(temp)):
        res = dict_prob_3.get(temp[i])
        #res1 = np.sum(res)
        prob_k1 = res+  prob_k1
        #prob_k1_list = np.append(prob_k1_list, res1)
    #print("The total prob of encrypted text is: ",add)
    #print("Prob using the key {} and the key is {}".format(prob_k1, "".join(str(x) for x in key_1)) )
    #print()
    return prob_k1
    #return prob_k1, "".join(str(x) for x in random_list)


random_list = list(random_list)
random_list[0], random_list[1] = random_list[1], random_list[0]
key_2 = random_list
#print("The next key is ","".join(str(x) for x in key_2))

print("The prob using key 1 is {} and the key is {}".format(hill_climb(key_1) ,"".join(str(x) for x in key_1)))
print("The prob using key 2 is {} and the key is {}".format(hill_climb(key_2) ,"".join(str(x) for x in key_2)))


if(hill_climb(key_1) > hill_climb(key_2)):
    #print("true")
    key_1 = list(key_1)
    key_1[1], key_1[2] = key_1[2], key_1[1]
    key_3 = key_1
    print("The prob using key 3 is {} and the key is {}".format(hill_climb(key_3) ,"".join(str(x) for x in key_3)))
    hill_climb(key_3)

else:
    #print("false")
    key_2 = list(key_2)
    key_2[24], key_2[25] = key_2[25], key_2[24]
    key_3 = key_2
    print("The prob using key 3 is {} and the key is {}".format(hill_climb(key_3) ,"".join(str(x) for x in key_3)))
    hill_climb(key_3)


if(hill_climb(key_3) > hill_climb(key_2)):
    #print("true")
    key_3 = list(key_3)
    key_3[7], key_3[8] = key_3[8], key_3[7]
    key_4 = key_3
    print("The prob using key 4 is {} and the key is {}".format(hill_climb(key_4) ,"".join(str(x) for x in key_4)))
    hill_climb(key_4)
else:
    #print("false")
    key_2 = list(key_2)
    key_2[11], key_2[12] = key_2[12], key_2[11]
    key_4 = key_2
    print("The prob using key 4 is {} and the key is {}".format(hill_climb(key_4) ,"".join(str(x) for x in key_4)))
    hill_climb(key_4)
    

if(hill_climb(key_4) > hill_climb(key_3)):
    #print("true")
    key_4 = list(key_4)
    key_4[14], key_4[15] = key_4[15], key_4[14]
    key_5 = key_4
    print("The prob using key 5 is {} and the key is {}".format(hill_climb(key_5) ,"".join(str(x) for x in key_5)))
    hill_climb(key_5) 
else:
    #print("false")
    key_3 = list(key_3)
    key_3[18], key_3[19] = key_3[19], key_3[18]
    key_5 = key_3
    print("The prob using key 5 is {} and the key is {}".format(hill_climb(key_5) ,"".join(str(x) for x in key_5)))
    hill_climb(key_5)  


if(hill_climb(key_5) > hill_climb(key_4)):
    #print("true")
    key_5 = list(key_5)
    key_5[20], key_5[21] = key_5[21], key_5[20]
    key_6 = key_5
    print("The prob using key 6 is {} and the key is {}".format(hill_climb(key_6) ,"".join(str(x) for x in key_6)))
    hill_climb(key_6)
    
else:
    #print("false")
    key_4 = list(key_4)
    key_4[21], key_4[22] = key_4[22], key_4[21]
    key_6 = key_4
    print("The prob using key 6 is {} and the key is {}".format(hill_climb(key_6) ,"".join(str(x) for x in key_6)))
    hill_climb(key_6)  


if(hill_climb(key_6) < hill_climb(key_5)):
    
    key_5 = list(key_5)
    key_5[22], key_5[23] = key_5[23], key_5[22]
    key_7 = key_5
    print("The prob using key 7 is {} and the key is {}".format(hill_climb(key_7) ,"".join(str(x) for x in key_7)))
    hill_climb(key_7)   
    
    if(hill_climb(key_7) < hill_climb(key_5)):
        key_5 = list(key_5)
        key_5[3], key_5[4] = key_5[4], key_5[3]
        key_8 = key_5
        print("The prob using key 8 is {} and the key is {}".format(hill_climb(key_8) ,"".join(str(x) for x in key_8)))
        hill_climb(key_8) 
        
        if(hill_climb(key_8) < hill_climb(key_5)):
            key_5 = list(key_5)
            key_5[7], key_5[8] = key_5[8], key_5[7]
            key_9 = key_5
            print("The prob using key 9 is {} and the key is {}".format(hill_climb(key_9) ,"".join(str(x) for x in key_9)))
            hill_climb(key_9)    
            
            if(hill_climb(key_8) < hill_climb(key_5)):
                key_5 = list(key_5)
                key_5[20], key_5[21] = key_5[0], key_5[25]
                key_10 = key_5
                print("The prob using key 10 is {} and the key is {}".format(hill_climb(key_10) ,"".join(str(x) for x in key_10)))
                hill_climb(key_10)                    
else:
    key_6 = list(key_6)
    key_6[22], key_6[23] = key_6[23], key_6[22]
    key_7 = key_6
    print("The prob using key 7 is {} and the key is {}".format(hill_climb(key_7) ,"".join(str(x) for x in key_7)))
    hill_climb(key_7)  

x1 = hill_climb(key_1)
x2 = hill_climb(key_2)
x3 = hill_climb(key_3)
x4 = hill_climb(key_4)
x5 = hill_climb(key_5)
x6 = hill_climb(key_6)
x7 = hill_climb(key_7)

y1 = "".join(str(x) for x in key_1)
y2 = "".join(str(x) for x in key_2)
y3 = "".join(str(x) for x in key_3)
y4 = "".join(str(x) for x in key_4)
y5 = "".join(str(x) for x in key_5)
y6 = "".join(str(x) for x in key_6)
y7 = "".join(str(x) for x in key_7)

test_list = x1,x2,x3,x4,x5,x6,x7
test_list_1 = y1,y2,y3,y4,y5,y6,y7
#print(test_list)
print()


dictionary1 = dict(zip(test_list_1, test_list))
#print(dictionary1)
print("The key with max prob is : {} and the value is : {} ".format(max(dictionary1, key=dictionary1.get),max([i for i in dictionary1.values()]) ))
#rint(max([i for i in dictionary1.values()]) )
# Create a dictionary from zip object
#dictOfWords = dict(dictionary1)
#print(dictOfWords)
print()

y = max(dictionary1, key=dictionary1.get)
z = max([i for i in dictionary1.values()])

print(z, y)

print("===========================Third iteration=============================")

def key(stringLength=26):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.sample(letters, stringLength))

random_list = key()

key_1 = random_list
print("The initial random key is",key_1)
print()
# =============================================================================
# for i in range(len(alphabets_list)):
#     
#     random_list_1 = random.choice(random_list)
#     #random_list_1 = [i.split('\t')[0] for i in random_list] 
# =============================================================================
#print("The initial key is",key_1)
    
test_list = []

def hill_climb(key_1):
# =============================================================================
#     for i in range(len(alphabets_list)):
#     
#         random_list = random.choice(alphabets_list)
#         #random_list_1 = [i.split('\t')[0] for i in random_list] 
#         print(random_list)
# =============================================================================
    dictionary = dict((key_1[i], alphabets_list[i]) for i in range(len(key_1)))
    #print(dictionary)
    #test_list = dictionary.keys()
    #print(test_list)
    test_list_1 = []

    dic_ini = []
    for i in range(len(cipher_list)):
        
        crypt = dictionary.get(cipher_list[i])
        dic_ini = np.append(dic_ini, crypt)
    #print(dic_ini)
    res_join = " ".join(str(x) for x in dic_ini)
    res_replace = res_join.replace(" ", "")    
    #print(res_replace)
    
    n = 3
    temp = []
    out = [(res_replace[i:i+n]) for i in range(len(res_replace)+1 -n)]
    #print(out)
    temp = out
    #print(temp)  

    prob_k1 = 0
    for i in range(len(temp)):
        res = dict_prob_3.get(temp[i])
        #res1 = np.sum(res)
        prob_k1 = res+  prob_k1
        #prob_k1_list = np.append(prob_k1_list, res1)
    #print("The total prob of encrypted text is: ",add)
    #print("Prob using the key {} and the key is {}".format(prob_k1, "".join(str(x) for x in key_1)) )
    #print()
    return prob_k1
    #return prob_k1, "".join(str(x) for x in random_list)


random_list = list(random_list)
random_list[0], random_list[1] = random_list[1], random_list[0]
key_2 = random_list
#print("The next key is ","".join(str(x) for x in key_2))

print("The prob using key 1 is {} and the key is {}".format(hill_climb(key_1) ,"".join(str(x) for x in key_1)))
print("The prob using key 2 is {} and the key is {}".format(hill_climb(key_2) ,"".join(str(x) for x in key_2)))


if(hill_climb(key_1) > hill_climb(key_2)):
    #print("true")
    key_1 = list(key_1)
    key_1[1], key_1[2] = key_1[2], key_1[1]
    key_3 = key_1
    print("The prob using key 3 is {} and the key is {}".format(hill_climb(key_3) ,"".join(str(x) for x in key_3)))
    hill_climb(key_3)

else:
    #print("false")
    key_2 = list(key_2)
    key_2[24], key_2[25] = key_2[25], key_2[24]
    key_3 = key_2
    print("The prob using key 3 is {} and the key is {}".format(hill_climb(key_3) ,"".join(str(x) for x in key_3)))
    hill_climb(key_3)


if(hill_climb(key_3) > hill_climb(key_2)):
    #print("true")
    key_3 = list(key_3)
    key_3[7], key_3[8] = key_3[8], key_3[7]
    key_4 = key_3
    print("The prob using key 4 is {} and the key is {}".format(hill_climb(key_4) ,"".join(str(x) for x in key_4)))
    hill_climb(key_4)
else:
    #print("false")
    key_2 = list(key_2)
    key_2[11], key_2[12] = key_2[12], key_2[11]
    key_4 = key_2
    print("The prob using key 4 is {} and the key is {}".format(hill_climb(key_4) ,"".join(str(x) for x in key_4)))
    hill_climb(key_4)
    

if(hill_climb(key_4) > hill_climb(key_3)):
    #print("true")
    key_4 = list(key_4)
    key_4[14], key_4[15] = key_4[15], key_4[14]
    key_5 = key_4
    print("The prob using key 5 is {} and the key is {}".format(hill_climb(key_5) ,"".join(str(x) for x in key_5)))
    hill_climb(key_5) 
else:
    #print("false")
    key_3 = list(key_3)
    key_3[18], key_3[19] = key_3[19], key_3[18]
    key_5 = key_3
    print("The prob using key 5 is {} and the key is {}".format(hill_climb(key_5) ,"".join(str(x) for x in key_5)))
    hill_climb(key_5)  


if(hill_climb(key_5) > hill_climb(key_4)):
    #print("true")
    key_5 = list(key_5)
    key_5[20], key_5[21] = key_5[21], key_5[20]
    key_6 = key_5
    print("The prob using key 6 is {} and the key is {}".format(hill_climb(key_6) ,"".join(str(x) for x in key_6)))
    hill_climb(key_6)
    
else:
    #print("false")
    key_4 = list(key_4)
    key_4[21], key_4[22] = key_4[22], key_4[21]
    key_6 = key_4
    print("The prob using key 6 is {} and the key is {}".format(hill_climb(key_6) ,"".join(str(x) for x in key_6)))
    hill_climb(key_6)  


if(hill_climb(key_6) < hill_climb(key_5)):
    
    key_5 = list(key_5)
    key_5[22], key_5[23] = key_5[23], key_5[22]
    key_7 = key_5
    print("The prob using key 7 is {} and the key is {}".format(hill_climb(key_7) ,"".join(str(x) for x in key_7)))
    hill_climb(key_7)   
    
    if(hill_climb(key_7) < hill_climb(key_5)):
        key_5 = list(key_5)
        key_5[3], key_5[4] = key_5[4], key_5[3]
        key_8 = key_5
        print("The prob using key 8 is {} and the key is {}".format(hill_climb(key_8) ,"".join(str(x) for x in key_8)))
        hill_climb(key_8) 
        
        if(hill_climb(key_8) < hill_climb(key_5)):
            key_5 = list(key_5)
            key_5[7], key_5[8] = key_5[8], key_5[7]
            key_9 = key_5
            print("The prob using key 9 is {} and the key is {}".format(hill_climb(key_9) ,"".join(str(x) for x in key_9)))
            hill_climb(key_9)    
            
            if(hill_climb(key_8) < hill_climb(key_5)):
                key_5 = list(key_5)
                key_5[20], key_5[21] = key_5[0], key_5[25]
                key_10 = key_5
                print("The prob using key 10 is {} and the key is {}".format(hill_climb(key_10) ,"".join(str(x) for x in key_10)))
                hill_climb(key_10)                    
else:
    key_6 = list(key_6)
    key_6[22], key_6[23] = key_6[23], key_6[22]
    key_7 = key_6
    print("The prob using key 7 is {} and the key is {}".format(hill_climb(key_7) ,"".join(str(x) for x in key_7)))
    hill_climb(key_7)  

x1 = hill_climb(key_1)
x2 = hill_climb(key_2)
x3 = hill_climb(key_3)
x4 = hill_climb(key_4)
x5 = hill_climb(key_5)
x6 = hill_climb(key_6)
x7 = hill_climb(key_7)

y1 = "".join(str(x) for x in key_1)
y2 = "".join(str(x) for x in key_2)
y3 = "".join(str(x) for x in key_3)
y4 = "".join(str(x) for x in key_4)
y5 = "".join(str(x) for x in key_5)
y6 = "".join(str(x) for x in key_6)
y7 = "".join(str(x) for x in key_7)

test_list = x1,x2,x3,x4,x5,x6,x7
test_list_1 = y1,y2,y3,y4,y5,y6,y7
#print(test_list)
print()


dictionary1 = dict(zip(test_list_1, test_list))
#print(dictionary1)
print("The key with max prob is : {} and the value is : {} ".format(max(dictionary1, key=dictionary1.get),max([i for i in dictionary1.values()]) ))
#rint(max([i for i in dictionary1.values()]) )
# Create a dictionary from zip object
#dictOfWords = dict(dictionary1)
#print(dictOfWords)
print()

print("===========================Fourth iteration=============================")

def key(stringLength=26):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.sample(letters, stringLength))

random_list = key()

key_1 = random_list
print("The initial random key is",key_1)
print()
# =============================================================================
# for i in range(len(alphabets_list)):
#     
#     random_list_1 = random.choice(random_list)
#     #random_list_1 = [i.split('\t')[0] for i in random_list] 
# =============================================================================
#print("The initial key is",key_1)
    
test_list = []

def hill_climb(key_1):
# =============================================================================
#     for i in range(len(alphabets_list)):
#     
#         random_list = random.choice(alphabets_list)
#         #random_list_1 = [i.split('\t')[0] for i in random_list] 
#         print(random_list)
# =============================================================================
    dictionary = dict((key_1[i], alphabets_list[i]) for i in range(len(key_1)))
    #print(dictionary)
    #test_list = dictionary.keys()
    #print(test_list)
    test_list_1 = []

    dic_ini = []
    for i in range(len(cipher_list)):
        
        crypt = dictionary.get(cipher_list[i])
        dic_ini = np.append(dic_ini, crypt)
    #print(dic_ini)
    res_join = " ".join(str(x) for x in dic_ini)
    res_replace = res_join.replace(" ", "")    
    #print(res_replace)
    
    n = 3
    temp = []
    out = [(res_replace[i:i+n]) for i in range(len(res_replace)+1 -n)]
    #print(out)
    temp = out
    #print(temp)  

    prob_k1 = 0
    for i in range(len(temp)):
        res = dict_prob_3.get(temp[i])
        #res1 = np.sum(res)
        prob_k1 = res+  prob_k1
        #prob_k1_list = np.append(prob_k1_list, res1)
    #print("The total prob of encrypted text is: ",add)
    #print("Prob using the key {} and the key is {}".format(prob_k1, "".join(str(x) for x in key_1)) )
    #print()
    return prob_k1
    #return prob_k1, "".join(str(x) for x in random_list)


random_list = list(random_list)
random_list[0], random_list[1] = random_list[1], random_list[0]
key_2 = random_list
#print("The next key is ","".join(str(x) for x in key_2))

print("The prob using key 1 is {} and the key is {}".format(hill_climb(key_1) ,"".join(str(x) for x in key_1)))
print("The prob using key 2 is {} and the key is {}".format(hill_climb(key_2) ,"".join(str(x) for x in key_2)))


if(hill_climb(key_1) > hill_climb(key_2)):
    #print("true")
    key_1 = list(key_1)
    key_1[1], key_1[2] = key_1[2], key_1[1]
    key_3 = key_1
    print("The prob using key 3 is {} and the key is {}".format(hill_climb(key_3) ,"".join(str(x) for x in key_3)))
    hill_climb(key_3)

else:
    #print("false")
    key_2 = list(key_2)
    key_2[24], key_2[25] = key_2[25], key_2[24]
    key_3 = key_2
    print("The prob using key 3 is {} and the key is {}".format(hill_climb(key_3) ,"".join(str(x) for x in key_3)))
    hill_climb(key_3)


if(hill_climb(key_3) > hill_climb(key_2)):
    #print("true")
    key_3 = list(key_3)
    key_3[7], key_3[8] = key_3[8], key_3[7]
    key_4 = key_3
    print("The prob using key 4 is {} and the key is {}".format(hill_climb(key_4) ,"".join(str(x) for x in key_4)))
    hill_climb(key_4)
else:
    #print("false")
    key_2 = list(key_2)
    key_2[11], key_2[12] = key_2[12], key_2[11]
    key_4 = key_2
    print("The prob using key 4 is {} and the key is {}".format(hill_climb(key_4) ,"".join(str(x) for x in key_4)))
    hill_climb(key_4)
    

if(hill_climb(key_4) > hill_climb(key_3)):
    #print("true")
    key_4 = list(key_4)
    key_4[14], key_4[15] = key_4[15], key_4[14]
    key_5 = key_4
    print("The prob using key 5 is {} and the key is {}".format(hill_climb(key_5) ,"".join(str(x) for x in key_5)))
    hill_climb(key_5) 
else:
    #print("false")
    key_3 = list(key_3)
    key_3[18], key_3[19] = key_3[19], key_3[18]
    key_5 = key_3
    print("The prob using key 5 is {} and the key is {}".format(hill_climb(key_5) ,"".join(str(x) for x in key_5)))
    hill_climb(key_5)  


if(hill_climb(key_5) > hill_climb(key_4)):
    #print("true")
    key_5 = list(key_5)
    key_5[20], key_5[21] = key_5[21], key_5[20]
    key_6 = key_5
    print("The prob using key 6 is {} and the key is {}".format(hill_climb(key_6) ,"".join(str(x) for x in key_6)))
    hill_climb(key_6)
    
else:
    #print("false")
    key_4 = list(key_4)
    key_4[21], key_4[22] = key_4[22], key_4[21]
    key_6 = key_4
    print("The prob using key 6 is {} and the key is {}".format(hill_climb(key_6) ,"".join(str(x) for x in key_6)))
    hill_climb(key_6)  


if(hill_climb(key_6) < hill_climb(key_5)):
    
    key_5 = list(key_5)
    key_5[22], key_5[23] = key_5[23], key_5[22]
    key_7 = key_5
    print("The prob using key 7 is {} and the key is {}".format(hill_climb(key_7) ,"".join(str(x) for x in key_7)))
    hill_climb(key_7)   
    
    if(hill_climb(key_7) < hill_climb(key_5)):
        key_5 = list(key_5)
        key_5[3], key_5[4] = key_5[4], key_5[3]
        key_8 = key_5
        print("The prob using key 8 is {} and the key is {}".format(hill_climb(key_8) ,"".join(str(x) for x in key_8)))
        hill_climb(key_8) 
        
        if(hill_climb(key_8) < hill_climb(key_5)):
            key_5 = list(key_5)
            key_5[7], key_5[8] = key_5[8], key_5[7]
            key_9 = key_5
            print("The prob using key 9 is {} and the key is {}".format(hill_climb(key_9) ,"".join(str(x) for x in key_9)))
            hill_climb(key_9)    
            
            if(hill_climb(key_8) < hill_climb(key_5)):
                key_5 = list(key_5)
                key_5[20], key_5[21] = key_5[0], key_5[25]
                key_10 = key_5
                print("The prob using key 10 is {} and the key is {}".format(hill_climb(key_10) ,"".join(str(x) for x in key_10)))
                hill_climb(key_10)                    
else:
    key_6 = list(key_6)
    key_6[22], key_6[23] = key_6[23], key_6[22]
    key_7 = key_6
    print("The prob using key 7 is {} and the key is {}".format(hill_climb(key_7) ,"".join(str(x) for x in key_7)))
    hill_climb(key_7)    

x1 = hill_climb(key_1)
x2 = hill_climb(key_2)
x3 = hill_climb(key_3)
x4 = hill_climb(key_4)
x5 = hill_climb(key_5)
x6 = hill_climb(key_6)
x7 = hill_climb(key_7)

y1 = "".join(str(x) for x in key_1)
y2 = "".join(str(x) for x in key_2)
y3 = "".join(str(x) for x in key_3)
y4 = "".join(str(x) for x in key_4)
y5 = "".join(str(x) for x in key_5)
y6 = "".join(str(x) for x in key_6)
y7 = "".join(str(x) for x in key_7)

test_list = x1,x2,x3,x4,x5,x6,x7
test_list_1 = y1,y2,y3,y4,y5,y6,y7
#print(test_list)
print()


dictionary1 = dict(zip(test_list_1, test_list))
#print(dictionary1)
print("The key with max prob is : {} and the value is : {} ".format(max(dictionary1, key=dictionary1.get),max([i for i in dictionary1.values()]) ))
#rint(max([i for i in dictionary1.values()]) )
# Create a dictionary from zip object
#dictOfWords = dict(dictionary1)
#print(dictOfWords)
print()

print("===========================Fifth iteration=============================")

def key(stringLength=26):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.sample(letters, stringLength))

random_list = key()

key_1 = random_list
print("The initial random key is",key_1)
print()
# =============================================================================
# for i in range(len(alphabets_list)):
#     
#     random_list_1 = random.choice(random_list)
#     #random_list_1 = [i.split('\t')[0] for i in random_list] 
# =============================================================================
#print("The initial key is",key_1)
    
test_list = []

def hill_climb(key_1):
# =============================================================================
#     for i in range(len(alphabets_list)):
#     
#         random_list = random.choice(alphabets_list)
#         #random_list_1 = [i.split('\t')[0] for i in random_list] 
#         print(random_list)
# =============================================================================
    dictionary = dict((key_1[i], alphabets_list[i]) for i in range(len(key_1)))
    #print(dictionary)
    #test_list = dictionary.keys()
    #print(test_list)
    test_list_1 = []

    dic_ini = []
    for i in range(len(cipher_list)):
        
        crypt = dictionary.get(cipher_list[i])
        dic_ini = np.append(dic_ini, crypt)
    #print(dic_ini)
    res_join = " ".join(str(x) for x in dic_ini)
    res_replace = res_join.replace(" ", "")    
    #print(res_replace)
    
    n = 3
    temp = []
    out = [(res_replace[i:i+n]) for i in range(len(res_replace)+1 -n)]
    #print(out)
    temp = out
    #print(temp)  

    prob_k1 = 0
    for i in range(len(temp)):
        res = dict_prob_3.get(temp[i])
        #res1 = np.sum(res)
        prob_k1 = res+  prob_k1
        #prob_k1_list = np.append(prob_k1_list, res1)
    #print("The total prob of encrypted text is: ",add)
    #print("Prob using the key {} and the key is {}".format(prob_k1, "".join(str(x) for x in key_1)) )
    #print()
    return prob_k1
    #return prob_k1, "".join(str(x) for x in random_list)


random_list = list(random_list)
random_list[0], random_list[1] = random_list[1], random_list[0]
key_2 = random_list
#print("The next key is ","".join(str(x) for x in key_2))

print("The prob using key 1 is {} and the key is {}".format(hill_climb(key_1) ,"".join(str(x) for x in key_1)))
print("The prob using key 2 is {} and the key is {}".format(hill_climb(key_2) ,"".join(str(x) for x in key_2)))


if(hill_climb(key_1) > hill_climb(key_2)):
    #print("true")
    key_1 = list(key_1)
    key_1[1], key_1[2] = key_1[2], key_1[1]
    key_3 = key_1
    print("The prob using key 3 is {} and the key is {}".format(hill_climb(key_3) ,"".join(str(x) for x in key_3)))
    hill_climb(key_3)

else:
    #print("false")
    key_2 = list(key_2)
    key_2[24], key_2[25] = key_2[25], key_2[24]
    key_3 = key_2
    print("The prob using key 3 is {} and the key is {}".format(hill_climb(key_3) ,"".join(str(x) for x in key_3)))
    hill_climb(key_3)


if(hill_climb(key_3) > hill_climb(key_2)):
    #print("true")
    key_3 = list(key_3)
    key_3[7], key_3[8] = key_3[8], key_3[7]
    key_4 = key_3
    print("The prob using key 4 is {} and the key is {}".format(hill_climb(key_4) ,"".join(str(x) for x in key_4)))
    hill_climb(key_4)
else:
    #print("false")
    key_2 = list(key_2)
    key_2[11], key_2[12] = key_2[12], key_2[11]
    key_4 = key_2
    print("The prob using key 4 is {} and the key is {}".format(hill_climb(key_4) ,"".join(str(x) for x in key_4)))
    hill_climb(key_4)
    

if(hill_climb(key_4) > hill_climb(key_3)):
    #print("true")
    key_4 = list(key_4)
    key_4[14], key_4[15] = key_4[15], key_4[14]
    key_5 = key_4
    print("The prob using key 5 is {} and the key is {}".format(hill_climb(key_5) ,"".join(str(x) for x in key_5)))
    hill_climb(key_5) 
else:
    #print("false")
    key_3 = list(key_3)
    key_3[18], key_3[19] = key_3[19], key_3[18]
    key_5 = key_3
    print("The prob using key 5 is {} and the key is {}".format(hill_climb(key_5) ,"".join(str(x) for x in key_5)))
    hill_climb(key_5)  


if(hill_climb(key_5) > hill_climb(key_4)):
    #print("true")
    key_5 = list(key_5)
    key_5[20], key_5[21] = key_5[21], key_5[20]
    key_6 = key_5
    print("The prob using key 6 is {} and the key is {}".format(hill_climb(key_6) ,"".join(str(x) for x in key_6)))
    hill_climb(key_6)
    
else:
    #print("false")
    key_4 = list(key_4)
    key_4[21], key_4[22] = key_4[22], key_4[21]
    key_6 = key_4
    print("The prob using key 6 is {} and the key is {}".format(hill_climb(key_6) ,"".join(str(x) for x in key_6)))
    hill_climb(key_6)  


if(hill_climb(key_6) < hill_climb(key_5)):
    
    key_5 = list(key_5)
    key_5[22], key_5[23] = key_5[23], key_5[22]
    key_7 = key_5
    print("The prob using key 7 is {} and the key is {}".format(hill_climb(key_7) ,"".join(str(x) for x in key_7)))
    hill_climb(key_7)   
    
    if(hill_climb(key_7) < hill_climb(key_5)):
        key_5 = list(key_5)
        key_5[3], key_5[4] = key_5[4], key_5[3]
        key_8 = key_5
        print("The prob using key 8 is {} and the key is {}".format(hill_climb(key_8) ,"".join(str(x) for x in key_8)))
        hill_climb(key_8) 
        
        if(hill_climb(key_8) < hill_climb(key_5)):
            key_5 = list(key_5)
            key_5[7], key_5[8] = key_5[8], key_5[7]
            key_9 = key_5
            print("The prob using key 9 is {} and the key is {}".format(hill_climb(key_9) ,"".join(str(x) for x in key_9)))
            hill_climb(key_9)    
            
            if(hill_climb(key_8) < hill_climb(key_5)):
                key_5 = list(key_5)
                key_5[20], key_5[21] = key_5[0], key_5[25]
                key_10 = key_5
                print("The prob using key 10 is {} and the key is {}".format(hill_climb(key_10) ,"".join(str(x) for x in key_10)))
                hill_climb(key_10)                    
else:
    key_6 = list(key_6)
    key_6[22], key_6[23] = key_6[23], key_6[22]
    key_7 = key_6
    print("The prob using key 7 is {} and the key is {}".format(hill_climb(key_7) ,"".join(str(x) for x in key_7)))
    hill_climb(key_7)  

x1 = hill_climb(key_1)
x2 = hill_climb(key_2)
x3 = hill_climb(key_3)
x4 = hill_climb(key_4)
x5 = hill_climb(key_5)
x6 = hill_climb(key_6)
x7 = hill_climb(key_7)

y1 = "".join(str(x) for x in key_1)
y2 = "".join(str(x) for x in key_2)
y3 = "".join(str(x) for x in key_3)
y4 = "".join(str(x) for x in key_4)
y5 = "".join(str(x) for x in key_5)
y6 = "".join(str(x) for x in key_6)
y7 = "".join(str(x) for x in key_7)

test_list = x1,x2,x3,x4,x5,x6,x7
test_list_1 = y1,y2,y3,y4,y5,y6,y7
#print(test_list)
print()


dictionary1 = dict(zip(test_list_1, test_list))
#print(dictionary1)
print("The key with max prob is : {} and the value is : {} ".format(max(dictionary1, key=dictionary1.get),max([i for i in dictionary1.values()]) ))
#rint(max([i for i in dictionary1.values()]) )
# Create a dictionary from zip object
#dictOfWords = dict(dictionary1)
#print(dictOfWords)
print()


