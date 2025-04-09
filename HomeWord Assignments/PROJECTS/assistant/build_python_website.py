import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Analysis App")
st.write("This is a simple data analysis app built with Streamlit")

# File upload
upload_file = st.file_uploader("Upload a CSV file", type=["csv"])

if upload_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(upload_file)
    st.write("File uploaded successfully...")

    # Data Preview
    st.subheader("Data Preview")
    st.write(df.head())

    # Data Summary
    st.subheader("Data Summary")
    st.write(df.describe())

    # Data Filtering
    st.subheader("Data Filtering")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select a column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select a value to filter by", unique_values)

    # Filter data
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    # Plot Data
    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
    else:
        st.write("Click the button to generate the plot")
else:
    st.write("Waiting on file upload...")






# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# st.title("Simple Data Analysis App ")
# st.write ("This is a  simple data analysis app build with streamlit")
# upload_file  = st.file_uploader("Upload a CSV file", type=["cvs"])
# if upload_file is not None:
#  st.write ("File uploaded successfully...")
# st.subheader("Data Preview")
# st.write(df.head())
# st. subheader("Data SUmmary")
# st.write(df.describe())
# st.subheader("Data Filtering")
# columns = df.columns.tolist()
# selected_column = st.selectbox("Select a column to filter by", columns)
# unique_values = df[selected_column].unique()
# selected_Value = st.selectbox("Select a value to filter by", unique_values)

# filtered_df =df[df[selected_column] == selected_Value]
# st.write[filtered_df]
# st.subheader("plot Data")
# x_column = st.selectbox("Select x-axis column",columns)
# y_column = st.selectbox("Select x-axis column",columns)

# if st.button("Generate Plot"):
#  st.line_chart(filtered_df.set_index(x_column)[y_column])
# else:
#  st.write("Click the button to generate the plot")
#  st.write("Waiting on file upload...")