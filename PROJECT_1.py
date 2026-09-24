names = {
    1: "Combo Shahi Thali",
    2: "Samosa",
    3: "Vada Pav",
    4: "Chicken 65",
    5: "Paneer Tikka",
    6: "Achari Paneer",
    7: "Paneer Butter Masala",
    8: "Chole Bhature",
    9: "Rajma",
    10: "Pav Bhaji",
    11: "Dal Makhani",
    12: "Malai Kofta",
    13: "Palak Paneer",
    14: "Butter Chicken",
    15: "Chicken Biryani",
    16: "Chicken Curry",
    17: "Veg Biryani",
    18: "Veg Fried Rice",
    19: "Tandoor Roti",
    20: "Aloo Parantha",
    21: "Masala Dosa",
    22: "Idli Sambhar",
    23: "Gulab Jamun",
    24: "Rasmalai",
    25: "Brownie",
    26: "Ice Cream",
    27: "Fresh Juice",
    28: "Cold Coffee",
    29: "Masala Chai",
    30: "Cold Drink"
}

prices = {
    1: 1200,
    2: 55,
    3: 60,
    4: 220,
    5: 180,
    6: 380,
    7: 350,
    8: 150,
    9: 120,
    10: 350,
    11: 220, 12: 300, 13: 270, 14: 420, 15: 350,
    16: 380, 17: 280, 18: 200, 19: 180, 20: 120,
    21: 350, 22: 150, 23: 50, 24: 120, 25: 150,
    26: 100, 27: 100, 28: 130, 29: 50, 30: 60
}

print("══════════════  MAYURI  ══════════════")
name = input("What's your name: ")
print("Hello,", name, "What would you like to order?")
print()

print("════════════ MENU ════════════")
for i in range(1,31):
    print(i, names[i],": ₹", prices[i])
print()

print()

cart = {}

while True:
    choice = int(input("Enter item number (0 to finish): "))

    if choice == 0:
        break

    print(names[choice])
    quantity = int(input("Enter the quantity: "))

    if choice in cart:
        cart[choice] += quantity
    else:
        cart[choice] = quantity

print()
print("=" * 45)
print("MAYURI RESTAURANT".center(45))
print("=" * 45)

print("Customer:", name)
print("-" * 45)

print(f"{'Item':<20}{'Qty':>5}{'Price':>8}{'Amount':>10}")
print("-" * 45)

total = 0

for item in cart:
    quantity = cart[item]
    amount = prices[item] * quantity
    total += amount

    print(f"{names[item]:<20}{quantity:>5}{prices[item]:>8}{amount:>10}")

gst = total * 5 / 100
grand_total = total + gst

print("-" * 45)
print(f"{'Subtotal':<35}{total:>10.2f}")
print(f"{'GST (5%)':<35}{gst:>10.2f}")
print("=" * 45)
print(f"{'GRAND TOTAL':<35}{grand_total:>10.2f}")
print("=" * 45)
print("Thank you! Visit again".center(45))
