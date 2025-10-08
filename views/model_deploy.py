import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --- App Title & Description ---
st.title('Travel Insurance Claim Prediction')
st.write('This app predicts the likelihood of a customer making a claim based on their travel insurance details.')

# --- Sidebar for Input ---
st.sidebar.header("Please input customer's features")

def create_user_input():
    # Numerical Features (based on model limitations)
    duration = st.sidebar.slider('Duration (days)', min_value=0.0, max_value=547.0, value=7.0)
    net_sales = st.sidebar.slider('Net Sales (USD)', min_value=0.19, max_value=682.0, value=200.0)
    commission = st.sidebar.slider('Commission (USD)', min_value=0.0, max_value=210.21, value=10.0)
    age = st.sidebar.slider('Age (years)', min_value=0, max_value=88, value=35)

    # Categorical Features (dropdown selections)
    agency = st.sidebar.selectbox(
        'Agency',
        ['C2B', 'EPX', 'JZI', 'CWT', 'LWC', 'ART', 'CSR', 'RAB', 'KML', 'SSI', 
         'TST', 'TTW', 'ADM', 'CCR', 'CBH']
    )

    agency_type = st.sidebar.selectbox('Agency Type', ['Airlines', 'Travel Agency'])
    distribution_channel = st.sidebar.selectbox('Distribution Channel', ['Online', 'Offline'])

    product_name = st.sidebar.selectbox(
        'Product Name',
        ['Annual Silver Plan', 'Cancellation Plan', 'Basic Plan', '2 way Comprehensive Plan',
         'Bronze Plan', '1 way Comprehensive Plan', 'Rental Vehicle Excess Insurance',
         'Single Trip Travel Protect Gold', 'Silver Plan', 'Value Plan', '24 Protect',
         'Annual Travel Protect Gold', 'Comprehensive Plan', 'Ticket Protector',
         'Travel Cruise Protector', 'Single Trip Travel Protect Silver',
         'Individual Comprehensive Plan', 'Gold Plan', 'Annual Gold Plan',
         'Annual Travel Protect Platinum', 'Premier Plan', 'Annual Travel Protect Silver',
         'Single Trip Travel Protect Platinum', 'Spouse or Parents Comprehensive Plan']
    )

    destination = st.sidebar.selectbox(
        'Destination Country',
        ['SINGAPORE', 'MALAYSIA', 'INDIA', 'UNITED STATES', 'KOREA, REPUBLIC OF', 'THAILAND', 'GERMANY', 'JAPAN', 
         'INDONESIA', 'VIET NAM', 'AUSTRALIA', 'FINLAND', 'UNITED KINGDOM', 'SRI LANKA', 'SPAIN', 'HONG KONG', 'MACAO', 
         'CHINA', 'IRAN, ISLAMIC REPUBLIC OF', 'TAIWAN, PROVINCE OF CHINA', 'POLAND', 'CANADA', 'OMAN', 'PHILIPPINES', 
         'GREECE', 'TURKEY', 'BRUNEI DARUSSALAM', 'DENMARK', 'SWITZERLAND', 'BELGIUM', 'SWEDEN', 'MYANMAR', 'KENYA', 
         'CZECH REPUBLIC', 'FRANCE', 'RUSSIAN FEDERATION', 'PAKISTAN', 'ARGENTINA', 'TANZANIA, UNITED REPUBLIC OF', 
         'SERBIA', 'ITALY', 'CROATIA', 'NEW ZEALAND', 'UNITED ARAB EMIRATES', 'NETHERLANDS', 'PERU', 'MONGOLIA', 
         'CAMBODIA', 'QATAR', 'NORWAY', 'LUXEMBOURG', 'MALTA', 'LAO PEOPLE\'S DEMOCRATIC REPUBLIC', 'ISRAEL', 
         'SAUDI ARABIA', 'AUSTRIA', 'PORTUGAL', 'UKRAINE', 'ESTONIA', 'ICELAND', 'BRAZIL', 'MEXICO', 'CAYMAN ISLANDS', 
         'PANAMA', 'BANGLADESH', 'TURKMENISTAN', 'BAHRAIN', 'KAZAKHSTAN', 'TUNISIA', 'IRELAND', 'ETHIOPIA', 
         'NORTHERN MARIANA ISLANDS', 'MALDIVES', 'VENEZUELA', 'NEPAL', 'SOUTH AFRICA', 'COSTA RICA', 'JORDAN', 
         'MALI', 'CYPRUS', 'MAURITIUS', 'LEBANON', 'KUWAIT', 'AZERBAIJAN', 'HUNGARY', 'BHUTAN', 'MOROCCO', 
         'ECUADOR', 'UZBEKISTAN', 'CHILE', 'FIJI', 'PAPUA NEW GUINEA', 'FRENCH POLYNESIA', 'NIGERIA', 
         'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF', 'NAMIBIA', 'GEORGIA', 'COLOMBIA', 'SLOVENIA', 'EGYPT', 
         'ZIMBABWE', 'BULGARIA', 'BERMUDA', 'URUGUAY', 'GUINEA', 'GHANA', 'BOLIVIA', 'TRINIDAD AND TOBAGO', 
         'VANUATU', 'GUAM', 'UGANDA', 'JAMAICA', 'ROMANIA', 'REPUBLIC OF MONTENEGRO', 'KYRGYZSTAN', 'GUADELOUPE', 
         'RWANDA', 'BOTSWANA', 'ZAMBIA', 'GUYANA', 'LITHUANIA', 'GUINEA-BISSAU', 'SENEGAL', 'CAMEROON', 'SAMOA', 
         'PUERTO RICO', 'TAJIKISTAN', 'BELARUS', 'ARMENIA', 'FAROE ISLANDS', 'DOMINICAN REPUBLIC', 'MOLDOVA, '
         'REPUBLIC OF', 'BENIN', 'REUNION'
] 
    )

    # Create input DataFrame
    user_data = {
        'Agency': agency,
        'Agency Type': agency_type,
        'Distribution Channel': distribution_channel,
        'Product Name': product_name,
        'Duration': duration,
        'Destination': destination,
        'Net Sales': net_sales,
        'Commision (in value)': commission,
        'Age': age
    }

    return pd.DataFrame([user_data])

# --- Collect User Input ---
data_customer = create_user_input()

# --- Display Input Data ---
st.subheader('Customer Features')
st.write(data_customer.transpose().style.hide(axis='index'))

# --- Load Model ---
with open('travel-insurance-prediction-model.sav', 'rb') as f:
    model_loaded = pickle.load(f)

# --- Prediction ---
target = model_loaded.predict(data_customer)[0]
probability = model_loaded.predict_proba(data_customer)[0]

# --- Display Results ---
st.subheader('Prediction Result')
if target == 1:
    st.success('✅ This customer is likely to make a claim.')
else:
    st.info('🟦 This customer is unlikely to make a claim.')

st.write(f'**Probability of Claim:** {probability[1]:.2%}')

# --- Disclaimer ---
st.caption('⚠️ Note: This prediction is valid within the defined data ranges and categories based on the model limitations.')
