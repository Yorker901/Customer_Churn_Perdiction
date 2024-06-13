import streamlit as st

st.set_page_config(layout="centered", page_title="Customer Churn Prediction")

# Load the model
pickle_in = open("rfcintel1.pkl", "rb")
rfcintel1 = pickle.load(pickle_in)

def Churn_data(...):
    ...

def prediction_page():
    st.title("Predict Customer Churn")
    st.write("Please fill in the parameters below to predict customer churn.")
    
    account_length = st.number_input("Account Length", min_value=0, max_value=100, value=0)
    voice_mail_plan = st.selectbox("Voice Mail Plan", ["No", "Yes"])
    voice_mail_messages = st.number_input("Voice Mail Messages", min_value=0, max_value=100, value=0)
    day_mins = st.number_input("Day Minutes", min_value=0.0, max_value=500.0, value=0.0)
    evening_mins = st.number_input("Evening Minutes", min_value=0.0, max_value=500.0, value=0.0)
    night_mins = st.number_input("Night Minutes", min_value=0.0, max_value=500.0, value=0.0)
    international_mins = st.number_input("International Minutes", min_value=0.0, max_value=100.0, value=0.0)
    customer_service_calls = st.number_input("Customer Service Calls", min_value=0, max_value=10, value=0)
    international_plan = st.selectbox("International Plan", ["No", "Yes"])
    day_calls = st.number_input("Day Calls", min_value=0, max_value=200, value=0)
    day_charge = st.number_input("Day Charge", min_value=0.0, max_value=100.0, value=0.0)
    evening_calls = st.number_input("Evening Calls", min_value=0, max_value=200, value=0)
    evening_charge = st.number_input("Evening Charge", min_value=0.0, max_value=100.0, value=0.0)
    night_calls = st.number_input("Night Calls", min_value=0, max_value=200, value=0)
    night_charge = st.number_input("Night Charge", min_value=0.0, max_value=100.0, value=0.0)
    international_calls = st.number_input("International Calls", min_value=0, max_value=50, value=0)
    international_charge = st.number_input("International Charge", min_value=0.0, max_value=50.0, value=0.0)
    total_charge = st.number_input("Total Charge", min_value=0.0, max_value=500.0, value=0.0)
    
    if st.button("Predict Churn"):
        result = Churn_data(...)
        if result[0] == 0:
            st.success("The customer is not likely to churn.")
        else:
            st.warning("The customer is likely to churn.")

def about_page():
    st.title("About")
    st.write("""
    This application uses a machine learning model to predict customer churn.
    Provide the required inputs and click on 'Predict Churn' to see the results.
    """)

PAGES = {
    "Prediction": prediction_page,
    "About": about_page
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page()
