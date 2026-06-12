import streamlit as st

# Page title
st.title("🧮 Simple Calculator")

st.write("Select operation and enter numbers")

# Operation selection
operation = st.selectbox(
    "Choose operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Calculation logic
if st.button("Calculate"):

    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {result}")

    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {result}")

    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {result}")

    elif operation == "Division":
        if num2 == 0:
            st.error("Error: Cannot divide by zero")
        else:
            result = num1 / num2
            st.success(f"Result: {result}")