import streamlit as st
import requests
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("🔥 Fuzzy Logic Fan Controller Web App")

# User Input for Temperature
temp_value = st.slider("Select Temperature (°C)", 0, 100, 50)

# Call Flask API
if st.button("Compute Fan Speed"):
    response = requests.post("http://127.0.0.1:5000/compute", json={'temperature': temp_value})
    if response.status_code == 200:
        result = response.json()
        st.success(f"At {result['temperature']}°C, the fan speed is: {result['fan_speed']:.2f}")
    else:
        st.error("Error in computing fan speed")

# Membership Function Plot
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Temperature Membership Functions
x = np.arange(0, 101, 1)
ax[0].plot(x, fuzz.gbellmf(x, 15, 3, 10), 'b', linewidth=2, label="Cold")
ax[0].plot(x, fuzz.gbellmf(x, 20, 3, 50), 'g', linewidth=2, label="Warm")
ax[0].plot(x, fuzz.gbellmf(x, 15, 3, 90), 'r', linewidth=2, label="Hot")
ax[0].set_title("Temperature Membership Functions")
ax[0].set_xlabel("Temperature (°C)")
ax[0].set_ylabel("Membership Degree")
ax[0].legend()

# Fan Speed Membership Functions
x_fan = np.arange(0, 101, 1)
ax[1].plot(x_fan, fuzz.gbellmf(x_fan, 15, 3, 10), 'b', linewidth=2, label="Slow")
ax[1].plot(x_fan, fuzz.gbellmf(x_fan, 20, 3, 50), 'g', linewidth=2, label="Medium")
ax[1].plot(x_fan, fuzz.gbellmf(x_fan, 15, 3, 90), 'r', linewidth=2, label="Fast")
ax[1].set_title("Fan Speed Membership Functions")
ax[1].set_xlabel("Fan Speed")
ax[1].set_ylabel("Membership Degree")
ax[1].legend()

# Display Plots
st.pyplot(fig)
