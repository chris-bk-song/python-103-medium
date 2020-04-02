# Write a program that calculates how much of a tip to leave at a restaurant.

bill_total = input('Total bill amount? ')
service_level = input('Level of service? (Please write one of the following: good, fair, or bad) ')



if service_level == "good":
     tip_amount = float(bill_total) * 0.20
     print(f'Tip amount: $ {tip_amount}')
     total_amount = float(bill_total) + tip_amount
     print(f'Total amount: $ {total_amount}')

elif service_level == "fair":
     tip_amount = float(bill_total) * 0.15
     print(f'Tip amount: $ {tip_amount}')
     total_amount = float(bill_total) + tip_amount
     print(f'Total amount: $ {total_amount}')

elif service_level == "bad":
     tip_amount = float(bill_total) * 0.10
     print(f'Tip amount: $ {tip_amount}')
     total_amount = float(bill_total) + tip_amount
     print(f'Total amount: $ {total_amount}')

