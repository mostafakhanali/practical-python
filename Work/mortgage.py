# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

print("month | total pay  | reminder")
while principal > 0:
    total_month += 1

    if (principal * (1+rate/12) - payment < 0):
        payment = principal * (1+rate/12)
        principal = 0
        total_paid = total_paid + payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

        if (total_month>=extra_payment_start_month) and (total_month<=extra_payment_end_month):
            principal = principal  - extra_payment
            total_paid = total_paid + extra_payment
    print(f"{total_month:4d}  | {total_paid:8.2f}   | {principal:8.2f}")

print('Total paid', round(total_paid,2))
print('Total month', total_month)