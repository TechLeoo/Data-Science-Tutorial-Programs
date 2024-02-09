import streamlit as st
import streamlit_option_menu as som
import streamlit_antd_components as sac
import joblib
from PIL import Image

st.set_page_config(
     page_title="Purchase Predictor",
     page_icon="💳",
     layout="centered",
     initial_sidebar_state="expanded",
    )

# Opening the Image
def open_image(image):
    image = Image.open(image)
    st.image(image)

# st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

with st.sidebar:
    # https://icons.getbootstrap.com/  ----> Use this to get your icon names
    # https://nicedouble-streamlitantdcomponentsdemo-app-middmy.streamlit.app/ ----> Very useful
    
    tabs = sac.menu([
        sac.MenuItem('Predictor', icon='bag'),
        sac.MenuItem('Project', icon='boxes'),
        sac.MenuItem('EDA', icon='bar-chart'),
        sac.MenuItem('Data Analysis', icon='graph-down'),
        sac.MenuItem('About', icon='file-person'),
        sac.MenuItem('Contact', icon='telephone'),
    ], open_all=True)
    
if tabs == "Predictor":
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.title("Predict Purchase")
        sac.divider(label='home', icon=sac.BsIcon(name='house', size=20), variant='dashed', color='gray')
        
        model = joblib.load("model1.pkl")
        question = st.radio("How to select parameters", options = ["Slider", "Number Input"])
        
        if question == "Slider":
            sac.divider(label='model', icon=sac.BsIcon(name='graph-up-arrow', size=20), variant='dashed', color='gray')
            gender = sac.segmented(
                    items=[
                        sac.SegmentedItem(label='Male', icon = "gender-male"),
                        sac.SegmentedItem(label='Female', icon="gender-female"),
                    ], label='Gender', align='left', size='sm', color='red'
                )
            age = st.slider("Age", min_value = 10, max_value = 90, value = 45, step = 1)
            estimated_salary = st.slider("Estimated Salary", min_value = 1000, max_value = 500000, value = 120000, step = 1000)
            
        elif question == "Number Input":
            sac.divider(label='Model', icon=sac.BsIcon(name='house', size=20), variant='dashed', color='gray')
            gender = sac.segmented(
                    items=[
                        sac.SegmentedItem(label='Male', icon = "gender-male"),
                        sac.SegmentedItem(label='Female', icon="gender-female"),
                    ], label='Gender', align='left', size='sm', color='red'
                )
            age = st.number_input("Age", min_value = 10, max_value = 90, value = 45, step = 1)
            estimated_salary = st.number_input("Estimated Salary", min_value = 1000, max_value = 500000, value = 120000, step = 1000)
            
        if gender == "Male":
            gender = 1
        else:
            gender = 0
            
        # Button to make predictions
        predict = st.button("Make Prediction")
        if predict and (question == "Slider" or question == "Number Input"):
            y_pred = model.predict([[age, estimated_salary, gender]])
            st.success("Prediction Successful.")
            if y_pred == 0:
                y_pred = "not purchase"
            else:
                y_pred = "purchase"
            if gender == 1:
                st.success(f"A male client who is {age} years old, and has an estimated salary of about ${estimated_salary} is expected to {y_pred} our product.")
            else:
                st.success(f"A female client who is {age} years old, and has an estimated salary of about ${estimated_salary} is expected to {y_pred} our product.")
            
            
elif tabs == "Project":
    dataset = joblib.load("dataset.pkl")
    with st.expander("Dataset"):
        data = st.data_editor(dataset, use_container_width= True)
    with st.expander("Code"):
        code = st.code(
            """
            # Import Libraries
            import numpy as np
            import pandas as pd
            import matplotlib.pyplot as plt
            from imblearn.over_sampling import SMOTE, RandomOverSampler
            from imblearn.under_sampling import RandomUnderSampler
            from sklearn.model_selection import train_test_split
            from xgboost import XGBClassifier
            from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score, auc

            # Get the dataset
            data = pd.read_csv("Social_Network_Ads.csv")

            # Exploratory Data Analysis
            data.info()
            data_head = data.head()
            data_tail = data.tail()
            data_descriptive_statistic = data.describe()
            data_more_desc_statistic = data.describe(include = "all")
            data_mode = data.mode()
            data_distinct_count = data.nunique()
            data_correlation_matrix = data.corr() 
            data_null_count = data.isnull().sum()
            data_total_null_count = data.isnull().sum().sum()
            # data_hist = data.hist(figsize = (15, 10), bins = 10)

            # Data Cleaning and Transformation
                # 1) Drop USER ID column
            data = data.drop("User ID", axis = 1)
                # 2) Categroical to numerical
            data = pd.get_dummies(data, drop_first = True, dtype = np.int8)

                # 3) Counting the number of values in each class
            y_class = data["Purchased"].value_counts()


            # Further Data Preparation and Segregation
                # 1) Select dependent and independent
            x = data.drop("Purchased", axis = 1)
            y = data.Purchased
                
                # 2) Data Binning
            x["Age"] = pd.cut(x = x["Age"], bins = 9, labels = False)
            x["EstimatedSalary"] = pd.cut(x = x["EstimatedSalary"], bins = 10, labels = False)

                # 3) Split the data
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

                # 4) Check for class imbalance
            ytrain_class = y_train.value_counts()

                # 5) Let's make the classes equal ---> Use SMOTE (Synthetic Minority OverSampling Technique)
            sampler = RandomOverSampler()
            xtrain_resampled, ytrain_resampled = sampler.fit_resample(x_train, y_train)

                # 6) Check to see if the model actually balanced the classes
            ytrain_resampled_class = ytrain_resampled.value_counts()

            # Model Training
            classifier = XGBClassifier(random_state = 0)
            model = classifier.fit(xtrain_resampled, ytrain_resampled)

            # Model Prediction
            y_pred = model.predict(xtrain_resampled)
            y_pred1 = model.predict(x_test)

            # Model Evaluation
            # - TRAINING 
            train_confusion_matrix = confusion_matrix(ytrain_resampled, y_pred)
            train_classification_report = classification_report(ytrain_resampled, y_pred)
            train_accuracy = accuracy_score(ytrain_resampled, y_pred)
            train_precision = precision_score(ytrain_resampled, y_pred)
            train_recall = recall_score(ytrain_resampled, y_pred)
            train_f1_score = f1_score(ytrain_resampled, y_pred)

            # - TEST
            test_confusion_matrix = confusion_matrix(y_test, y_pred1)
            test_classification_report = classification_report(y_test, y_pred1)
            test_accuracy = accuracy_score(y_test, y_pred1)
            test_precision = precision_score(y_test, y_pred1)
            test_recall = recall_score(y_test, y_pred1)
            test_f1_score = f1_score(y_test, y_pred1)
            """
            )

elif tabs == "EDA":
    pass
elif tabs == "Data Analysis":
    pass
elif tabs == "About":
    pass
elif tabs == "Contact":
    pass