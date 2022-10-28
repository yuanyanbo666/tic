# import packages
import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st

# show the title
st.title('Titanic App by Yanbo Yuan')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.write(df)

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
fig, ax = plt.subplots(1, 3, figsize = (15,5))
df[df['Pclass'] == 1]['Fare'].plot.box(ax = ax[0])
df[df['Pclass'] == 2]['Fare'].plot.box(ax = ax[1])
df[df['Pclass'] == 3]['Fare'].plot.box(ax = ax[2])
ax[0].set_xlabel('PClass = 1')
ax[0].set_ylabel('Fare')
ax[1].set_xlabel('PClass = 2')
ax[1].set_ylabel('Fare')
ax[2].set_xlabel('PClass = 3')
ax[2].set_ylabel('Fare')
st.pyplot(fig)