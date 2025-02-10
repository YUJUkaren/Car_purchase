import streamlit as st
import pickle
import pandas as pd


st.title('Car Purchase Prediction')
st.write('This web app predicts the **Car Price**')

# 讀取模型
model = pickle.load(open('model_yu.pkl', 'rb'))

# 用戶輸入
Gender = st.selectbox('Gender', ['Male', 'Female'])
Age = st.number_input('Age', min_value=18, max_value=100, step=1)
Annualsalary = st.number_input('Annual Salary', min_value=0, step=1000)
Purchased = st.selectbox('Purchased', [0, 1])

# One-Hot Encoding（將性別轉換為數值特徵）
Gender_Female = 1 if Gender == 'Female' else 0
Gender_Male = 1 if Gender == 'Male' else 0

# 轉換為 DataFrame，確保欄位名稱與模型訓練時相同
user_data = pd.DataFrame({
    'AnnualSalary': [Annualsalary],
    'Age': [Age],
    'Gender_Female': [Gender_Female],
    'Gender_Male': [Gender_Male]
})


user_data = pd.DataFrame({
    'AnnualSalary': [float(Annualsalary)]
})

# 預測
if st.button('Predict'):
    prediction = model.predict(user_data)
    st.write(f'The predicted car price is: {prediction[0]:,.2f}')
