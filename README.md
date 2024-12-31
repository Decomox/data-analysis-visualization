# Data Analysis and Visualization Project

This project demonstrates data analysis and visualization using Python, MySQL, and Tableau to generate insights from sales and inventory data.

## Project Overview
The project aims to:
1. Analyze incoming and outgoing stock data.
2. Generate business insights to support decision-making.
3. Create dashboards for data visualization.

## Datasets
- **Incoming Stock (`pemasukan_barang`)**: Contains 63 records of incoming stock data.
- **Outgoing Stock (`penjualan_barang`)**: Contains 1289 records of sales data.

## Analysis Performed
1. **Sales per Item**: Total sales grouped by item.
2. **Monthly Trends**: Monthly sales trends for each item.
3. **Profit Margin Analysis**: Average profit margin per item.
4. **Top Buyer**: Buyers with the highest transaction values.
5. **Stock Comparison**: Comparison of incoming and outgoing stock.
6. **Monthly Incoming Trends**: Trends of incoming stock per month.
7. **Frequent Buyers**: Buyers with the most transactions.

## Visualizations
The following dashboards were created using Tableau:
1. **Total Sales per Item**
2. **Monthly Sales Trends**
3. **Profit Margin Analysis**
4. **Stock Comparison**
5. **Monthly Incoming Trends**
6. **Top Buyer**
7. **Frequent Buyers**

## Technical Details
- **Language**: Python
- **Database**: MySQL
- **Visualization Tool**: Tableau
- **Scripts**:
  - `load_data.py`: Loads datasets into MySQL.
  - `analysis.py`: Performs data analysis and saves results.

## Installation and Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/data-analysis-visualization.git
2. Install required Python packages:
   ```bash
   pip install pandas sqlalchemy mysql-connector-python
3. Run the scripts
   - Load data into MySQL:
     ```bash
     python load_data.py
   - Perform analysis
     ```bash
     python analysis.py
     
## Business Insights
1. Key Findings:
   - Top Buyer: TOKO ENGKON with total transactions worth 2,047,000,000.
   - Most Sold Item: BERAS with 1,965,258 units sold.
   - Highest Margin: DAGING with an average profit margin of 71,216.
   - Overstock Issue: BERAS has significantly higher incoming stock than sales.
  
2. Recommendation:
   - Optimize stock management to avoid overstock of BERAS.
   - Increase marketing for high-margin items like DAGING.
   - Prepare for seasonal demand spikes in May and December.

## Author
Created by Muhammad Syifa Ridhoni
