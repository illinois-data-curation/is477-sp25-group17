## Overview
This project aims to analyze greenhouse gas emissions (GHG) in Chicago buildings by merging data from the Chicago Energy Benchmarking Dataset and the Chicago Energy Benchmarking Buildings Covered Dataset. Our analysis will evaluate the effectiveness of the city's energy efficiency and identify areas of weakness where additional city policies and improvements may be needed. Our findings could add to the ongoing discussion and progress of environmental sustainability and policy effectiveness in urban energy management. 

## Research Question 
- What are the individual relationships between Water, Gas, and Electricity with Total GHG Emissions and how does each relationship compare to the others? 
- Is there a significant difference in the Total GHG Emissions across different Community Areas?

## Team 
**Members:**
- Ashley Witte (agwitte2@illinois.edu)
- Harshi Vetrivel (hvetr2@illinois.edu)

**Responsibilities:**
  - Harshi: Data Acquisition + Integration
  - Ashley: Data Cleaning
  - Shared: Data Visualization and Results
    
## Datasets
1. [Chicago Energy Benchmarking Dataset](https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking/xq83-jr8c/data_preview)
   
The Chicago Energy Benchmarking dataset contains key data about energy and water use for large buildings (over 50,000 sq. ft) in the Chicago area as a part of the efforts for the Chicago Energy Benchmarking Ordinance. The buildings included in the dataset contribute to approximately 20% of the city’s total energy use, so they provide important information and context for monitoring and improving energy efficiency. Some key variables include building size, various energy sources (electricity, natural gas, steam), water use, Energy Star scores, and greenhouse gas emissions. Each building is identified through a unique Benchmarking ID and the precise location of the building is narrowed down through zip code and latitude/longitude data points. The data ranges from 2014 up to 2023, and the contributors aim to update every year to help offer insight into energy patterns across urban areas like Chicago over time.

2. [Chicago Energy Benchmarking - Covered Buildings](https://data.cityofchicago.org/browse?category=Environment+%26+Sustainable+Development&sortBy=most_accessed&pageSize=20&page=1)

This dataset lists all buildings required to follow the Chicago Energy Benchmarking Ordinance. It includes commercial, institutional, and residential buildings larger than 50,000 square feet. The main purpose of this dataset is to help building owners, managers, and representatives check if their property needs to comply with the ordinance by the June 1st annual deadline. Each building in this dataset is assigned a unique Chicago Energy Benchmarking ID. This ID is used to link the covered buildings dataset with the main energy benchmarking dataset, allowing for better analysis of energy performance across different buildings.

## Timeline
### **Week 1: Data Acquisition & Integration**
To be completed by: Harshi
- Develop scripts (Python) to import datasets
- Confirm data quality by cross-checking if datasets have imported accurately
- Create methods to integrate both datasets with a common variable (Building ID)

### **Week 2: Data Cleaning**  
To be completed by: Ashley
- Preprocess and clean missing/null values to ensure data completeness  
- Standardize variables with large ranges (e.g., building size) for consistency in analysis
- Document data cleaning and quality assessment steps

### **Week 3: Data Visualization** 
To be completed by: Both
- Compute summary statistics to understand data distribution.
- Generate initial visualizations (histograms, box plots, bar plots, pie charts, etc.)
- Document the rationale behind visualization choices and analysis methods
- Conduct correlation analysis to assess relationships between water, gas, and electricity and total GHG emissions
- Perform ANOVA tests to compare emissions across different community areas 

### **Week 4: Documentation & Results Presentation**
To be completed by: Both
- Generate more visualizations (e.g., map) if necessary to effectively present insights and trends  
- Summarize key findings and connect them to the research questions  
- Compare results with initial hypotheses to assess accuracy 
