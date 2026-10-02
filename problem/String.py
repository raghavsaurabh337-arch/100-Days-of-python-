# str1="saurabh"
# str2="raghav"
# l1=list(str1)
# l2=list(str2)
# # print((type(l1)))
# for i in range (len(l1)):
        
#     for j in range(len(l2)):
#         if l1[i]==l2[j]:
#                 print(l1[i])
                
#         else:
#                 print("this is not match",l2[j])
                


str1 = "saurabh"
str2 = "raghav"

l1 = list(str1)
l2 = list(str2)

for i in range(len(l1)):
    found = False

    for j in range(len(l2)):
        if l1[i] == l2[j]:
            print("Match:", l1[i])
            found = True
            break

    if found == False:
        print("Not Match:", l1[i])