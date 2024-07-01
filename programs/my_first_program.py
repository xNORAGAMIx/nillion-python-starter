from nada_dsl import *

def nada_main():

    party1 = Party(name="Party1")
    
    my_int1 = SecretInteger(Input(name="my_int1", party=party1)) #original ley
    my_int2 = SecretInteger(Input(name="my_int2", party=party1)) #test key

    modulus = Integer(100000) #used for enscryption

    encrptedKey = Integer(67890) #using a key to encrypt the original key

    encrypt = (my_int1 + encrptedKey) % modulus #creating encrypt data using modulus

    decrypt = (encrypt - my_int2 + modulus) % modulus #creating decrypt data using the encrypt data
    
    #checking if the original key matches the decrypted key
    condition =  decrypt == my_int1 
    result = condition.if_else(Integer(1), Integer(0))

    #returns 1 if the key matches, else returns 0
    return [
        Output(result, "1 True, 0 False", party1)
        
    ]
