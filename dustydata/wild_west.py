# This is a data wrangling class:
import pandas as pd 
import numpy as np

class johnWayne:
    
    def __init__(self, dataframe, check_null=True):
        self.dataframe = dataframe
        self.check_null = check_null
        self.main()
        
    def __check_nulls__(self):
        null_dictionary = {}
        for e, i in enumerate(self.dataframe.isnull().sum()):
            if i > 0:
                null_dictionary[e] = i
        print(null_dictionary)
        
    def main(self):
        if self.check_null == True:
            self.__check_nulls__()


df = pd.DataFrame({0: ['g', 'g', 'g', 'y', 't', 'u', 'o'],
                    1: ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
                    2: ['b', 'b', np.nan, 'b', 'b', 'b', 'b'],
                    3: ['t', np.nan, 'f', 'f', 't', 'h', 'j'],
                    4: ['f', 'h', 'd', 'k', 'j', 'y', 'j']})

jw = johnWayne(df, False)
        
    
        
        

