import streamlit as st
import requests


def main():
    page = st.session_state.page

    if page == "Home":
        home_page()
    elif page == "Calculate":
        calculate_page()

def home_page():

    st.title("Wie nachhaltig sind Ihre Reisen?")
    st.subheader("Where are you going on this trip?")

    places = ["St.Gallen", "Zurich", "Basel","Bern"]
    from_place = st.selectbox("From?",places)
    to_place = st.selectbox("To?", places)
    if st.button("Calculate"):
        st.session_state.from_place = from_place
        st.session_state.to_place = to_place
        st.session_state.page = "Calculate"

    
def calculate_page():

    from_place = st.session_state.from_place
    to_place = st.session_state.to_place
    st.title("Results")
    st.write("To go from",from_place,"to",to_place,"you should take...")
    
#Add visual here

    st.write("!!!!The ranking and visuals need to go here.")

#BUTTON
    button_html = """
        <style>
        .button {
            background-color: #004080; /* Dark blue color */
            color: white; /* Text color */
            padding: 10px 20px; /* Padding */
            text-align: center; /* Center-align text */
            text-decoration: none; /* Remove underline */
            display: inline-block; /* Make it inline */
            border: none; /* Remove border */
            border-radius: 4px; /* Add border radius */
            cursor: pointer; /* Add cursor pointer */
        }
        </style>
        <a href="https://example.com" class="button" style="color: white;">Want to offset your travel’s carbon footprint?</a>
        """

    # Display the custom HTML
    st.markdown(button_html, unsafe_allow_html=True)


    if st.button("Return to homepage"):
        st.session_state.page = "Home"

if __name__ == "__main__":
    if "page" not in st.session_state:
        st.session_state.page = "Home"
    main()   