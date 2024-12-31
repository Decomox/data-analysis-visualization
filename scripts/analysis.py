import pandas as pd
from sqlalchemy import create_engine

def save_analysis_to_mysql(engine, df, table_name):
    # Save DataFrame to MySQL
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"{table_name} saved to MySQL successfully.")

def run_analysis(engine):
    # Analyze data
    connection = engine.connect()

    # Total sales per item
    query_sales_per_item = """
    SELECT nama_barang, SUM(kuantum) AS total_kuantum
    FROM penjualan_barang
    GROUP BY nama_barang
    ORDER BY total_kuantum DESC;
    """
    sales_per_item = pd.read_sql(query_sales_per_item, con=connection)
    sales_per_item.to_csv('outputs/sales_per_item.csv', index=False)
    save_analysis_to_mysql(engine, sales_per_item, 'sales_per_item')

    # Monthly trends
    query_monthly_trends = """
    SELECT DATE_FORMAT(tanggal, '%Y-%m') AS bulan, nama_barang, SUM(kuantum) AS total_kuantum
    FROM penjualan_barang
    GROUP BY bulan, nama_barang
    ORDER BY bulan;
    """
    monthly_trends = pd.read_sql(query_monthly_trends, con=connection)
    monthly_trends.to_csv('outputs/monthly_trends.csv', index=False)
    save_analysis_to_mysql(engine, monthly_trends, 'monthly_trends')

    # Profit margin analysis
    query_margin = """
    SELECT pb.nama_barang, 
           SUM(pj.nominal) / SUM(pj.kuantum) - SUM(pb.kuantum) / COUNT(pb.id) AS avg_margin
    FROM pemasukan_barang pb
    JOIN penjualan_barang pj ON pb.nama_barang = pj.nama_barang
    GROUP BY pb.nama_barang;
    """
    margin_analysis = pd.read_sql(query_margin, con=connection)
    margin_analysis.to_csv('outputs/margin_analysis.csv', index=False)
    save_analysis_to_mysql(engine, margin_analysis, 'margin_analysis')

    # Top buyer by nominal
    query_top_buyer = """
    SELECT nama_pembeli, SUM(nominal) AS total_nominal
    FROM penjualan_barang
    GROUP BY nama_pembeli
    ORDER BY total_nominal DESC;
    """
    top_buyer = pd.read_sql(query_top_buyer, con=connection)
    top_buyer.to_csv('outputs/top_buyer.csv', index=False)
    save_analysis_to_mysql(engine, top_buyer, 'top_buyer')

    # Comparison of incoming and outgoing stock
    query_stock_comparison = """
    SELECT pb.nama_barang, 
           SUM(pb.kuantum) AS total_pemasukan, 
           SUM(pj.kuantum) AS total_penjualan
    FROM pemasukan_barang pb
    LEFT JOIN penjualan_barang pj ON pb.nama_barang = pj.nama_barang
    GROUP BY pb.nama_barang;
    """
    stock_comparison = pd.read_sql(query_stock_comparison, con=connection)
    stock_comparison.to_csv('outputs/stock_comparison.csv', index=False)
    save_analysis_to_mysql(engine, stock_comparison, 'stock_comparison')


    # Monthly incoming trends
    query_monthly_incoming = """
    SELECT DATE_FORMAT(tanggal, '%Y-%m') AS bulan, nama_barang, SUM(kuantum) AS total_pemasukan
    FROM pemasukan_barang
    GROUP BY bulan, nama_barang;
    """
    monthly_incoming = pd.read_sql(query_monthly_incoming, con=connection)
    monthly_incoming.to_csv('outputs/monthly_incoming.csv', index=False)
    save_analysis_to_mysql(engine, monthly_incoming, 'monthly_incoming')


    # Top frequent buyers
    query_frequent_buyers = """
    SELECT nama_pembeli, COUNT(*) AS jumlah_transaksi
    FROM penjualan_barang
    GROUP BY nama_pembeli
    ORDER BY jumlah_transaksi DESC;
    """
    frequent_buyers = pd.read_sql(query_frequent_buyers, con=connection)
    frequent_buyers.to_csv('outputs/frequent_buyers.csv', index=False)
    save_analysis_to_mysql(engine, frequent_buyers, 'frequent_buyers')

    connection.close()
    print("Analysis results saved to outputs folder.")



if __name__ == '__main__':
    db_user = 'root'
    db_password = ''
    db_host = 'localhost'
    db_name = 'transaksi_db'

    engine = create_engine(f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}')
    run_analysis(engine)
