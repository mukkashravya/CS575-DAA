def CalculateLpsArray(pattern,lps_array):
    length=len(pattern)

    #declaring an array with pattern length which can be used for pattern matching
    #lps_array=[0]*length
    #print(lps_array)

    #first element of the array will always be 0
    lps_array[0]=0
    i=0
    #j=1

    #while j<length:
    for j in range(1,length):
        if pattern[i]==pattern[j]:
            #print("coming")
            lps_array[j]=i+1
            i+=1
            #j+=1
        else:
            #print(i,j)
            # lps[j]=0
            # i=lps[i-1]
            # j+=1
            #if i=0 lps_array[i-1] could be neagtive, to avoid that
            if(i!=0):
                i=lps_array[i-1]
            else:
                lps_array[j]=i
                #j+=1

    print(lps_array)
    #return lps_array


def findMatchKmp(text,pattern):

    patlen=len(pattern)
    textlen=len(text)
    # array to store longest prefix suffix values which is used for comparision
    lps_array = [0] * patlen
    CalculateLpsArray(pattern,lps_array)
    print(lps_array)
    #pointers for pattern and text to compare both
    i=0
    j=0
    #variable decalred if the pattern found in text
    found=0

    while i<textlen:
        if text[i]==pattern[j]:
            i+=1
            j+=1
        else:
            if j!=0:
                j=lps_array[j-1]
            else:
                i+=1
        if j==patlen:
            #incrementing found variable as the pattern is found
            found+=1
            print("Pattern found in text at "+str(i-j) +"index")
            j=lps_array[j-1]

    #ptint when there is no match as found is incremented everytime when thers is a match found in text
    if(found==0):
        print("Match doesn't found")


print("please enter Text to search the pattern")
s1=str(input())
print("please enter pattern to be found in Text entered before")
s2=str(input())
findMatchKmp(s1,s2)