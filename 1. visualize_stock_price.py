# Visualise any stock in the world by following these simple methods
# Chosen stock company 'Maruti Suzuki'
# Stock name or stock code is 'MRTI'
# Country -> 'India'

# importing necessary libraries

import investpy
import matplotlib.pyplot as plt

def get_stock_history(symbol='MRTI', stock_country='India', from_date='01/01/2010', to_date='31/12/2020', order='ascending'):
    ''' Collects stock data from_date to start_date and sorts them by order ''' 
    df = investpy.get_stock_historical_data(stock=symbol, country=stock_country,\
                                            from_date=from_date, to_date=to_date, order='ascending')

    return df

def concise_columns(df):
    ''' Shortens the columns as required here we consider date and "Close" points '''
    df = df['Close']
    return df

def visualize(df):
    ''' Visualizes the data in line graph and area plots. '''
    # Line
    df.plot(x=None, y='Close', kind='line')
    plt.ylabel('Price')
    plt.show()

    # Area
    plt.ylabel('Price')
    df.plot(x=None, y='Close', kind='area')
    plt.show()


def visualize_stock():
    ''' Visualize any stock in the world from its past data or history.
    # You can add any other stock. 'Maruti Suzuki' is the default stock here.
    # If you want to visualize other stocks uncomment below lines and edit as per your requirement.
    '''

    # stock_symbol, stock_country = 'MRTI', 'India'
    # from_date, to_date = '01/01/2010', '31/12/2020'
    # df = get_stock_history(stock_symbol, stock_country, \
    #                       from_date=from_date, to_date=to_date, order='ascending')

    df = get_stock_history() # comment this line if edited above lines. 
    df = concise_columns(df)
    visualize(df)


if __name__ == '__main__':
    visualize_stock()