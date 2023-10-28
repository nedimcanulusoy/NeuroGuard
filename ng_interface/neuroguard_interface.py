import streamlit as st
import requests

st.title("Prompt Injection Detection")

user_input = st.text_input("Enter a text:")

if st.button("Submit"):
    # Validate input
    if not user_input:
        st.warning("Please enter a text before submitting.")
    else:
        # Making the request
        try:
            with st.spinner("Getting predictions..."):
                response = requests.post("http://api:8000/predict", json={"data": user_input}, timeout=10)
                response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code

            prediction = response.json().get("prediction")

            if prediction == 1:
                st.success("Injection!")
            elif prediction == 0:
                st.success("Legit!")
            else:
                st.warning(f"Unexpected prediction value: {prediction}")

        except requests.RequestException as e:
            st.error(f"Error making request: {str(e)}")
        except ValueError:
            st.error("Error decoding the server's response.")
