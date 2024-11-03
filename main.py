import pandas as pd
from numpy.lib.recfunctions import join_by

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row['letter']: row['code'] for _,row in nato_df.iterrows()}

user_name = input("Enter your name: ").upper()

phonetic_code = [nato_dict[letter] for letter in user_name if letter in nato_dict]

print(phonetic_code)