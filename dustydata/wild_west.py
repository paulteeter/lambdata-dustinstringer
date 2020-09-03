# This is a data wrangling class:
import pandas as pd 
import numpy as np

class johnWayne:
    
    def __init__(self, dataframe, check_null=True, 
                 check_data_types=True):
        self.dataframe = dataframe
        self.check_null = check_null
        self.check_data_types = check_data_types
        self.main()
        
    def __check_nulls__(self):
        null_dictionary = {}
        for e, i in enumerate(self.dataframe.isnull().sum()):
            if i > 0:
                null_dictionary[e] = i
        print(null_dictionary)
        
    def __check_data_types__(self):
        print(self.dataframe.dtypes)
        
    def main(self):
        if self.check_null == True:
            self.__check_nulls__()
        if self.check_data_types == True:
            self.__check_data_types__()


df = pd.DataFrame({0: [1, 2.9, 3, 4, 5, 6, 7],
                    1: ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
                    2: ['b', 'b', np.NaN, 'b', 'b', 'b', 'b'],
                    3: ['t', np.NaN, 'f', 'f', 't', 'h', 'j'],
                    4: ['f', 'h', 'd', 'k', 'j', 'y', 'j']})

jw = johnWayne(df)
        
    
        
        

