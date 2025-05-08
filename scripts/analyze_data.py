import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import os

df_clean = pd.read_csv("data/cleaned_data.csv")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

#scatterplots
sns.scatterplot(x='water_use_kgal', y='total_ghg_emissions_metric_tons_co2e', data=df_clean, ax=axes[0])
axes[0].set_title('Water Use vs Total GHG Emissions')
axes[0].set_xlabel('Water Use (Kgal)')
axes[0].set_ylabel('Total GHG Emissions (Metric Tons CO2e)')

sns.scatterplot(x='electricity_use_kbtu', y='total_ghg_emissions_metric_tons_co2e', data=df_clean, ax=axes[1])
axes[1].set_title('Electricity Use vs Total GHG Emissions')
axes[1].set_xlabel('Electricity Use (KBtu)')
axes[1].set_ylabel('Total GHG Emissions (Metric Tons CO2e)')

sns.scatterplot(x='natural_gas_use_kbtu', y='total_ghg_emissions_metric_tons_co2e', data=df_clean, ax=axes[2])
axes[2].set_title('Natural Gas Use vs Total GHG Emissions')
axes[2].set_xlabel('Natural Gas Use (KBtu)')
axes[2].set_ylabel('Total GHG Emissions (Metric Tons CO2e)')

fig.suptitle('Figure 1: Scatter Plots of GHG Emissions vs Selected Features')
#plt.show()
fig.savefig("output/scatter_plots.png")

#correlation matrix 
correlation_matrix = df_clean[['water_use_kgal', 'electricity_use_kbtu', 'natural_gas_use_kbtu', 'total_ghg_emissions_metric_tons_co2e']].corr()
#print("\nCorrelation Matrix:")
#print(correlation_matrix)

fig2 = plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f')
plt.title('Figure 2: Correlation Heatmap of of GHG Emissions and Selected Features')
#plt.show()
fig2.savefig("output/correlation_heatmap.png")

#pie chart
top_10_community_areas = df_clean['community_area_name'].value_counts().head(5).index
filtered_data = df_clean[df_clean['community_area_name'].isin(top_10_community_areas)]
#print("Top 10 Most Common Community Areas:")
#print(top_10_community_areas)

community_areas_count = filtered_data.groupby('community_area_name').count()
community_areas_count

community_counts = df_clean['community_area_name'].value_counts()
top_5_communities = community_counts.head(5)

others_count = community_counts.iloc[5:].sum()
pie_data = top_5_communities.copy()
pie_data['Other'] = others_count

colors = sns.color_palette('Set3', len(pie_data))

fig3 = plt.figure(figsize=(10, 6))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops={'edgecolor': 'black'})
plt.title('Figure 3: Distribution of Community Areas (Highlighting Top 5)')
plt.tight_layout()
#plt.show()
fig3.savefig("output/pie_chart.png")

filtered_data = df_clean[df_clean['community_area_name'].isin(top_10_community_areas)]
avg_emissions = filtered_data.groupby('community_area_name')['total_ghg_emissions_metric_tons_co2e'].mean()

colors = sns.color_palette('Set3', len(pie_data))

fig4 = plt.figure(figsize=(10, 6))
avg_emissions.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Figure 4: Average GHG Emissions for Top 5 Community Areas')
plt.xlabel('Community Area')
plt.ylabel('Average GHG Emissions (Metric Tons CO2e)')
plt.xticks(rotation=45)
plt.tight_layout()
#plt.show()
fig4.savefig("output/avg_emissions_barplot.png")

# ANOVA & tukey tests
grouped_data_top5 = [group['total_ghg_emissions_metric_tons_co2e'].dropna() for _, group in filtered_data.groupby('community_area_name')]
anova_result_top5 = f_oneway(*grouped_data_top5)

#print("\nANOVA Test Result for Top 10 Community Areas:")
#print(f"F-statistic: {anova_result_top5.statistic}, p-value: {anova_result_top5.pvalue}")

with open("output/anova_tukey_results.txt", "w") as f:
    f.write("ANOVA test results:\n")
    f.write(str(f"F-statistic: {anova_result_top5.statistic}, p-value: {anova_result_top5.pvalue}"))
# Post-hoc analysis using Tukey's HSD
tukey = pairwise_tukeyhsd(endog=filtered_data['total_ghg_emissions_metric_tons_co2e'],
                          groups=filtered_data['community_area_name'],
                          alpha=0.05)

#print(tukey)
with open("output/anova_tukey_results.txt", "a") as f:
    f.write("\n\nTukey HSD results:\n")
    f.write(str(tukey))



