"""A loop is used to execute a block of code repeatedly until a condition is satisfied.
Loops help avoid writing the same code again and again."""

#for loop
#used when the number of iterations is known
for i in range(1, 6):
    print(i,end=",")

#while loop
attempts = 1

while attempts <= 3:
    print("Eligibility check attempt:", attempts)
    attempts += 1

#loop control statements
print("-------------")
#break:- stops the loop completely
for i in range(1, 6):
    if i == 3:
        break
    print(i)
print("-----------")
#continue:- skips current iteration
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
