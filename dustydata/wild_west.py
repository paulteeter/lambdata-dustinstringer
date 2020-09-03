# This is a data wrangling class:
import pandas as pd 
import numpy as np

class johnWayne:
    """
    Data Wrangling Class
    
    ex:
    new_wrangler = johnWayne(dataframe)
    """
    
    def __init__(self, dataframe, check_null=True, 
                 check_data_types=True):
        self.dataframe = dataframe
        self.check_null = check_null
        self.check_data_types = check_data_types
        self.main()
        
    def main(self):
        """
        Main function to run when the class is instantiated.
        These functions can be enabled and disabled as params in the
        class instance.
        """
        if self.check_null == True:
            self.__check_nulls__()
            
        if self.check_data_types == True:
            self.__check_data_types__()
        
    def __check_nulls__(self):
        """
        Checks for null values in a data frame and 
        returns the sum of nulls in a column.
        """
        null_dictionary = {}
        for e, i in enumerate(self.dataframe.isnull().sum()):
            if i > 0:
                null_dictionary[e] = i
        print(null_dictionary)
        
    def __check_data_types__(self):
        """
        Returns the datatypes of each series in a data frame.
        """
        print(self.dataframe.dtypes)
        
    def cardinality_cutter(self, threshold=50):
        """
        Cut the cardinality of categorical data.
        Return a list of features that made the cut.
        """
        card = self.dataframe.select_dtypes(exclude='number').nunique()
        card_cut = card[card <= threshold].index.tolist()
        return card_cut 


df = pd.DataFrame({0: [1, 2.9, 3, 4, 5, 6, 7],
                    1: ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
                    2: ['b', 'b', np.NaN, 'b', 'b', 'b', 'b'],
                    3: ['t', np.NaN, 'f', 'f', 't', 'h', 'j'],
                    4: ['f', 'h', 'd', 'k', 'j', 'y', 'j']})

jw = johnWayne(df, False, False)
print(jw.cardinality_cutter(threshold=5))
        
    
        
        

