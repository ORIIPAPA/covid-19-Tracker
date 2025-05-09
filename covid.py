import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def main():
    # Set visualization style
    sns.set_style('whitegrid')
    plt.rcParams['figure.figsize'] = (12, 6)

    # 1. Data Collection and Loading
    try:
        df = pd.read_csv('owid-covid-data.csv')
        print("\nData loaded successfully!")
        print("Dataset shape:", df.shape)
    except FileNotFoundError:
        print("Error: Please download the dataset and save it as 'owid-covid-data.csv' in your working directory")
        return

    # 2. Data Exploration
    print("\nFirst 5 rows:")
    print(df.head())  # Replaced display() with print()

    print("\nMissing values summary:")
    missing_values = df.isnull().sum()
    print(missing_values[missing_values > 0].sort_values(ascending=False))

    # 3. Data Cleaning
    df['date'] = pd.to_datetime(df['date'])
    countries_of_interest = ['Kenya', 'United States', 'India', 'Brazil', 'United Kingdom']
    df_filtered = df[df['location'].isin(countries_of_interest)].copy()
    
    numeric_cols = ['total_cases', 'new_cases', 'total_deaths', 'new_deaths', 
                   'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated']
    df_filtered[numeric_cols] = df_filtered[numeric_cols].fillna(0)

    # 4. Exploratory Data Analysis
    # Plot total cases over time
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=df_filtered, x='date', y='total_cases', hue='location')
    plt.title('Total COVID-19 Cases Over Time')
    plt.ylabel('Total Cases')
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.savefig('total_cases.png')  # Save the figure
    plt.close()  # Close the figure to free memory

    # Plot total deaths over time
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=df_filtered, x='date', y='total_deaths', hue='location')
    plt.title('Total COVID-19 Deaths Over Time')
    plt.ylabel('Total Deaths')
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.savefig('total_deaths.png')
    plt.close()

    print("\nAnalysis complete! Check the generated PNG files for visualizations.")

if __name__ == "__main__":
    main()