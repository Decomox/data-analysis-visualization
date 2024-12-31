import pandas as pd
from sqlalchemy import create_engine, text

def load_data():
    pemasukan_file = 'data/pemasukan_barang.csv'
    penjualan_file = 'data/penjualan_barang.csv'

    pemasukan_df = pd.read_csv(pemasukan_file)
    penjualan_df = pd.read_csv(penjualan_file)

    return pemasukan_df, penjualan_df

def create_and_load_tables(engine, pemasukan_df, penjualan_df):
    # Drop existing tables if they exist
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS pemasukan_barang;"))
        connection.execute(text("DROP TABLE IF EXISTS penjualan_barang;"))

    # Add 'id' column for pemasukan_df
    pemasukan_df['id'] = range(1, len(pemasukan_df) + 1)

    # Rename columns to match SQL queries
    pemasukan_df.rename(columns={"nama.barang": "nama_barang"}, inplace=True)
    penjualan_df.rename(columns={"nama.pembeli": "nama_pembeli", "nama.barang": "nama_barang"}, inplace=True)

    # Create tables and insert data
    pemasukan_df.to_sql('pemasukan_barang', con=engine, if_exists='replace', index=False)
    penjualan_df.to_sql('penjualan_barang', con=engine, if_exists='replace', index=False)
    print("Data successfully loaded into MySQL")

def main():
    # Database connection
    db_user = 'root'
    db_password = ''
    db_host = 'localhost'
    db_name = 'transaksi_db'

    engine = create_engine(f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}')

    # Load datasets
    pemasukan_df, penjualan_df = load_data()

    # Create and load tables
    create_and_load_tables(engine, pemasukan_df, penjualan_df)

if __name__ == '__main__':
    main()
