# 3.2.4-convert.py
# Program that takes is a float $ amount and returns its absolute amount in cent
# Author: Oksana Abrosimova

amount = abs(float(input("Please enter an amount:")))
cent_amount = amount * 100
print(f"That amount in cent is :{int(cent_amount)}")