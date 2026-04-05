"""def student_marks(name, mark1, mark2, mark3):
      total_marks = mark1 + mark2 + mark3
      average = total_marks / 3
      percentage = (mark1 + mark2 + mark3) / 3
      if 90 < percentage < 100:
        print("Your Grade is A")
      elif 80 < percentage < 90:
        print("Your Grade is B")
      elif 70 < percentage < 80:
        print("Your Grade is C")
      elif 60 < percentage < 70:
        print("Your Grade is D")
      elif 50 < percentage < 60:
        print("Your Grade is E")
      elif percentage < 50:
        print("Your Grade is F")
      print(name)
      print(total_marks)
      print(average)
      print(f"{percentage}")

name = input("Enter student name: ")
mark1 = int(input("Enter marks of one subject: "))
mark2 = int(input("Enter marks of second subject: "))
mark3 = int(input("Enter marks of third subject: "))
student_marks(name, mark1, mark2, mark3)"""

"""def billing(n):
    menu = {"Burger":40,"Sandwhich":30,"Patties":20,"Dosa":30,"Cold Cofee":60,"Pastrie":45}
    for i in n:
      x = menu[name]
    print(x)
    name = input("Enter item name: ")
    n = int(input("Enter quantities: "))"""

"""def display_bill(items):
    total_cost = 0
    print("\n---Bill Summary ---")
    for item in items:
        name, quantity,price = item
        cost = quantity * price
        total_cost += cost
        print(f"{name} X {quantity} @ ₹{price:.2f} = ₹{cost:.2f}")
    print(f"\nTotal Cost: ₹{total_cost:.2f}")
order_list = []
num_items = int(input("Enter the number of items you want to order: "))
for i in range(num_items):
    print(f"\nItem {i + 1}:")
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity in Kg: "))
    price = float(input("Enter price per Kg: "))
    order_list.append((name, quantity, price))
display_bill(order_list)"""

"""Distance_travelled = int(input("Enter distance in KM: "))
Base_fair = 50
Per_km_rate = 30
total = Distance_travelled * Per_km_rate + Base_fair
print("Total taxi price:",total)"""