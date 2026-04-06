import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
# optional streamlit import
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "cars.csv")

df = pd.read_csv(csv_path)

# Clean data
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend_cars(budget, min_mileage):

    cars = df[(df["price"] <= budget) & (df["mileage"] >= min_mileage)].copy()

    if cars.empty:
        return None

    # Smart score (higher mileage + lower price)
    cars["score"] = (cars["mileage"] * 1000) / cars["price"]

    cars = cars.sort_values(by="score", ascending=False)

    return cars.head(5)


# -----------------------------
# CLI VERSION
# -----------------------------
def run_cli():

    print("\n🚗 USED CAR RECOMMENDATION SYSTEM\n")

    budget = int(input("Enter your budget: "))
    mileage = int(input("Minimum mileage required: "))

    result = recommend_cars(budget, mileage)

    if result is None:
        print("❌ No cars match your criteria")
        return

    print("\n✅ Top Recommended Cars:\n")
    print(result[["car_name", "brand", "price", "mileage"]])

    # Visualization
    plt.bar(result["car_name"], result["mileage"])
    plt.xlabel("Car")
    plt.ylabel("Mileage")
    plt.title("Mileage Comparison")
    plt.show()


# -----------------------------
# STREAMLIT VERSION
# -----------------------------
def run_streamlit():

    st.title("🚗 Smart Used Car Recommendation")

    st.write("Find the best used cars based on your budget and mileage")

    budget = st.slider("Select Budget", 300000, 1500000, 800000)
    mileage = st.slider("Minimum Mileage", 10, 30, 18)

    result = recommend_cars(budget, mileage)

    if result is None:
        st.error("No cars found")
    else:
        st.subheader("Top Recommended Cars")
        st.dataframe(result[["car_name", "brand", "price", "mileage"]])

        st.bar_chart(result.set_index("car_name")["mileage"])


# -----------------------------
# MAIN MENU
# -----------------------------
print("\nChoose Program Mode")
print("1 - CLI (Terminal)")
print("2 - Web App (Streamlit)")

choice = input("Enter choice: ")

if choice == "1":
    run_cli()

elif choice == "2":
    if st is None:
        print("Install Streamlit first → pip install streamlit")
    else:
        run_streamlit()

else:
    print("Invalid choice")
