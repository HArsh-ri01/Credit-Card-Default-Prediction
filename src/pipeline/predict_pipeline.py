import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
        

class CustomData:
    def __init__(  self,
        LIMIT_BAL: float,
        SEX: float,
        AGE: int,
        PAY_1: float,
        PAY_2: float,
        PAY_3: float,
        PAY_4: float,
        PAY_5: float,
        PAY_6: float,
        BILL_AMT1: float,
        BILL_AMT2: float,
        BILL_AMT3: float,
        BILL_AMT4: float,
        BILL_AMT5: float,
        BILL_AMT6: float,
        PAY_AMT1: float,
        PAY_AMT2: float,
        PAY_AMT3: float,
        PAY_AMT4: float,
        PAY_AMT5: float,
        PAY_AMT6: float,
        EDUCATION_Grade_School: bool,
        EDUCATION_High_School: bool,
        EDUCATION_Others: bool,
        EDUCATION_University: bool,
        MARRIAGE_Married: bool,
        MARRIAGE_Others: bool,
        MARRIAGE_Single: bool,):

        self.LIMIT_BAL = LIMIT_BAL
        self.SEX = SEX
        self.AGE = AGE
        self.EDUCATION_Grade_School = EDUCATION_Grade_School
        self.EDUCATION_High_School = EDUCATION_High_School
        self.EDUCATION_Others = EDUCATION_Others
        self.EDUCATION_University = EDUCATION_University
        self.MARRIAGE_Married = MARRIAGE_Married
        self.MARRIAGE_Others = MARRIAGE_Others
        self.MARRIAGE_Single = MARRIAGE_Single
        self.PAY_1 = PAY_1
        self.PAY_2 = PAY_2
        self.PAY_3 = PAY_3
        self.PAY_4 = PAY_4
        self.PAY_5 = PAY_5
        self.PAY_6 = PAY_6
        self.BILL_AMT1 = BILL_AMT1
        self.BILL_AMT2 = BILL_AMT2
        self.BILL_AMT3 = BILL_AMT3
        self.BILL_AMT4 = BILL_AMT4
        self.BILL_AMT5 = BILL_AMT5
        self.BILL_AMT6 = BILL_AMT6
        self.PAY_AMT1 = PAY_AMT1
        self.PAY_AMT2 = PAY_AMT2
        self.PAY_AMT3 = PAY_AMT3
        self.PAY_AMT4 = PAY_AMT4
        self.PAY_AMT5 = PAY_AMT5
        self.PAY_AMT6 = PAY_AMT6


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "LIMIT_BAL": [self.LIMIT_BAL],
                "SEX": [self.SEX],
                "AGE": [self.AGE],
                "PAY_1": [self.PAY_1],
                "PAY_2": [self.PAY_2],
                "PAY_3": [self.PAY_3],
                "PAY_4": [self.PAY_4],
                "PAY_5": [self.PAY_5],
                "PAY_6": [self.PAY_6],
                "BILL_AMT1": [self.BILL_AMT1],
                "BILL_AMT2": [self.BILL_AMT2],
                "BILL_AMT3": [self.BILL_AMT3],
                "BILL_AMT4": [self.BILL_AMT4],
                "BILL_AMT5": [self.BILL_AMT5],
                "BILL_AMT6": [self.BILL_AMT6],
                "PAY_AMT1": [self.PAY_AMT1],
                "PAY_AMT2": [self.PAY_AMT2],
                "PAY_AMT3": [self.PAY_AMT3],
                "PAY_AMT4": [self.PAY_AMT4],
                "PAY_AMT5": [self.PAY_AMT5],
                "PAY_AMT6": [self.PAY_AMT6],
                "EDUCATION_Grade_School": [self.EDUCATION_Grade_School],
                "EDUCATION_High_School": [self.EDUCATION_High_School],
                "EDUCATION_Others": [self.EDUCATION_Others],
                "EDUCATION_University": [self.EDUCATION_University],
                "MARRIAGE_Married": [self.MARRIAGE_Married],
                "MARRIAGE_Others": [self.MARRIAGE_Others],
                "MARRIAGE_Single": [self.MARRIAGE_Single]
            }
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
