import pandas as pd
fish = pd.read_csv('https://bit.ly/fish_csv_data')
fish.head()

print(pd.unique(fish['Species']))
fish_input = fish[['Weight', 'Length','Diagonal','Height','Width']].to_numpy()

