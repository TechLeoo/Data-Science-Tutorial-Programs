# WELL DONE AND WELCOME TO STREAMLIT
# 1) How to access EMOJI's on your NOT MAC ---> CTRL + ;
# 2) First command for EVERY streamlit app ---> st.set_page_config()
# 3) Find the file location in the command prompt then run ---> streamlit run name_of_file.py
# 4) Please do not forget to put .py at the end

import streamlit as st

st.set_page_config(
         page_title="Happy New Month",
         page_icon="😭",
         layout="wide",
         initial_sidebar_state="expanded",
    )

# # (1) Collect Data with ...
# # ---> First Group
# slider_value = st.slider(label = "Test Slider", min_value = 3, max_value = 50, value = 10, help = "Specify a value")
# multiselect_value = st.multiselect(label = "Test MultiSelect", options = ["Male", "Female", "Baby", "Father", "Girl", "Mother", "Boy"], help = "Identify yourself", max_selections = 2)
# radio_value = st.radio(label = "Test Radio", options = ["Male", "Female", "Baby", "Father", "Girl", "Mother", "Boy"], help = "Identify yourself", index = 0, horizontal = True)
# checkbox_value = st.checkbox(label = "Agree to terms & conditions", help = "Agree or leave", value = True)
# selectbox_value = st.selectbox(label = "Test Radio", options = ["Male", "Female", "Baby", "Father", "Girl", "Mother", "Boy"], help = "Identify yourself", index = 4)

# # ---> Second Group
# text_box = st.text_input("Some text", max_chars = 50, )
# password_box = st.text_input("Some text", max_chars = 50, type = "password",)
# text_area = st.text_area("I need a text area", height = 200, max_chars = 1000)
# number_box = st.number_input("Some number", min_value = 1, max_value = 10, step = 1)
# collect_time = st.time_input("Some time", step = 60)


# (2) Designing your layout
# st.columns
# st.sidebar
# st.tabs
# st.container
# st.expander
# st.empty

# ---> st.sidebar
# METHOD 1
# create_sidebar = st.sidebar
# create_sidebar.text_input("Username", max_chars = 50,)
# create_sidebar.text_input("Password", max_chars = 50, type = "password",)

# METHOD 2
# with st.sidebar:
#     st.text_input("Username", max_chars = 50,)
#     st.text_input("Password", max_chars = 50, type = "password",)

# ---> st.container
# with st.container():
#     col1, col2 = st.columns(2)
    
    # with col1:
        # slider_value = st.slider(label = "Test Slider", min_value = 3, max_value = 50, value = 10, help = "Specify a value")
        # multiselect_value = st.multiselect(label = "Test MultiSelect", options = ["Male", "Female", "Baby", "Father", "Girl", "Mother", "Boy"], help = "Identify yourself", max_selections = 2)
    
    
    # with col2:
        # radio_value = st.radio(label = "Test Radio", options = ["Male", "Female", "Baby", "Father", "Girl", "Mother", "Boy"], help = "Identify yourself", index = 0, horizontal = True)
        # checkbox_value = st.checkbox(label = "Agree to terms & conditions", help = "Agree or leave", value = True)
        # selectbox_value = st.selectbox(label = "Test Radio", options = ["Male", "Female", "Baby", "Father", "Girl", "Mother", "Boy"], help = "Identify yourself", index = 4)

# with st.container():
#     col1, col2, col3, col4, col5 = st.columns([1, 1, 3, 1, 1])
#     with col3:
#         text_box = st.text_input("Email", max_chars = 50)
#         password_box = st.text_input("User Password", max_chars = 50, type = "password",)
#         text_area = st.text_area("Leave a comment", height = 200, max_chars = 1000)  
    
# with st.container():
#     number_box = st.number_input("Some number", min_value = 1, max_value = 10, step = 1)
#     collect_time = st.time_input("Some time", step = 60)

# # ---> st.tabs
# tab1, tab2, tab3 = st.tabs(["Widgets", "Input", "Date"])
# with tab1:
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         slider_value = st.slider(label = "Test Slider", min_value = 3, max_value = 50, value = 10, help = "Specify a value")
#         radio_value = st.radio(label = "Test Radio", options = ["Male", "Female", "Baby", "Father", "Girl", "Mother", "Boy"], help = "Identify yourself", index = 0)
        
#     with col2:
#         multiselect_value = st.multiselect(label = "Test MultiSelect", options = ["Male", "Female", "Baby", "Father", "Girl", "Mother", "Boy"], help = "Identify yourself", max_selections = 2)
#         selectbox_value = st.selectbox(label = "Test Selectbox", options = ["Male", "Female", "Baby", "Father", "Girl", "Mother", "Boy"], help = "Identify yourself", index = 4)
    
#     with col3:
#         checkbox_value = st.checkbox(label = "Agree to terms & conditions", help = "Agree or leave", value = True)

# with tab2:
#     col1, col2 = st.columns([1, 2.5])
#     with col1:
#         text_box = st.text_input("Email", max_chars = 50)
#         password_box = st.text_input("User Password", max_chars = 50, type = "password",)
#         text_area = st.text_area("Leave a comment", height = 200, max_chars = 1000)  
        
# with tab3:
#     number_box = st.number_input("Some number", min_value = 1, max_value = 10, step = 1)
#     collect_time = st.time_input("Some time", step = 60)

# ---> st.expander
# with st.expander("More Info"):
#     slider_value = st.slider(label = "Test Slider", min_value = 3, max_value = 50, value = 10, help = "Specify a value")
#     radio_value = st.radio(label = "Test Radio", options = ["Male", "Female", "Baby", "Father", "Girl", "Mother", "Boy"], help = "Identify yourself", index = 0)
#     multiselect_value = st.multiselect(label = "Test MultiSelect", options = ["Male", "Female", "Baby", "Father", "Girl", "Mother", "Boy"], help = "Identify yourself", max_selections = 2)
#     selectbox_value = st.selectbox(label = "Test Selectbox", options = ["Male", "Female", "Baby", "Father", "Girl", "Mother", "Boy"], help = "Identify yourself", index = 4)
#     checkbox_value = st.checkbox(label = "Agree to terms & conditions", help = "Agree or leave", value = True)

    # st.write(slider_value); st.write(radio_value); st.write(multiselect_value); st.write(selectbox_value); st.write(checkbox_value)
















# -----> LETS WRITE SOME INFORMATION
# st.title("This is the title")
# st.header("This is a header")
# st.subheader("This is a subheader")
# # Write normal text
# st.text("This is some text")
# st.write("This is using st.write")
# st.markdown("""
#             This is me showing markdown
#             """)


st.error("This is an error")
st.warning("You have been warned")
st.success("This is successful")
st.exception(ValueError("This is an exception"))
st.info("I have some info for you")





