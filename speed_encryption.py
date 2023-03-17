import random,time,os

characters_in_order = [x for x in range(0,2**8)]

def to_list(data):
    t=type(data)
    if t==str:
        data=[ord(i)for i in data]
    elif t==bytes or t==bytearray:
        data=list(data)
    else:
        raise ValueError("No numbers allowed.")
    return data

def switch(data,rows=2):
    for i in range(0,len(data)):
        i+=1
        if i%rows==0:
            ls=data[i-rows:i]
            ls.reverse()
            data[i-rows:i]=ls
    return data

def reverse(data):
    data.reverse()
    return data

def encrypt(data,seed):
    random.seed(seed)
    shuffled_list = characters_in_order.copy()
    random.shuffle(shuffled_list)
    result=[]
    for i in data:
        result.append(shuffled_list[i])
    return result

def decrypt(data,seed):
    random.seed(seed)
    shuffled_list = characters_in_order.copy()
    random.shuffle(shuffled_list)
    result=[]
    #data=[i for i in data]
    for i in data:
        result.append(characters_in_order[shuffled_list.index(i)])
    return result

def obfuscate(data,key=0):
    data=switch(data)
    data=reverse(data)
    data=encrypt(data,key)
    return data

def unobfuscate(data,key=0):
    data=decrypt(data,key)
    data=reverse(data)
    data=switch(data)
    return data


def key_data(data):
    key=random.randint(0,255)
    print("key:",key)
    data=obfuscate(data,key)
    data.insert(0,key)
    return data

def dekey_data(data):
    key=data[0]
    del data[0]
    print("key:",key)
    data=unobfuscate(data,key)
    #print(data)
    return data

def to_string(data):
    s=""
    for i in data:
        s+=chr(i)
    return s

def to_bytes(data):
    data=bytearray(data)
    data=bytes(data)
    return data

###
#
##
#
###ncode 


data_in="hello"
print(data_in)
data_out=to_string(key_data(to_list(data_in)))
print(data_out)
data_back=to_string(dekey_data(to_list(data_out)))
print(data_back)

