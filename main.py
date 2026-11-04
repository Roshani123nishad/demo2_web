import streamlit as st

###with the help of steamlit to write ant word on th webpage
# st.title("welcome to wscube tech")
# st.header("python")
# st.subheader("java")
# st.markdown("I love Python")
# st.code("for i in range(1,5,1): print('Hello, World!')")


## with help of streamlit to add excel sheet in webpage
# import pandas as pd
# dataset = pd.read_csv("sales_data_2.csv")
# st.dataframe(dataset)


####with help of steamlit  to creat form in webpage
data1=st.form(key="form1")
name=data1.text_input("Enter your name")
fname=data1.text_input("Enter your father name")
adr=data1.text_area("Enter your text :")
classdata=data1.selectbox("Select your class",["1st","2nd","3rd","4th"])
button=st.button("Submit")
if button:
    st.markdown(f"""
    Name : {name}
    Father Name : {fname} 
    Address : {adr}  
    Class : {classdata}""")

