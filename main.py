# Import Modules
import streamlit as st

# Page Header

st.set_page_config(page_title='Odd Or Even?')


# Page Title

st.title('Odd or Even? ')

# Description 

st.info('You Can Enter Any Number and know, Whether It is Odd OR Even.')


# Taking Input
# We will add min_value at the last because if we don't add it the program will take input in decimal value
a = st.number_input('Enter Any Number and know, Whether It is Odd Or Even.',min_value=0)
if a % 2 == 0:
    st.success(f'{a} is Even Number')
else:
    st.success(f'{a} is an Odd Number')