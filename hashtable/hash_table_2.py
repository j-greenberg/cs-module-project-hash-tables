
def my_hash(s): 
    string_bytes = s.encode()
    total = 0
    for b in string_bytes: 
        total += b
    
    return total

# choose some big random number, usually prime
# loop over the bytes of our string, and do something weird 
# return the weird result 

# "something weird" mean with the bits, which you'll learn in computer architecture 


def djb2(string): 
    hash_var = 5381 

    string_bytes = string.encode()

    for b in string_bytes: 
        hash_var = ((hash_var << 5) + hash_var) + b
    
    return hash_var

print (djb2('hello'))

    # def djb2(self, key): 
    #   hash = 5381
    #   for element in key: 
    #       hash = (hash * 33) + ord(element) 
    #   return hash


def fnv(s): 
    FNV_offset_basis = 1469581039346656037
    FNV_prime = 1099511628211

    hashed_var = FNV_offset_basis

    string_bytes = s.encode()

    for b in string_bytes: 
        hashed_var = hashed_var * FNV_prime
        hashed_var = hashed_var ^ b 

    return hashed_var

    # algorithm fnv-1 is
    #     hash := FNV_offset_basis do

    # for each byte_of_data to be hashed
    #     hash := hash × FNV_prime
    #     hash := hash XOR byte_of_data

    # return hash 