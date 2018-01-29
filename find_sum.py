#Find sum of all numbers in a file
import re
sum = 0
with open('text.txt') as fp:
    for line in fp:
        ll = re.findall('\d+', line) #Finds list of numbers in this line (\d+ => 1 or more continous digits
        sum_list = 0
        if len(ll) > 0:
            print(ll)
            for i in ll:
                sum_list = sum_list + int(i)
            print ("sum_list : ", sum_list)
            sum = sum + sum_list
print ("sum : ", sum)