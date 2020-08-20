"""
CP5632 Practical 1

Program to estimate electricity bill based on tariff number, daily usage and
billing period values provided by the user
"""

print("Electricity bill estimator 2.0")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff_no = int(input("Which tariff? 11 or 31: "))
while tariff_no != 11 and tariff_no != 31:
    print("Incorrect tariff number.")
    tariff_no = int(input("Which tariff? 11 or 31: "))
if tariff_no == 11:
    tariff_value = TARIFF_11
else:
    tariff_value = TARIFF_31

daily_use = float(input("Enter daily use in kWh: "))
billing_period = int(input("Enter number of billing days: "))

estimated_bill = tariff_value * daily_use * billing_period
print("Estimated bill: ${:.2f}".format(estimated_bill))
