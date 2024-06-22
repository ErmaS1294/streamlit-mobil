import pickle
import streamlit as st
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]{
	background-color:#F0F8FF;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title('Estimasi Harga Mobil Bekas')
st.image('Mobil BMW.jpg')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input KM Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input EngineSize')
 
predict = ''

if st.button('Estimasi Harga'):
	predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
	st.write('Estimasi harga mobil bekas dalam Ponds : ', predict)
	st.write('Estimasi harga mobil bekas dalam IDR (Juta) : ', predict*19000)