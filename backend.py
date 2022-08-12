
def processExcel(df):
    # function that converts marks to strings on value based threshold

    columns = df.iloc[:, 2:].columns
    for col in columns:
        df[col] = df[col].apply(lambda x : 'pass' if x > 40 else 'fail')

    df2 = df.copy()
    for col in columns:
        df2[col] = df2[col].apply(lambda x : True if x == 'pass' else False)

    resultList = []

    for row in df.index:
        passed = True
        for col in columns:
            passed = passed and df2[col][row]
            if(passed == False): break
        resultList.append((lambda x : 'Yes' if x == True else 'No')(passed))
    
    df["Result"] = resultList

    return df