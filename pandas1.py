import pandas as pd

# with pd.read_csv("C:/Users/abhis/PycharmProjects/Pandas/Data/SummerOlympics.csv", skiprows=4 ) as open_csv:
#     print(open_csv.head)

oo = pd.read_csv("Data/SummerOlympics.csv", skiprows=4 )
print(oo,oo['NOC'], type(oo['NOC']), oo['Edition'], oo['City'], oo['Athlete'], oo['Medal'])

