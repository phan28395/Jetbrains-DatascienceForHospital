import pandas as pd

pd.set_option('display.max_columns', 8)

hospital_general = pd.read_csv('general.csv') #Importing 3 csv Files
hospital_prenatal = pd.read_csv('prenatal.csv')
hospital_sports = pd.read_csv('sports.csv')

NaN = float("NaN")

list_column_general = list(hospital_general)# Set all columns in other 2 hospital to be the same as general hospital
hospital_prenatal.columns = list_column_general
hospital_sports.columns = list_column_general


all_hospital = pd.concat([hospital_general, hospital_prenatal, hospital_sports], ignore_index=True)#concat into a table
all_hospital.drop(columns='Unnamed: 0', inplace=True) #drop blank column

all_hospital.dropna(how='all', inplace=True) #drop all row that have missing values
#--------------------------------------------------------
all_hospital['gender'] = all_hospital['gender'].replace('man', 'm')
all_hospital['gender'] = all_hospital['gender'].replace('woman', 'f')
all_hospital['gender'] = all_hospital['gender'].replace('male', 'm')
all_hospital['gender'] = all_hospital['gender'].replace('female', 'f')
all_hospital['gender'] = all_hospital['gender'].replace(NaN, 'f')
#----------------------------------------------------------------
all_hospital['bmi'] = all_hospital['bmi'].fillna(0)
all_hospital['diagnosis'] = all_hospital['diagnosis'].fillna(0)
all_hospital['blood_test'] = all_hospital['blood_test'].fillna(0)
all_hospital['ecg'] = all_hospital['ecg'].fillna(0)
all_hospital['ultrasound'] = all_hospital['ultrasound'].fillna(0)
all_hospital['mri'] = all_hospital['mri'].fillna(0)
all_hospital['xray'] = all_hospital['xray'].fillna(0)
all_hospital['children'] = all_hospital['children'].fillna(0)
all_hospital['months'] = all_hospital['months'].fillna(0)

class Statistic:
    def highest_patient_finder(self): # return the hospital name that have highest patient number
        count_general = 0
        count_prenatal = 0
        count_sports = 0
        for hospital in all_hospital['hospital']:
            if hospital == 'general':
                count_general += 1
            elif hospital == 'prenatal':
                count_prenatal +=1
            elif hospital == 'sports':
                count_sports += 1
        if count_general == max(count_general, count_sports, count_prenatal):
            return print('The answer to the 1st question is General')
        elif count_prenatal == max(count_general, count_sports, count_prenatal):
            return print('The answer to the 1st question is Prenatal')
        elif count_sports == max(count_general, count_sports, count_prenatal):
            return print('The answer to the 1st question is Sports')

    def generalhospital_stomach_issues_share_calculator(self): #return the percentage of patient with stomach issues in General hospital
        count_stomach = 0
        filtered_dataframe = all_hospital.loc[(all_hospital['hospital'] == 'general')]
        count_index_general = max(filtered_dataframe.index) + 1
        for disease in filtered_dataframe['diagnosis']:
            if disease == 'stomach':
                count_stomach += 1
        return print(f'The answer to the 2nd question is {round(count_stomach / count_index_general, 3)}')



    def sporthospital_dislocation_issues_share_calculator(self):#return the percentage of patient with dislocation issues in Sports hospital
        count_dislocation = 0
        filtered_dataframe = all_hospital.loc[(all_hospital['hospital'] == 'sports')]
        filtered_dataframe.reset_index(inplace=True) # need to reset index back to 0,1,2...
        count_index_sports = max(filtered_dataframe.index) + 1

        for disease in filtered_dataframe['diagnosis']:
            if disease == 'dislocation':
                count_dislocation += 1
        return print(f'The answer to the 3rd question is {round(count_dislocation / count_index_sports, 3)}')

    def median_age_difference_general_sport(self):#return the difference in the median ages of the patients in the general and sports hospitals
        filtered_general = all_hospital.loc[(all_hospital['hospital'] == 'general')]
        filtered_sports = all_hospital.loc[(all_hospital['hospital'] == 'sports')]
        filtered_sports.reset_index(inplace=True)
        sum_age_general = filtered_general['age'].sum()
        sum_age_sports = filtered_sports['age'].sum()
        patient_num_general = max(filtered_general.index) + 1
        patient_num_sports = max(filtered_sports.index) + 1
        return print(f'The answer to the 4th question is {(sum_age_general / patient_num_general) - (sum_age_sports / patient_num_sports)}')
    
    def bloodtest_count_all_hospital(self): #return in which hospital the blood test was taken the most often
        count_prenatal = 0
        count_sports = 0
        for result in hospital_general['blood_test']:
            if result == 't':
                count_general += 1
        for result in hospital_prenatal['blood_test']:
            if result == 't':
                count_prenatal += 1
        for result in hospital_sports['blood_test']:
            if result == 't':
                count_sports += 1
        if count_general == max(count_general, count_prenatal, count_sports):
            return print(f'The answer to the 5th question is General, {count_general} blood tests')
        if count_prenatal == max(count_general, count_prenatal, count_sports):
            return print(f'The answer to the 5th question is Prenatal, {count_prenatal} blood tests')
        if count_sports == max(count_general, count_prenatal, count_sports):
            return print(f'The answer to the 5th question is Sport, {count_sports} blood tests')

if __name__ == '__main__':

    answer_question = Statistic()
    answer_question.highest_patient_finder()
    answer_question.generalhospital_stomach_issues_share_calculator()
    answer_question.sporthospital_dislocation_issues_share_calculator()
    answer_question.median_age_difference_general_sport()
    answer_question.bloodtest_count_all_hospital()
