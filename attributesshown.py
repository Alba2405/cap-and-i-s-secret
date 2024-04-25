import streamlit as st
import requests
import pandas as pd
from geopy.distance import geodesic

# Read the CSV file containing airport codes
@st.cache_data
def load_airport_codes():
    airport_df = pd.read_csv("C:/Users/Surface/Downloads/CSCarbon/airport-codes.csv")
    return airport_df

def estimate_flight_emissions(departure_airport, destination_airport, passengers=1):
    # Carbon Interface API endpoint
    endpoint = "https://www.carboninterface.com/api/v1/estimates"

    api_key = "PADZcJLe9LL9xi6CxF1wAQ"

    # Request headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Flight legs data
    legs = [
        {"departure_airport": departure_airport.upper(), "destination_airport": destination_airport.upper()}
    ]

    # Request payload
    payload = {
        "type": "flight",
        "passengers": passengers,
        "legs": legs
    }

    try:
        # Make API request
        response = requests.post(endpoint, headers=headers, json=payload)
        
        # Print response content for debugging
        st.text_area("API Response", response.content.decode("utf-8"))

        data = response.json()

        # Check if request was successful
        if response.status_code == 200:
            # Extract carbon emissions from response
            carbon_emissions = data['data']['attributes']['carbon_kg']
            return carbon_emissions
        else:
            # Print error message if request failed
            st.error(f"Error: {data}")
            return None
    except Exception as e:
        # Print error message if request failed
        st.error(f"Error: {e}")
        return None

def main():
    st.title("Estimate CO2 Emissions for Your Flight")

    # Load the airport codes from the CSV file
    airport_df = load_airport_codes()

    # Extract the airport codes as a list
    airport_codes = airport_df["iata_code"].tolist()

    # User input for departure and destination airport codes
    departure_airport = st.selectbox("Select departure airport code:", airport_codes)
    destination_airport = st.selectbox("Select destination airport code:", airport_codes)

    # Number of passengers
    passengers = st.number_input("Enter number of passengers:", min_value=1, value=1)

    # Button to trigger CO2 emissions estimation
    if st.button("Estimate CO2 Emissions"):
        if departure_airport and destination_airport:
            # Estimate CO2 emissions
            emissions = estimate_flight_emissions(departure_airport, destination_airport, passengers)
            if emissions is not None:
                st.success(f"Estimated CO2 emissions: {emissions} kilograms")
            else:
                st.error("Failed to estimate CO2 emissions. Please check your inputs and try again.")
        else:
            st.warning("Please select both departure and destination airport codes.")

if __name__ == "__main__":
    main()
