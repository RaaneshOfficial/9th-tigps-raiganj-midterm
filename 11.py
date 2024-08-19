og_price = float(input("Enter the original price:"))
discount_percent = float(input("Enter discount percentage(%):"))
final_price = og_price * (1 - discount_percent / 100)

print("Discounted amount:",final_price)