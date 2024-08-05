import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_excel('/home/gaurav/FS/Xeon_work/Xeon_Consol.xlsx', header=None, skiprows=1)
column_names = [
    "Model", "Task", "Input Modal", "Optimizations", "ISV Story", "Model link", 
    "Parameter/Size", "Latency (Seconds)", "Percentage Improvement", "Core Affinity"
]
df.columns = column_names
df.dropna(how='all', inplace=True)
st.write(df)
# Set the page title
st.title('Model Data Explorer')

# Sidebar for selecting filters
task_filter = st.sidebar.selectbox(
    "Select Task",
    df['Task'].unique()
)

task_filtered_df = df[
    (df['Task'] == task_filter)
]

# Display the filtered dataframe
st.write(task_filtered_df)


isv_filter = st.sidebar.selectbox(
    "Select ISV",
    df['ISV Story'].unique()
)

isv_filtered_df = df[
    (df['ISV Story'] == isv_filter)
]

# Display the filtered dataframe
st.write(isv_filtered_df)


optimization_filter = st.sidebar.selectbox(
    "Select Optimization",
    df['Optimizations'].unique()
)

# Filter the dataframe based on selected options
optimized_filtered_df = df[
    (df['Optimizations'] == optimization_filter)
]

# Display the filtered dataframe
st.write(optimized_filtered_df)
