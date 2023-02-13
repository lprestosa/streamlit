"""
Medium article:
   https://towardsdatascience.com/getting-started-with-streamlit-web-based-applications-626095135cb8
Display streamlit page, load csv file and show plot
"""

# Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Add a title and intro text
st.title('Earthquake Data Explorer')
st.text('This is a web app to allow exploration of Earthquake Data')

# Create file uploader object
upload_file = st.file_uploader('Upload a file containing earthquake data')

# Check to see if a file has been uploaded
if upload_file is not None:
    # Read the file to a dataframe using pandas
    df = pd.read_csv(upload_file)

    # Create a section for the dataframe statistics
    st.header('Statistics of Dataframe')
    st.write(df.describe())

    # Create a section for the dataframe header
    st.header('Header of Dataframe')
    st.write(df.head())

    # Create a section for the dataframe info
    st.header('Info of Dataframe')

    # dataframe.info default output to stdout not to streamlit.
    # see this link https://discuss.streamlit.io/t/direct-the-output-of-df-info-to-web-page/14894
    import io
    buffer = io.StringIO()
    df.info(buf=buffer)
    txt = buffer.getvalue()
    st.text(txt)



    # Create a section for matplotlib figure
    st.header('Plot of Data')
    fig, ax = plt.subplots(1, 1)
    ax.scatter(x=df['Depth'], y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')
    st.pyplot(fig)
