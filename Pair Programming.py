income = int(input("Please enter your taxable income: "))
income2 = int(input("Please enter taxable income of your husband/wife: "))
allowance = 132000

if income * 0.05 > 18000:
    mpf = 18000

elif income * 0.05 < 7100:
    mpf = 0

else:
    mpf = income * 0.05

if income2 * 0.05 > 18000:
    mpf2 = 18000

elif income2 * 0.05 < 7100:
    mpf2 = 0

else:
    mpf2 = income2 * 0.05


netchargeableincome = income - mpf - allowance
netchargeableincome2 = income2 - mpf2 - allowance
netchargeableincome3 = netchargeableincome + netchargeableincome2


if netchargeableincome <= 0:
    tax = 0
    print("You don't need to pay any tax")
else:
    if netchargeableincome <= 50000:
        tax = netchargeableincome * 0.02

    elif netchargeableincome <= 100000:
        tax = (netchargeableincome - 50000) * 0.06 + 1000

    elif netchargeableincome <= 150000:
        tax = (netchargeableincome - 100000) * 0.1 + 4000

    elif netchargeableincome <= 200000:
        tax = (netchargeableincome - 150000) * 0.14 + 9000

    else:
        tax = (netchargeableincome - 200000) * 0.17 + 16000

        if tax > (income - 18000) * 0.15:
            tax = (income - 18000) * 0.15

        if (netchargeableincome - 200000) * 0.17 + 16000 > ((income + 18000) * 0.15):
            tax = (income - 18000) * 0.15

    print("you have to pay", tax, "dollars in tax under separate taxation")

if netchargeableincome2 <= 0:
    tax2 = 0
    print("You don't need to pay any tax")
else:
    if netchargeableincome2 <= 50000:
        tax2 = netchargeableincome2 * 0.02

    elif netchargeableincome2 <= 100000:
        tax2 = (netchargeableincome2 - 50000) * 0.06 + 1000

    elif netchargeableincome2 <= 150000:
        tax2 = (netchargeableincome2 - 100000) * 0.1 + 4000

    elif netchargeableincome2 <= 200000:
        tax2 = (netchargeableincome2 - 150000) * 0.14 + 9000

    else:
        tax2 = (netchargeableincome2 - 200000) * 0.17 + 16000

        if tax2 > (income2 - 18000) * 0.15:
            tax2 = (income2 - 18000) * 0.15

        if (netchargeableincome2 - 200000) * 0.17 + 16000 > ((income2 - 18000) * 0.15):
            tax2 = (income2 - 18000) * 0.15

    print("your husband/wife have to pay", tax2, "dollars in tax under separate taxation!")

if netchargeableincome3 <= 0:
    tax3 = 0
    print("You don't need to pay any tax")
else:
    if netchargeableincome3 <= 50000:
        tax3 = netchargeableincome3 * 0.02

    elif netchargeableincome3 <= 100000:
        tax3 = (netchargeableincome3 - 50000) * 0.06 + 1000

    elif netchargeableincome3 <= 150000:
        tax3 = (netchargeableincome3 - 100000) * 0.1 + 4000

    elif netchargeableincome3 <= 200000:
        tax3 = (netchargeableincome3 - 150000) * 0.14 + 9000

    else:
        tax3 = (netchargeableincome3 - 200000) * 0.17 + 16000

        if tax3 > netchargeableincome3 * 0.17:
            tax3 = (netchargeableincome3 - 200000) * 0.15

    print("you and your husband/wife have to pay", tax3, "dollars in tax in total for joint assessment!")


def Total_tax():
    Total_seperation_tax = tax + tax2
    print("you and your husband/wife have to pay", Total_seperation_tax,
          "dollars in tax in total under separate taxation!")


def suggestion():
    Total_seperation_tax = tax + tax2
    if Total_seperation_tax > tax3:
        print("you should pay tax under joint assessment")
    else:
        print("you should pay tax under separate taxation")


Total_tax()

suggestion()
