print("The Love Calculator is calculating your score...")
name1 = 'David Beckham' # What is your name?
name2 = 'Victoria Beckham' # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()
true_count, love_count = 0, 0
for name in [name1_lower, name2_lower]:
    for letter in ["t","r","u","e"]:
        true_count += name.count(letter)
    for letter in ["l","o","v","e"]:    
        love_count += name.count(letter)
total_count = int(str(true_count) + str(love_count))
if total_count < 10 or total_count > 90:
    print(f"Your score is {total_count}, you go together like coke and mentos.")
elif total_count >= 40 and total_count <= 50:
    print(f"Your score is {total_count}, you are alright together.")
else:
    print(f"Your score is {total_count}.")
    