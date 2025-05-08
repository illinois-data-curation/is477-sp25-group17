need to add:
Reproducing: Sequence of steps required for someone else to reproduce your results.
References: Formatted citations for any papers, datasets, or software used in your project.

# Analysis of Greenhouse Gas Emission Patterns in Chicago

Archival Record:
## Contributors 
**Members:**
- Ashley Witte (agwitte2@illinois.edu)
- Harshi Vetrivel (hvetr2@illinois.edu)
  
**Responsibilities:**
  - Harshi: Data Cleaning
  - Ashley: Descriptive Analytics
  - Shared: Data Analysis, Visualization, and Results

## Summary
This project investigates the environmental impact of large buildings in Chicago by analyzing energy usage and greenhouse gas (GHG) emissions data. Specifically, we will integrate two publicly available data sets from the City of Chicago, the Chicago Energy Benchmarking Dataset and the Chicago Energy Benchmarking Buildings Covered Dataset. The resulting merged dataset contains key factors including water use, energy use, gas use, building characteristics, and GHG emissions for commercial, institutional, and residential properties larger than 50,000 square feet. Through this project we will explore how building specific resource usage correlates with total greenhouse gas emissions and how these emissions vary across different community areas within the city of Chicago. 

Our motivation for this project stemmed from a growing interest in urban sustainability and data-driven environment policy. Our analysis will evaluate the effectiveness of the city's energy initiatives and identify areas of weakness where additional city policies and improvements may be needed. Our findings could add to the ongoing discussion and progress of environmental sustainability and policy effectiveness in urban energy management. 

Specifically, our project aimed to answer 2 main research questions:
1. What are the individual relationships between Water, Gas, and Electricity with Total GHG Emissions and how does each relationship compare to the others? 
2. Is there a significant difference in the Total GHG Emissions across different Community Areas?

To answer these questions we began by merging our two individual datasets into one combined dataset on their shared variable, building ID. We then cleaned our data, focusing mainly on key variables such as electricity_use_kbtu, natural_gas_use_kbtu, water_use_kgal, and total_ghg_emissions_metric_tons_co2e, to ensure we were conducting our analysis on the most representative data possible. We then used summary statistics, scatterplots, correlation heatmaps, and statistical testing, including methods such as ANOVA and Tukey’s HSD to answer our research questions. 

We found that there were substantial linear relationships between all investigated variables, electricity, water, and gas use, and GHG emissions. Among these variables, electricity use had  the strongest linear relationship with GHG emissions, achieving a correlation coefficient of 0.95. This suggests that buildings with higher electricity consumption tend to emit higher levels of greenhouse gas emissions. The other two variables, water and gas use, also had positive correlations with GHG emissions, achieving correlation coefficients of 0.64 and 0.61 respectively. 

We also found that there was a significant difference between the average GHG emissions across different community areas. We conducted ANOVA and Tukey HSD tests to confirm these findings. We specifically investigated the average GHG emissions of the top 5 community areas with the most large buildings and found that the Loop had significantly higher average emissions than the other 4 community areas. Additionally, communities like Lake View and Lincoln Park had lower average emissions. These results suggest that location plays a crucial role in shaping emissions. The emission differences between these locations are likely a result of differences in building density, function, and infrastructure. 

## Data Profile
To conduct meaningful analysis of energy use across large building in Chicago, we integrated two datasets: 

1. [Chicago Energy Benchmarking Dataset](https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking/xq83-jr8c/data_preview)

The Chicago Energy Benchmarking dataset contains key data about energy and water use for large buildings (over 50,000 sq. ft) in the Chicago area as a part of the efforts for the Chicago Energy Benchmarking Ordinance. The buildings included in the dataset contribute to approximately 20% of the city’s total energy use, so they provide important information and context for monitoring and improving energy efficiency. Some key variables include building size, various energy sources (electricity, natural gas, steam), water use, Energy Star scores, and greenhouse gas emissions. Each building is identified through a unique Benchmarking ID and the precise location of the building is narrowed down through zip code and latitude/longitude data points. The data ranges from 2014 up to 2023, and the contributors aim to update every year to help offer insight into energy patterns across urban areas like Chicago over time.

2. [Chicago Energy Benchmarking - Covered Buildings](https://data.cityofchicago.org/browse?category=Environment+%26+Sustainable+Development&sortBy=most_accessed&pageSize=20&page=1)

This dataset lists all buildings required to follow the Chicago Energy Benchmarking Ordinance. It includes commercial, institutional, and residential buildings larger than 50,000 square feet. The main purpose of this dataset is to help building owners, managers, and representatives check if their property needs to comply with the ordinance by the June 1st annual deadline. Each building in this dataset is assigned a unique Chicago Energy Benchmarking ID. This ID is used to link the covered buildings dataset with the main energy benchmarking dataset, allowing for better analysis of energy performance across different buildings.

### License/Terms of Use

Our project uses datasets provided by the City of Chicago. The terms of use states that “The City of Chicago makes no claims as to the content, accuracy, timeliness, or completeness of the data. The data is subject to change and is used at one’s own risk”. For our research purposes, we have modified the data to gather meaningful answers to our research questions.  

### Data Integration
To integrate data from our two separate datasets into one cohesive dataset we merged them on their shared feature, building ID, which uniquely identifies each building across both datasets. In the Chicago Energy Benchmarking Dataset this feature is represented by the variable “id” and in the Chicago Energy Benchmarking - Covered Buildings dataset this feature is represented by the variable “building_id”. This method allows each record of performance data (per year) to be linked with static building attributes from the covered buildings list.

We used Python, with the pandas library, for this integration process. The corresponding scripts for data merging can be found in `scripts/prepare_data.py`

### Data Cleaning

In answering our two main research questions we identified water_use_kgal, natural_gas_use_kbtu, electricity_use_kbtu, community_area, and total_ghg_emissions_metric_tons_co2e as key variables for our analysis. For that reason we prioritize those variables during our data cleaning process. 
To clean our newly merged dataframe we investigated missing values by feature variable. We found multiple variables with high rates of missing values but focused on resolving this issue primarily for our identified key variables. This prevented us from over dropping data and losing information that was critical to our analysis. 
Of our key variables water_use_kgal was of the highest concern at this stage. It was missing around 88% of its total data. To combat this issue we decided not to drop all water use missing values in efforts to retain as much useful information in the overall dataframe. Instead we noted that this missing value percentage was too high for us to draw reliable conclusions from and opted to explore the resulting relationship in the small subset of data we do have, but to note additionally that our findings will not be generalizable. 
Another two key variables, natural_gas_use_kbtu and electricity_use_kbtu, were of slight concern, missing around 20% and 16% of total data respectively. In this case we opted to drop rows with missing values for both variables, retaining around 80% and 84% of total data respectively. We made the choice of dropping missing values rather than inputting replacement values to avoid skewing key distributions and relationships. 

## Findings

To begin our analysis we computed summary statistics to understand underlying data structures and distributions. Then to investigate further the relationship between water, gas, and electricity and total GHG emissions we created scatterplots, see Figure 1, visualizing each relationship individually.

![scatter_plots](https://github.com/user-attachments/assets/d3e97466-7109-4f6a-8fac-3f9efbed8346)

Through these visualizations we identified that electricity had the strongest linear relationship with GHG emissions. We then conducted a correlation analysis and investigated the corresponding correlation coefficients for each relationship to quantify these results. For easy visual analysis we displayed these correlations in a heat map, see Figure 2.

![correlation_heatmap](https://github.com/user-attachments/assets/c7470e8a-567b-4bab-b621-6b98a220f0ee)

The heat map confirmed that of the 3 variables electricity use was the most highly correlated with total GHG emissions, having a correlation coefficient of 0.95. This close to perfect positive relationship indicates that buildings using more energy tend to emit significantly more greenhouse gas emissions. This finding makes sense since normally generating energy, especially when not from renewable sources, produced greenhouse gas emissions. Natural gas use and water use also have significant positive relationships with total GHG emissions with correlation coefficients of 0.64 and 0.61 respectively. It is important to note that additional research should be done to confirm our findings associated with water usage since that variable is underrepresented in our dataframe. 

These findings suggest that targeting electricity usage could yield the largest reduction in greenhouse gas emissions, but also that a holistic approach, targeting multiple resource usages, would be the most beneficial in sustainability efforts. The relatively strong correlations between water, gas, and electricity usage and total GHG emissions also highlights how interconnected building operations are when it comes to energy use and environmental impact.  

In investigating the relationships between community areas and Total GHG Emissions we conducted several statistical tests to confirm whether there is a significant difference in the Total GHG Emissions across different Community Areas. Specifically, we chose to examine relationships of the 5 most common community areas so we subsetted out the 5 community areas with the most corresponding buildings in our dataframe. The breakdown of those 5 most common community areas can be seen below in Figure 3. 

![pie_chart](https://github.com/user-attachments/assets/c8b10e76-2ba7-4996-ae9e-856d2e6ded30)

Initial analysis of these 5 community areas showed that on average the Loop was the community with the highest GHG emissions, closely followed by the Near North Side community and the Near West Side community. Figure 4 below visualizes those distributions.

![avg_emissions_barplot](https://github.com/user-attachments/assets/a32d31b5-f09f-4937-85f0-6b9a4f8874cb)

To confirm the statistical significance in differences between these communities we performed an ANOVA test on those areas to compare emissions. Our ANOVA test resulted in a p-value of 1.12e^-62 which confirmed that there is a statistically significant difference between the mean GHG emissions of at least one community area. To gain deeper insight into the individual relationships between each community area and GHG emissions, we then conducted a Tukey HSD test. The resulting table from this test can be seen below in Figure 5.


<img width="590" alt="Screenshot 2025-05-08 at 5 17 53 PM" src="https://github.com/user-attachments/assets/9b8b7b43-6065-4022-a5cb-5cf7cf21b909" />

This table shows that several community areas differ significantly in their mean GHG emissions. It also confirms from Figure 4 that the Loop is a community that has significantly higher emissions compared to Lake View, Lincoln Park, Near North Side, and Near West Side. These findings align with those from the  ANOVA test, reinforcing that geographic location within Chicago contributes to substantial variation in emissions. From this table we can also see that not all differences were significant. Specifically, we see that Lake View and Lincoln Park as well as Near North Side and Near West Side showed statistically similar emission profiles.

From these results we can infer targeted sustainability recommendations. Since the Loop was identified as a high emission zone, it might benefit from stricter energy efficiency policies or district-wide heating/cooling upgrades. On the other hand, lower emissions zones, such as Lake View and Lincoln Park could serve as models for sustainable urban development. In either case, these findings reinforce that sustainable energy strategies should be evaluated individually for different communities, taking into account the unique emission profiles and infrastructure of each area.

## Future Work

A key takeaway from working on this project was learning the distinction between working with real-world datasets versus pre-modified ones, especially when they originate from public sources such as the City of Chicago Data Portal. Being able to successfully complete the cleaning and preprocessing steps required a thorough understanding of our research questions so that we could bridge the gap between our raw data and the meaningful insights we were trying to get to. We utilized skills and techniques learned through this class and previous coursework to standardize and remove data when necessary. We often had to go back and retrace our steps back to the initial preprocessing stage when we encountered errors in our later analyses. Additionally, we found that it was often valuable to take a step back from the technical side of the project and look at the bigger picture. By keeping the context of our research questions and overall project goals in mind, we were able to thoroughly analyze relationships between variables like electricity, gas, water, and community area and how they affect total greenhouse gas emission patterns in Chicago. Oftentimes in coursework, we tend to forget the bigger picture and focus on the details, so this project encouraged us to understand our work on a deeper level. 

There are plenty of opportunities to expand or improve this project in the future. A major one would be to incorporate data across multiple years. Right now, our range is 2014-2023 but a wider range could give us a more holistic view of trends and patterns in emission rates across time. This could provide major insights into the energy efficiency of the city during different historical events, evolutions of community areas, and more. Another area that we did not have the opportunity to explore in this project would be to include socioeconomic data for each community area that we used as a part of our data analysis. We could investigate concerns related to environmental equity, like if lower-income neighborhoods were more or less affected by high-emission buildings in their area. This could also lead to identifying communities that are being overlooked in energy saving efforts. Another great idea would be to introduce predictive models that could give us insight into the expected emission rates of buildings with certain characteristics. If we could turn that predictive model into something that can be used by city planners or sustainability organizations, it may be able to introduce an accessible way to produce buildings with minimized harm to the environment. We also think it would be interesting to interview building managers and/or city officials to gain insight into what kinds of improvements are actually being implemented in their fields and how public policy influences the patterns that we see. We could also research Chicago’s energy and climate policies to identify how the data may intersect. Understanding the policies could make our project more relevant for real-world usage.

Overall, there's a lot of potential to grow our project into a deeper investigation into the sustainability practices of urban cities like Chicago. With more datasets, modeling techniques, and added context, future work could offer more meaningful insights into how Chicago can reduce its building-related emissions.

