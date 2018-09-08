'''
Created on Dec 21, 2017

@author: ishank
'''

def  decrypt(encrypted_message):
    
# #     knownEnding = "-Your friend, Alice"
#     knownEnding = "The quick brown fox jumps over the lazy dog"
#     key = ''
    decryptedMessage = ''
#     
# #     encryptedEnding = encrypted_message[-19:]
#     
#     encryptedEnding = "Bjj rwkcs dwpyp fwz ovors wxjs vje tcez fqg" 
# #     encryptedEnding = "-Atvt hrqgse, Cnikg"
#     
#     for i in range(len(encryptedEnding)):
#         if str.isalpha(encryptedEnding[i]):
#             rotation = ord(encryptedEnding[i]) - ord(knownEnding[i])
#             if rotation < 0:
#                 rotation = 26 + rotation
#             key += str(rotation)
#     
#     searchIndex = 1
#     print key
#     
#     tempKey = key
#     
#     while searchIndex < len(key):
#         position = key.find(key[0], searchIndex)
#         if position == -1:
#             break
#         
#         if key[:position] == key[position:position + len(key[:position])]:
#             newKey = key[:position]
#             while len(newKey) < len(key):
#                 newKey += newKey
#             if newKey[:len(key)] == key:
#                 key = key[:position]
#                 break
#             
#         searchIndex = position + 1
#     
    keyIndex = 0
#     key = tempKey[-len(key):]
#     print key
    key = "8251220"
    for c in encrypted_message:
        rotation = int(key[keyIndex])
        if not str.isalpha(c):
            decryptedMessage += c
            continue
        
        if str.isupper(c):
            if (ord(c) - rotation) < ord('A'):
                rotation = rotation - 26
        else:
            if (ord(c) - rotation) < ord('a'):
                rotation = rotation - 26
            
        decryptedMessage += chr(ord(c) - rotation)
        keyIndex = (keyIndex + 1) % len(key)
            
    
    return decryptedMessage  
    
    
    
    
# print decrypt("Otjfvknou kskgnl, K mbxg iurtsvcnb ksgq hoz atv. Vje xcxtyqrl vt ujg smewfv vrmcxvtg rwqr ju vhm ytsf elwepuqyez. -Atvt hrqgse, Cnikg")
# print decrypt("z. -Atvt hrqgse, Cnikg")

print decrypt("Bjj rwkcs dwpyp fwz ovors wxjs vje tcez fqg")







