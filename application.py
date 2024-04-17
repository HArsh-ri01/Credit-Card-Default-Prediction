import streamlit as st
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

def predict_datapoint(data):
    pred_df = data.get_data_as_data_frame()
    print(pred_df)

    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    if results[0] == 1:
        prediction = "Default in the next month"
    elif results[0] == 0:
        prediction = "Not be Default in the next month"
    
    return prediction

def main():
    st.title('Credit Default Prediction')

    limit_bal = st.number_input('LIMIT_BAL', value=0)
    sex = st.radio('SEX', ['Male', 'Female'])
    age = st.number_input('AGE', value=0)
    pay_1 = st.number_input('PAY_1', value=0)
    pay_2 = st.number_input('PAY_2', value=0)
    pay_3 = st.number_input('PAY_3', value=0)
    pay_4 = st.number_input('PAY_4', value=0)
    pay_5 = st.number_input('PAY_5', value=0)
    pay_6 = st.number_input('PAY_6', value=0)
    bill_amt1 = st.number_input('BILL_AMT1', value=0)
    bill_amt2 = st.number_input('BILL_AMT2', value=0)
    bill_amt3 = st.number_input('BILL_AMT3', value=0)
    bill_amt4 = st.number_input('BILL_AMT4', value=0)
    bill_amt5 = st.number_input('BILL_AMT5', value=0)
    bill_amt6 = st.number_input('BILL_AMT6', value=0)
    pay_amt1 = st.number_input('PAY_AMT1', value=0)
    pay_amt2 = st.number_input('PAY_AMT2', value=0)
    pay_amt3 = st.number_input('PAY_AMT3', value=0)
    pay_amt4 = st.number_input('PAY_AMT4', value=0)
    pay_amt5 = st.number_input('PAY_AMT5', value=0)
    pay_amt6 = st.number_input('PAY_AMT6', value=0)
    education_grade_school = st.checkbox('EDUCATION_Grade_School')
    education_high_school = st.checkbox('EDUCATION_High_School')
    education_others = st.checkbox('EDUCATION_Others')
    education_university = st.checkbox('EDUCATION_University')
    marriage_married = st.checkbox('MARRIAGE_Married')
    marriage_others = st.checkbox('MARRIAGE_Others')
    marriage_single = st.checkbox('MARRIAGE_Single')

    if st.button('Predict'):
        data = CustomData(
            LIMIT_BAL=limit_bal,
            SEX=sex,
            AGE=age,
            PAY_1=pay_1,
            PAY_2=pay_2,
            PAY_3=pay_3,
            PAY_4=pay_4,
            PAY_5=pay_5,
            PAY_6=pay_6,
            BILL_AMT1=bill_amt1,
            BILL_AMT2=bill_amt2,
            BILL_AMT3=bill_amt3,
            BILL_AMT4=bill_amt4,
            BILL_AMT5=bill_amt5,
            BILL_AMT6=bill_amt6,
            PAY_AMT1=pay_amt1,
            PAY_AMT2=pay_amt2,
            PAY_AMT3=pay_amt3,
            PAY_AMT4=pay_amt4,
            PAY_AMT5=pay_amt5,
            PAY_AMT6=pay_amt6,
            EDUCATION_Grade_School=education_grade_school,
            EDUCATION_High_School=education_high_school,
            EDUCATION_Others=education_others,
            EDUCATION_University=education_university,
            MARRIAGE_Married=marriage_married,
            MARRIAGE_Others=marriage_others,
            MARRIAGE_Single=marriage_single
        )
        prediction = predict_datapoint(data)
        st.write('Prediction:', prediction)

if __name__ == '__main__':
    main()
