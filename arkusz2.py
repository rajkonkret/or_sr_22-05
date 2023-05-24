import pandas as pd
# as oznacza jako alias
#  pip install pandas

excel_data = pd.read_excel('sales.xlsx')
# wczyta wybrane kolumny
# data = pd.DataFrame(excel_data, columns=['Sales Date', 'Amount'])
# wczyta wszystkie kolumny
data = pd.DataFrame(excel_data)

# podmiana wartosci w wiersz w danej kolumnie
data.loc[0, 'Sales Person'] = "Radek"
print(data)
print(type(data))
print(data.columns)
print(data.values)

val2 = data['Amount'].to_list()
print(val2)

# 11:30
