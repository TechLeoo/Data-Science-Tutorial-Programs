import streamlit as st
import joblib
from PIL import Image

st.set_page_config(
     page_title="Salary Predictor",
     page_icon="💰",
     layout="centered",
     initial_sidebar_state="expanded",
    )

# Opening the Image
def open_image(image):
    image = Image.open(image)
    st.image(image)

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

with st.sidebar:
    model = joblib.load("model.pkl")
    st.markdown("# Predictor")
    question = st.radio("How to select parameters", options = ["Slider", "Number Input", "Not Sure"])
    if question == "Slider":
        st.divider()
        years_experience = st.slider("Years of Experience", min_value = 0.0, max_value = 70.0, value = 35.0, step = 0.1)
        
    elif question == "Number Input":
        st.divider()
        years_experience = st.number_input("Years of Experience", min_value = 0.0, max_value = 70.0, value = 35.0, step = 0.1)
        
    elif question == "Not Sure":
        st.divider()
        open_image("happy_people/comic-style-2118785_640.jpg")
        st.text("It's alright! Take your time before making a decision between the slider or number input.")
    
    # Button to make predictions
    predict = st.button("Make Prediction")
    if predict and (question == "Slider" or question == "Number Input"):
        y_pred = model.predict([[years_experience]])[0]
        st.success("Prediction Successful.")
        st.success(f"Your estimated salary is {y_pred}.")
        
    elif predict and (question == "Not Sure"):
        st.error("You can not make predictions when you are 'NOT SURE'.")
    
    
    
    
# MAIN PAGE
st.title("Salary Predictor")
st.divider()
st.write(
        """
This project is part of a sample done to teach application of streamlit
towards creating web applications for data scientists. In this project,
we create a model that predicts salary based of a person's experience. 

We hope you enjoy using this application, please do leave us a feedback so we continue to improve.
        """
        )
with st.expander("Code"):
    st.code("""
            import numpy as np
            import pandas as pd
            import matplotlib.pyplot as plt
            from sklearn.ensemble import RandomForestRegressor
            from sklearn.metrics import r2_score, mean_squared_error

            dataset = pd.read_csv("Salary_Data.csv")

            # EDA
            # Exploratory Data Analysis
            data_unique = {}
            data_category_count = {}
            dataset.info()
            data_head = dataset.head()
            data_tail = dataset.tail()
            data_mode = dataset.mode().iloc[0]
            data_descriptive_stats = dataset.describe()
            data_more_descriptive_stats = dataset.describe(include = "all")
            data_correlation_matrix = dataset.corr(numeric_only = True)
            data_distinct_count = dataset.nunique()
            data_count_duplicates = dataset.duplicated() 
            # Check if there are missing values.
            data_count_null = dataset.isnull().sum()
            data_total_null = dataset.isnull().sum().sum()
            for each_column in dataset.columns:
                data_unique[each_column] = dataset[each_column].unique()
            for each_column in dataset.select_dtypes(object).columns:
                data_category_count[each_column] = dataset[each_column].value_counts()

            # Data Segregation
            x = dataset.iloc[:, [0]]
            y = dataset.Salary

            # Model Training
            regressor = RandomForestRegressor(random_state = 0)
            model = regressor.fit(x, y)

            # Model Prediction
            y_pred = model.predict(x)

            # Model Evaluation
            r2 = r2_score(y, y_pred)
            rmse = np.sqrt(mean_squared_error(y, y_pred))
            """)
            
st.divider()
st.subheader("Leave a Feedback")
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
       email = st.text_input("Email", placeholder = "User email")
       comment = st.text_area("Comment", max_chars = 1000, placeholder = "Write here", height = 200)
       submit = st.button("Submit Feedback")



# st.markdown("<br></br>", unsafe_allow_html = True) # Useful to create spaces when you need to