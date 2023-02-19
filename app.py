import pickle
import streamlit as st

# loading the trained model

# pickle_in=open('predicter.pkl','rb')
# predicter=pickle.load(pickle_in)

@st.cache()

# defining the function to make the prediction  using the data which the user inputs
def Prediction(county,month):
    prediction=predicter.predict([[county,month]])
    

# defining function for webpage

def main():
    # front-end
    html_temp = """ 
    <div style ="background-color:lightblue;padding:14px"> 
    <h1 style ="color:black;text-align:center;"> Malaria Commodities Demand Prediction Model</h1> 
    </div> 
    """
    # Set the theme of the app
    st.set_page_config(page_title='My App', page_icon=':smiley:', layout='wide')

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # following lines create boxes in which user can enter data required to make prediction
    county = st.selectbox('County', ('Baringo County', 'Bomet County', 'Bungoma County', 'Busia County',
       'Elgeyo Marakwet County', 'Embu County', 'Garissa County',
       'Homa Bay County', 'Isiolo County', 'Kajiado County', 'Kakamega County',
       'Kericho County', 'Kiambu County', 'Kilifi County', 'Kirinyaga County',
       'Kisii County', 'Kisumu County', 'Kitui County', 'Kwale County',
       'Laikipia County', 'Lamu County', 'Machakos County', 'Makueni County',
       'Mandera County', 'Marsabit County', 'Meru County', 'Migori County',
       'Mombasa County', 'Muranga County', 'Nairobi County', 'Nakuru County',
       'Nandi County', 'Narok County', 'Nyamira County', 'Nyandarua County',
       'Nyeri County', 'Samburu County', 'Siaya County', 'Taita Taveta County',
       'Tana River County', 'Tharaka Nithi County', 'Trans Nzoia County',
       'Turkana County', 'Uasin Gishu County', 'Vihiga County', 'Wajir County',
       'West Pokot County'))
    month = st.selectbox('Month of the year', ("January", "February","March","April","March","April","May","June","July","August","September","October","November","December"))
    commodities = ""
    result=""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(county, month)
        st.success('County Commodity is {}'.format(result))
        print(commodities)


if __name__ == '__main__':
    main()