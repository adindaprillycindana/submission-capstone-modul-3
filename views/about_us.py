import streamlit as st

# --- TERRA ---
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image("./assets/terra_v.png", width=230)
    st.write('''


Vision:
             
To become the most trusted general insurance company in Asia by providing protection that is strong, transparent, and human-centered.

Missions:
1. Deliver reliable and transparent insurance products that meet modern lifestyle needs.
2. Strengthen risk management and claim assessment through data-driven innovation.
3. Build long-term relationships with customers based on trust and empathy.
4. Encourage a culture of continuous learning and technological advancement within the company.
5. Contribute to a safer and more resilient society through financial protection.
             
        
''')

with col2:
    st.title("Terra General Insurance", anchor=False)
    st.write('''
“Solid Protection, Grounded in Trust.”
    
Founded in 2012, Terra General Insurance is a leading provider of comprehensive general insurance solutions in Southeast Asia.
Terra believes that true protection begins with stability, not only financial stability, but also emotional reassurance for every customer.
With products spanning motor, property, health, business, and travel insurance, Terra aims to make insurance simpler, smarter, and more accessible for everyone.
In the past few years, Terra has invested heavily in data science and automation to improve its claim assessment process and customer experience.


Core Products:
1. TerraCare: Health insurance
2. TerraMove: Motor vehicle insurance
3. TerraHome: Property and disaster protection
4. TerraTravel: Travel insurance
     
             ''')