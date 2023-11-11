import random, time
import math
def generateSafePrime(n) :
    while True :
        q=random.getrandbits(n-1)
        p=2*q +1
        if isPrime(p) and isPrime(q) :
            return p
        
def generatePrime(n) :
    while True :
        p=random.getrandbits(n)
        if isPrime(p) :
            return p
        
def isPrime(n,k=20) :
    if n==1 or n%2==0 :
        return False
    if n==2 :
        return True
    maxDivByTwo=0
    s=n-1
    while s % 2 == 0 :
        maxDivByTwo+=1
        s //=2
    for iteration in range(k):
        a=random.randrange(2,n-1)
        x=comuputeModularExpo(a,s,n)
        
       
        for r in range(maxDivByTwo) :
            
            y=comuputeModularExpo(x,2,n)
            if y==1 and x!=1 and x!=n-1 :
                return False
            x=y
            
        if y!=1 :
            return False
    return True

def generatePrimitiveRoot(minN,maxN,moduloPrime) :
    while True :
        i=random.randint(minN,maxN)
    
        if isPrimitiveRoot(i,moduloPrime) :
            return i
   
def isPrimitiveRoot(g,p) :
    if comuputeModularExpo(g,2,p)==1 or comuputeModularExpo(g,math.ceil((p-1)/2),p) ==1 :
            return False
    return True
def Compute_g_a(g,p,k) :
    a=generatePrime((math.ceil(k/2)))
  
    A = comuputeModularExpo(g, a, p)
    return A,a

def Compute_g_b(g,p,k) :
    b=generatePrime((math.ceil(k/2)))
  
    B = comuputeModularExpo(g, b, p)
    return B,b
def computeSharedKey(A_B,a_b,p) :
    s1 = comuputeModularExpo(A_B, a_b, p)
    return s1

def comuputeModularExpo(g,a,p) :
    
    result=1
    while a>0 : 
        if a&1 :
            result=(result*g)%p
        a >>=1
        g=(g*g)%p      
    return result          
if __name__ == '__main__':
    
    for k in [128,198,256] :
        computationTimePavg=0
        computationTimeGavg=0
        computationTimeAavg=0
        computationTimeaAvg=0
        computationTimeSavg=0
        for i in range(5) :
            startTimer = time.time()
            p=generateSafePrime(k)
            computationTimeP=time.time()-startTimer
            computationTimePavg+=computationTimeP
            
            startTimer = time.time()
            g=generatePrimitiveRoot(101,p-100,p)
            computationTimeG=time.time()-startTimer
            computationTimeGavg+=computationTimeG
            

            #compute a
            startTimer = time.time()
            a=generatePrime((math.ceil(k/2)))
            computationTimea=time.time()-startTimer
            computationTimeaAvg+=computationTimea

            #compute b
            
            b=generatePrime((math.ceil(k/2)))
           
           
            
            #compute A
            startTimer = time.time()
            A = comuputeModularExpo(g, a, p)
            computationTimeA=time.time()-startTimer
            
            computationTimeAavg+=computationTimeA

            #compute B
           
            B = comuputeModularExpo(g, b, p)
           
            # Generate the shared secrets

            startTimer = time.time()
            s1 = comuputeModularExpo(A, b, p)
            computationTimesS=time.time()-startTimer
            computationTimeSavg+=computationTimesS
            s2 = comuputeModularExpo(B, a, p)

            
                
        computationTimePavg=computationTimePavg/5
        computationTimeGavg=computationTimeGavg/5
        computationTimeAavg=computationTimeAavg/5
        computationTimeaAvg=computationTimeaAvg/5
        computationTimeSavg=computationTimeSavg/5
        print("keylength ", k)
        print("Average time for generating safe prime ",computationTimePavg)
        print("Average time for generating primitive root ",computationTimeGavg)
        print("Average time for generating a ",computationTimeaAvg)
        print("Average time for generating A ",computationTimeAavg)
        print("Average time for generating shared key ",computationTimeSavg)








