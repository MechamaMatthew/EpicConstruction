import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="House Budget",
    page_icon=":house:",
    layout="wide",  # This will make content expand to the full width
    initial_sidebar_state="expanded",
)

# Load the Excel file
file_path = "C:/Users/arvel/OneDrive/Desktop/Epic Con/Expenses.xlsx"
df = pd.read_excel(file_path)

# Get unique project names
all_projects = df['Project Name'].unique()

# Select project to display
selected_project = st.selectbox("Select a project to display", all_projects)

# Filter data based on selected project
selected_project_data = df[df['Project Name'] == selected_project]

# Filter data where 'Contracted' is False and True
not_contracted_data = selected_project_data[selected_project_data['Contracted'] == False]
contracted_data = selected_project_data[selected_project_data['Contracted'] == True]

# Add title
st.title("House Budget")

# Create graphs using Matplotlib
st.write(f"## Expenses for {selected_project}")

# Graph 1: In House Expenses where Contracted = False
expenses_by_type_not_contracted = not_contracted_data.groupby('Expense Type')['Amount'].sum()
fig1, ax1 = plt.subplots()
bars1 = ax1.bar(expenses_by_type_not_contracted.index, expenses_by_type_not_contracted, color='slategray')  # Change color to slategray
ax1.set_xlabel("Expense Type")
ax1.set_ylabel("Amount")
ax1.set_title("In House Expenses")

# Set background color behind bars
ax1.set_facecolor('#333F4F')  # Set background color to match Streamlit background
fig1.set_facecolor('#333F4F')

# Add data labels inside the bars
for bar in bars1:
    height = bar.get_height()
    ax1.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3),
                 textcoords="offset points", ha='center', va='bottom', color='white')

# Change text color
ax1.xaxis.label.set_color('white')
ax1.yaxis.label.set_color('white')
ax1.title.set_color('white')
ax1.tick_params(axis='x', colors='white')
ax1.tick_params(axis='y', colors='white')
ax1.tick_params(axis='x', labelrotation=45)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)

# Graph 2: In House Expenses where Contracted = True
expenses_by_type_contracted = contracted_data.groupby('Expense Type')['Amount'].sum()
fig2, ax2 = plt.subplots()
bars2 = ax2.bar(expenses_by_type_contracted.index, expenses_by_type_contracted, color='slategray')  # Change color to slategray
ax2.set_xlabel("Expense Type")
ax2.set_ylabel("Amount")
ax2.set_title("Subcontracted Expenses")

# Rotate Axes
plt.xticks(rotation=45, ha='right')

# Set background color behind bars
ax2.set_facecolor('#333F4F')  # Set background color to match Streamlit background
fig2.set_facecolor('#333F4F')

# Add data labels inside the bars
for bar in bars2:
    height = bar.get_height()
    ax2.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3),
                 textcoords="offset points", ha='center', va='bottom', color='white')

# Change text color
ax2.xaxis.label.set_color('white')
ax2.yaxis.label.set_color('white')
ax2.title.set_color('white')
ax2.tick_params(axis='x', colors='white')
ax2.tick_params(axis='y', colors='white')

ax2.tick_params(axis='x', labelrotation=45)

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)

# Display graphs side by side
col1, col2 = st.columns(2)
with col1:
    st.pyplot(fig1)

with col2:
    st.pyplot(fig2)
