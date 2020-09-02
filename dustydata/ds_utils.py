def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100

print(enlarge(5))


def cardinality_cutter(df, threshold):
    """
    Cut the cardinality of categorical data.
    """
    card = df.select_dtypes(exclude='number').nunique()
    card_cut = card[card <= threshold].index.tolist()
    return card_cut    

if __name__ == '__main__':  # run the name space when impoted in test_functions
    
    import pandas as pd
    df = pd.DataFrame({0: [2, 3, 2, 3, 2, 3, 3],
                       1: [3, 3, 3, 3, 3, 3, 3],
                       2: [4, 4, 4, 4, 4, 4, 4],
                       3: [5, 4, 4, 3, 2, 5, 3],
                       4: [5, 4, 3, 2, 5, 4, 6]})
    df = cardinality_cutter(df, 5)
    print(df)
    
    
    