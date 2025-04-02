## Overview

## Research Question 

## Team 
**Members:**
- Ashley Witte (agwitte2@illinois.edu)
- Harshi Vetrivel (hvetr2@illinois.edu)

**Responsibilities:**
  - Harshi: Data Cleaning: 
  - Ashley: Descriptive Analytics
  - Shared: Data Analysis, Visualization, and Results
    
## Datasets
1. [Chicago Energy Benchmarking Dataset](https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking/xq83-jr8c/data_preview)
   
The Chicago Energy Benchmarking dataset contains key data about energy and water use for large buildings (over 50,000 sq. ft) in the Chicago area as a part of the efforts for the Chicago Energy Benchmarking Ordinance. The buildings included in the dataset contribute to approximately 20% of the city’s total energy use, so they provide important information and context for monitoring and improving energy efficiency. Some key variables include building size, various energy sources (electricity, natural gas, steam), water use, Energy Star scores, and greenhouse gas emissions. Each building is identified through a unique Benchmarking ID and the precise location of the building is narrowed down through zip code and latitude/longitude data points. The data ranges from 2014 up to 2023, and the contributors aim to update every year to help offer insight into energy patterns across urban areas like Chicago over time.

2. [Chicago Energy Benchmarking - Covered Buildings](https://data.cityofchicago.org/browse?category=Environment+%26+Sustainable+Development&sortBy=most_accessed&pageSize=20&page=1)

This dataset lists all buildings required to follow the Chicago Energy Benchmarking Ordinance. It includes commercial, institutional, and residential buildings larger than 50,000 square feet. The main purpose of this dataset is to help building owners, managers, and representatives check if their property needs to comply with the ordinance by the June 1st annual deadline. Each building in this dataset is assigned a unique Chicago Energy Benchmarking ID. This ID is used to link the covered buildings dataset with the main energy benchmarking dataset, allowing for better analysis of energy performance across different buildings.

## Timeline
### **Week 1: Data Cleaning**
To be completed by: Harshi
- Preprocess and clean missing/null values to ensure data completeness  
- Standardize variables with large ranges (e.g., building size) for consistency in analysis  
- Link datasets through ID matching to integrate relevant information  

### **Week 2: Descriptive Analytics**  
To be completed by: Ashley
- Generate initial visualizations (histograms, box plots, bar plots, pie charts, etc.) to understand data distribution  
- Create correlation maps to identify key relationships between variables  
- Compute summary statistics to provide an overview of data characteristics 

### **Week 3: Data Analysis** 
To be completed by: Both
- Develop predictive models for deeper insights  
  - Perform **linear regression** to analyze emission rates  
  - Use **classification models** to analyze building size 
- Optimize model performance through hyperparameter tuning 
- Evaluate model effectiveness using performance metrics such as **R²** for regression and **Cohen’s Kappa** for classification 

### **Week 4: Documentation & Results Presentation**
To be completed by: Both
- Summarize key findings and connect them to the research questions  
- Compare results with initial hypotheses to assess accuracy 
- Generate visualizations (e.g., maps) to effectively present insights and trends  
