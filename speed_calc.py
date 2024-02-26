from time import * #type: ignore
import random as r
import re 


def mistake(r_list,q_list):
    counter = 0
    for i in range (len(q_list)):
        try:
            if q_list[i] != r_list[i]:
                counter += 1
        except Exception as e:
            counter += 1

    if len(r_list) > len(q_list): counter = counter + len(r_list)- len(q_list)
    return counter


test = ['Hello this is the statement 1','This is the second statement ', 'This is the 3rd test statement'] #List of all the text to display for typing speed test.

test_choice = r.choice(test)
print("\n*******Typing speed calculator*******")
print()
print(test_choice)
print()
check1 = time()
response = input("Enter the above text: ")
check2 = time()
time_taken = round((check2-check1),2)

print(f"Total time taken:{time_taken}")
words_per_speed = round(len(response)/time_taken,2)
print(f"Total words per seed:{words_per_speed}")

print(f"Wrong words counted: {mistake(response,test_choice)}")
