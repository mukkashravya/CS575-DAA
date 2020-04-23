def computeLcs(s1,s2):
    m=len(s1)
    n=len(s2)
    #rows,cols=(m+1,n+1)
    #lcs_array=[[0]*cols]*rows
    lcs_array=[[0 for x in range(n+1)] for x in range(m+1)]
    letter_array = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                lcs_array[i][j]=0
                letter_array[i][j]=0
            elif s1[i-1]==s2[j-1]:
                lcs_array[i][j]=lcs_array[i-1][j-1]+1
                letter_array[i][j] = "D"
            elif lcs_array[i-1][j]>=lcs_array[i][j-1]:
                lcs_array[i][j]=lcs_array[i-1][j]
                letter_array[i][j] = "U"
            else:
                lcs_array[i][j] = lcs_array[i][j-1]
                letter_array[i][j] = "L"

    print(lcs_array)
    print(letter_array)
    lcs_length=lcs_array[m][n]
    print("The length of longest common subsequence is "+ str(lcs_length))
    lcs=[""]*(lcs_length)

    i=m
    j=n

    while i>0 and j>0:
        #print(i,j)
        if letter_array[i][j]=="D":
            lcs[lcs_length-1]=s1[i-1]
            #print(s1[i-1])
            i-=1
            j-=1
            lcs_length-=1
        elif letter_array[i][j]=="U":
            i-=1
        elif letter_array[i][j]=="L":
            j-=1

    if(len(lcs)>0):
        print("Longest common sub sequence of " + s1.upper() + " and " + s2.upper() + " is " +"".join(lcs).upper())
    else:
        print("No match found")



#s1="AGGTAB"
#s2="GXTXAYB"
print("please enter first string")
s1=str(input())
print("please enter second string")
s2=str(input())

computeLcs(s1,s2)
