# Write a program that calculates how much of a tip to leave at a restaurant 
# and add ability to divide the check into a equal parts amount of number of 
# eople

bill_total = input('Total bill amount? ')
service_level = input('Level of service? (Please write one of the following: good, fair, or bad) ')
number_split = input('Split how many ways? ')


if service_level == "good":
     tip_amount = float(bill_total) * 0.20
     print(f'Tip amount: $ {tip_amount}')
     total_amount = float(bill_total) + tip_amount
     print(f'Total amount: $ {total_amount}')
     per_person_amount = total_amount / int(number_split)
     print(f'Amount per person: $ {per_person_amount}')

elif service_level == "fair":
     tip_amount = float(bill_total) * 0.15
     print(f'Tip amount: $ {tip_amount}')
     total_amount = float(bill_total) + tip_amount
     print(f'Total amount: $ {total_amount}')
     per_person_amount = total_amount / int(number_split)
     print(f'Amount per person: $ {per_person_amount}')

elif service_level == "bad":
     tip_amount = float(bill_total) * 0.10
     print(f'Tip amount: $ {tip_amount}')
     total_amount = float(bill_total) + tip_amount
     print(f'Total amount: $ {total_amount}')
     per_person_amount = total_amount / int(number_split)
     print(f'Amount per person: $ {per_person_amount}')