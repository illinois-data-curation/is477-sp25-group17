import pandas as pd
  
url = "https://data.cityofchicago.org/resource/xq83-jr8c.csv?$limit=17728"
df_energy = pd.read_csv(url)
df_energy.to_csv("data/energy_data.csv", index=False)

url_covered = "https://data.cityofchicago.org/resource/g5i5-yz37.csv?$limit=11460"
df_buildings = pd.read_csv(url_covered)
df_buildings.to_csv("data/buildings_data.csv", index=False)

df_energy = df_energy.rename(columns={'id': 'building_id'})

merged_data = pd.merge(df_energy, df_buildings, on='building_id', how='inner')
merged_data.to_csv('data/merged_data.csv', index=False)

df_clean = merged_data.dropna(subset=['total_ghg_emissions_metric_tons_co2e', 'natural_gas_use_kbtu', 'electricity_use_kbtu'])

df_clean.to_csv("data/cleaned_data.csv", index=False)
