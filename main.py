#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total_cost = input('What is the total cost? \n')
total_people = input('How many people are splitting the bill? \n')

total_per_person = float(total_cost)/float(total_people) * 1.12
total_per_person = round(total_per_person,2)

print(f'Each person should pay {total_per_person:.2f}')

#End
