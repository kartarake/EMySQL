import pandas as pd
import decimal
import time

def exporttable(data:list, headings:list, path:str) -> decimal.Decimal:
    start_time = decimal.Decimal(time.time())
    df = pd.DataFrame(data, columns=headings)
    df.to_excel(path, index=False)
    end_time = decimal.Decimal(time.time())
    return end_time - start_time