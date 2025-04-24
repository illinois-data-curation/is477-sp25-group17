Status Interim Report 
Week 1: Data Acquisition & Integration (Completed)
- Successfully read in both of our datasets into pandas dataframes in VS code 
- Investigated the data quality of each dataset to confirm accuracy of the imports
- Integrated the two individual datasets into one cohesive dataset by merging on  their common variable (Building ID)
Week 2: Data Cleaning (Completed)
- Identified key features of our data (17288 rows x 27 columns)
- Investigated missing values by feature variable 
- Key variables in our analysis will be water_use_kgal, natural_gas_use_kbtu, electricity_use_kbtu, community_area, and total_ghg_emissions_metric_tons_co2e
Note: water use variable is missing  ~ 88% of its data, which is too high for us to draw reliable conclusions from. We will explore the relationship in the small subset of data we do have but note that our findings will not be generalizable.
Note: gas use variable is missing ~ 20% of its data. We opted to drop rows with missing gas use data, retaining ~ 80% of total data, instead of inputting replacement values to avoid skewing key distributions or relationships.
Note: we made the same decision with electricity use, which is missing ~ 16% 
Standardized variables with large ranged for consistency in analysis (including: electricity_use_kbtu, natural_gas_use_kbtu, gross_floor_area_buildings_sq_ft, total_ghg_emissions_metric_tons_co2e, ghg_intensity_kg_co2e_ft)
Week 3: Data Visualization (Completed)
Computed summary statistics to understand underlying data structures and distributions
Visualized relationships between water, gas, and electricity and total GHG emissions through individual scatter plots
Electricity initially displays the most linear relationship with GHG emissions 
Conducted correlation analysis of water, gas, electricity, and total GHG emissions to confirm trends seen in scatter plots
Visualize correlations in a heat mat for easy visual analysis 
Performed ANOVA tests to compare emissions across different community areas
P-value =  6.64e^-136 < 0.0.5 -> there is a statistically significant difference in mean GHG emissions across different community areas
Week 4: Documentation & Results Presentation (To be completed)
Generate more visualizations if necessary to effectively present insights and trends
Summarize key findings and connect them to the research questions
Compare results with initial hypotheses to assess accuracy

*At this stage, we have not made any significant changes to our project plan. However, we anticipate conducting additional statistical analyses and generating further visualizations during Week 4 to strengthen the support for our findings.

*The code corresponding to our completed analysis is available in the attached .ipynb file on GitHub. All sections are clearly labeled with relevant headers for easy navigation.
