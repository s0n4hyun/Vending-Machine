#Vending Machine Simulator

price = int(input("상품 가격: "))
input_amount = int(input("지불 가격: "))
money_remain = input_amount - price

money_1000 = money_remain // 1000
money_remain = money_remain % 1000

money_500 = money_remain // 500
money_remain = money_remain % 500

money_100 = money_remain // 100
money_reman = money_remain % 100

money_50 = money_remain // 50
money_remain = money_remain % 50

print(" ")
print(f"1000원: {money_1000} 장")
print(f"500원: {money_500} 개")
print(f"100원: {money_100} 개")
print(f"50원: {money_50} 개")
