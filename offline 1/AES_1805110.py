from BitVector import *
import time
Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)
RoundConst = [
    [ 0x00, 0x00, 0x00, 0x00 ],
    [ 0x01, 0x00, 0x00, 0x00 ],
    [ 0x02, 0x00, 0x00, 0x00 ],
    [ 0x04, 0x00, 0x00, 0x00 ],
    [ 0x08, 0x00, 0x00, 0x00 ],
    [ 0x10, 0x00, 0x00, 0x00 ],
    [ 0x20, 0x00, 0x00, 0x00 ],
    [ 0x40, 0x00, 0x00, 0x00 ],
    [ 0x80, 0x00, 0x00, 0x00 ],
    [ 0x1B, 0x00, 0x00, 0x00 ],
    [ 0x36, 0x00, 0x00, 0x00 ],
    [ 0x6C, 0x00, 0x00, 0x00 ],
    [ 0xD8, 0x00, 0x00, 0x00 ],
    [ 0xAB, 0x00, 0x00, 0x00 ],
    [ 0x4D, 0x00, 0x00, 0x00 ],
    [ 0x9A, 0x00, 0x00, 0x00 ]
]

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]
encryptionTime=0
decryptionTime=0
KeySceduleTime=0
PlainTextAscii=""
PlainTextHex=""
KeyAscii=""
KeyHex=""
CypherTextAscii=""
CypherTextHex=""
deCypherTextAscii=""
deCypherTextHex=""
def printMatrix(input):
    for j in range(4):
        for i in range(4) :
            print(hex(input[j][i]),end=" ")
        print('\n')

def convertToMatrix(input) :
    hexInput=[]
    hexMatrix=[]
    input=input.ljust(16,'\0')
    #print("inside convert to hex matrix", input)
    for j in range(4):
        hexInput = []
        for i in range(j,len(input),4) :
            hexInput.append(ord(input[i]))
        hexMatrix.append(hexInput)
    #printMatrix(hexMatrix)
    return hexMatrix

def shifRowLeftN(row,n):
     shift_amount = n
     shifted_row = row[shift_amount:] + row[:shift_amount]
     return shifted_row


def shifRowRightN(row, n):
    shift_amount = n
    shifted_row = row[-shift_amount:] + row[:-shift_amount]
    return shifted_row

def shiftRight(mat) :
    for i in range(4):
        mat[i]=shifRowRightN(mat[i],i)
    return mat
def shiftLetf(mat):
    for i in range(4):
        mat[i]=shifRowLeftN(mat[i],i)
    return mat

def addRoundKey(mat,round) :
    return

def subBytes(mat) :
    subByte=[]
    
    for i in range(4):
        rowByte=[]
        for j in range(4):
            rowByte.append(Sbox[mat[i][j]])
        subByte.append(rowByte)
    return subByte
def invSubBytes(mat) :
    subByte=[]
    
    for i in range(4):
        rowByte=[]
        for j in range(4):
            rowByte.append(InvSbox[mat[i][j]])
        subByte.append(rowByte)
    return subByte
def transposeMatrix(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
def generateKeys(stringKey) : 
    global KeySceduleTime
    global KeyAscii,KeyHex
    #split into byte sized array
    stringKey=stringKey.ljust(16,'\0')
    stringKey=stringKey[:16]
    mat=convertToMatrix(stringKey)
    
    KeyAscii=stringKey
    KeyHex=printMatrixAsHex(mat)
    
    time1=time.time()
    allKeys=[mat]
    #round 0
   
    for round in range(1,11) :
        
        newWords=[]
        
        oldWords=[[allKeys[round-1][j][i]for j in range(4)]for i in range(4)]
        
        for i in range (4):
            
            if i==0 :
                #do your thing
                modifiedWord3=oldWords[-1]
                #print("modified word 3",[hex(modifiedWord3[i]) for i in range(4)])
                 #shiftRows
                
                modifiedWord3=shifRowLeftN(modifiedWord3,1)
                #print("modified word 3 after shift",[hex(modifiedWord3[i]) for i in range(4)])
                #subBytes
                modifiedWord3=[Sbox[element]for element in modifiedWord3]
                #print("modified word 3 after sub bytes",[hex(modifiedWord3[i]) for i in range(4)])
                
                #addRoundConstant
                modifiedWord3= [modifiedWord3[i]^RoundConst[round][i] for i in range(4)]
                #print("modified word 3 after round const",[hex(modifiedWord3[i]) for i in range(4)])
               
                newWord=[oldWords[0][i]^modifiedWord3[i] for i in range(4)]              
               
                newWords.append(newWord)
                
            else :
                newWord=[newWords[i-1][j]^oldWords[i][j] for j in range(4)]
                #print("new word",[hex(newWord[i]) for i in range(4)])
                newWords.append(newWord)

        #printMatrix(newWords)
        #allKeys[round]=newWords
        allKeys.append(transposeMatrix(newWords))
    # for i in range(11) :
    #     print("key",i)
    #     printMatrix(allKeys[i])
    time2=time.time()
    KeySceduleTime=time2-time1
    return allKeys
def xorOperation(mat1,mat2) :
    matNew=[]
    for i in range(4):
        matNew.append([])
        for j in range(4):
            matNew[i].append(mat1[i][j] ^ mat2[i][j])
    return matNew
def mixColumns(mat) :
    AES_mod = BitVector(bitstring='100011011')
    matNew=[]
    for i in range(4):
        matNew.append([])
        for j in range(4):
            matNew[i].append(0)
    for i in range(4):
        for j in range(4):
            for k in range(4):
                val=Mixer[i][k].gf_multiply_modular(BitVector(intVal=mat[k][j]),AES_mod,8)
                matNew[i][j] ^=val.intValue()
    
    return matNew
def invMixColumns(mat) :    
    AES_mod = BitVector(bitstring='100011011')
    matNew=[]
    for i in range(4):
        matNew.append([])
        for j in range(4):
            matNew[i].append(0)
    for i in range(4):
        for j in range(4):
            for k in range(4):
                val=InvMixer[i][k].gf_multiply_modular(BitVector(intVal=mat[k][j]),AES_mod,8)
                matNew[i][j] ^=val.intValue()

    return matNew
def printMatrixAsString(input):
    str=""
    for j in range(4):
        for i in range(4) :
            #print(chr(input[i][j]),end="")
            str+=chr(input[i][j])
    return str        
def printMatrixAsHex(input):
    str=""
    for j in range(4):
        for i in range(4) :
            #print(hex(input[i][j])[2:],end="")       
            str+=hex(input[i][j])[2:]
    return str        
def encryptChunk(chunk,keys) :
   
    mat=convertToMatrix(chunk)
    global PlainTextAscii,PlainTextHex,CypherTextAscii,CypherTextHex
    PlainTextAscii+=printMatrixAsString(mat)
    PlainTextHex+=printMatrixAsHex(mat)
    #round 0
    mat=xorOperation(mat,keys[0])
    
   
    for round in range(1,10) :
        #print("round",round)
        #subBytes
        #print("after sub bytes")
        mat=subBytes(mat)
        ##printMatrix(mat)
        #shiftRows
        mat=shiftLetf(mat)
        #print("after shift rows")
        #printMatrix(mat)
        
       
        #mixColumns
        mat=mixColumns(mat)
        
        #print("after mix columns")
        #printMatrix(mat)
        #addRoundKey
        
        mat=xorOperation(mat,keys[round])
        #print("after xor ")
        #printMatrix(mat)
        
    #round 10
    #print("round",10)
   
    mat=subBytes(mat)
    mat=shiftLetf(mat)
    mat=xorOperation(mat,keys[10])
    
    CypherTextAscii+=printMatrixAsString(mat)
    
    CypherTextHex+=printMatrixAsHex(mat)
    return printMatrixAsString(mat)
def encrypt(text,keyString) :
    encryptedChunk=""
    global encryptionTime
    
    keys=generateKeys(keyString)
    
    time1=time.time()
    for i in range(0,len(text),16) :   
        chunk=text[i:i+16]
        
        #encrypt the chunk
        if len(chunk)<16 :
            chunk=chunk.ljust(16,'\0')
        encryptedChunk+=encryptChunk(chunk,keys)
    time2=time.time()
    encryptionTime=time2-time1    
    return encryptedChunk
        
        
    
    
def decrypt(ciphertext,keyString) :
    global decryptionTime
    keys=generateKeys(keyString)
    decryptedChunk=""
    time1=time.time()
    for i in range(0,len(ciphertext),16) :   
        chunk=ciphertext[i:i+16]
        
        #encrypt the chunk
        if len(chunk)<16 :
            chunk=chunk.ljust(16,'\0')
        decryptedChunk+=decryptChunk(chunk,keys)
        

    time2=time.time()
    decryptionTime=time2-time1
    
    return decryptedChunk
def decryptChunk(chunk,keys) :
    global deCypherTextAscii,deCypherTextHex 
    mat=convertToMatrix(chunk)
   
    #round 0
    mat=xorOperation(mat,keys[10])
    mat=shiftRight(mat)
    mat=invSubBytes(mat)
    #print("round",0)
    #printMatrix(mat)
    for round in range(1,10) :
        #print("round",round)
        #subBytes
        #print("after sub bytes")
        mat=xorOperation(mat,keys[10-round])
        ##printMatrix(mat)
        #shiftRows
        mat=invMixColumns(mat)
        #print("after shift rows")
        #printMatrix(mat)
        
       
        #mixColumns
        mat=shiftRight(mat)
        
        #print("after mix columns")
        #printMatrix(mat)
        #addRoundKey
        
        mat=invSubBytes(mat)
        #print("after xor ")
        #printMatrix(mat)
        
    #round 10
    #print("round",10)
   
   
    mat=xorOperation(mat,keys[0])
    #printMatrix(mat)
    
    plainText=printMatrixAsString(mat)
    deCypherTextAscii+=plainText
    deCypherTextHex+=printMatrixAsHex(mat)
    
    return plainText
if __name__ == '__main__':

    
    #plainText = input()
    
    keys="BUET CSE18 Batch"
    cyphertext=encrypt("Can They Do This",keys)
    decrypt(cyphertext,keys)
    #print plaintext
    print("Plain Text :")
    print("In ASCCI : ",PlainTextAscii)
    print("In Hex : ",PlainTextHex)
    #print key
    print("Key : ")
    print("In ASCCI : ",KeyAscii)
    print("In Hex :",KeyHex)
    #print cyphertext
    print("Cypher Text : ")
    print("In ASCCI : ",CypherTextAscii)
    print("In Hex : ",CypherTextHex)
    #print decrypted text
    print("Decrypted Text : ")
    print("In ASCCI : ",deCypherTextAscii)
    print("In Hex : ",deCypherTextHex)

    #print time taken for encryption and decryption
    print("Execution Time Details : ")
    print("key generation Time : ",KeySceduleTime)
    print("Encryption Time : ",encryptionTime)
    print("Decryption Time : ",decryptionTime)