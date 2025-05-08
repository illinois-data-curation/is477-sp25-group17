rule reproduce_all:
    input:
        "output/scatter_plots.png",
        "output/correlation_heatmap.png",
        "output/pie_chart.png",
        "output/avg_emissions_barplot.png",
        "output/anova_tukey_results.txt"
rule prepare_data:
    output:
        "data/energy_data.csv",
        "data/buildings_data.csv",
        "data/cleaned_data.csv"
    shell:
        "python scripts/prepare_data.py"
rule analyze_data:
    input:
        "data/cleaned_data.csv"
    output:
        "output/scatter_plots.png",
        "output/correlation_heatmap.png",
        "output/pie_chart.png",
        "output/avg_emissions_barplot.png",
        "output/anova_tukey_results.txt"
    shell:
        "python scripts/analyze_data.py"