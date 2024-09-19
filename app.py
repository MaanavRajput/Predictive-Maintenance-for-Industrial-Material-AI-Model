import streamlit as st
import pickle  
import numpy as np

model=pickle.load(open("C:/Users/maana/OneDrive/Desktop/MAANAV/for_ThinkML/logistic_model.pkl", 'rb'))

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file) 
def main():
 st.set_page_config(page_title="Predictive maintenance AI", page_icon="🔍", layout="wide")
 st.title('AI Model Prediction Interface')

 air_temp = st.number_input('Air Temperature [K]', min_value=290, max_value=320, step=1)
 process_temp = st.number_input('Process Temperature [K]', min_value=290, max_value=320, step=1)
 rotational_speed = st.number_input('Rotational Speed [rpm]', min_value=100, max_value=5000, step=100)
 torque = st.number_input('Torque [Nm]', min_value=0, max_value=100, step=1)
 tool_wear = st.number_input('Tool Wear [min]', min_value=0, max_value=300, step=10)

 if st.button('Predict'):
    try:
       
        input_data = np.array([[air_temp, process_temp, rotational_speed, torque, tool_wear]])
        
   
        input_data_scaled = scaler.transform(input_data)
        
    
        prediction = model.predict(input_data_scaled)  
        
    
        if prediction[0] == 1:
            st.write('Prediction: The machine is likely to fail.')
        else:
            st.write('Prediction: The machine is unlikely to fail.')
    except Exception as e:
        st.write(f"Error: {e}")
if __name__=='__main__':
  main()
