import pandas as pd

from kamernet import web_scrape
import pandas as pd

if __name__ == '__main__':
    print('Welcome to real estate aggregator')
    options = {'1': 'Update data', '2': 'Present data','3': 'Exit'}
    options_restrict = {'1': 'Price range', '2': 'Type', '3': 'Surface range', '4': 'Furnished', '5': 'Availability', '6': 'Exit'}
    while True:
        print(options)
        user_input = input('Choose action: ')
        if user_input == '1':
            file_name = input('Input filepath: ')
            web_scrape(file_name)
        if user_input == '2':
            file_name = input('Input filepath: ')
            df = pd.read_csv(file_name)
            pd.options.display.max_columns = 10
            pd.options.display.max_rows = 27
            pd.options.display.max_colwidth = 100
            print(df)
            restrict = input('Would you like to restrict search (Y/N): ')
            if restrict == 'Y':
                while True:
                    print(options_restrict)
                    option = input('Choose option: ')
                    if option == '1':
                        upper = int(input('Enter upper-bound'))
                        lower = int(input('Enter lower-bound'))
                        print(df[(df['Price'] > lower) & (df['Price'] < upper)])
                    if option == '2':
                    if option == '3':
                    if option == '4':
                    if option == '5':
                    if option == '6':
                        break

        if user_input == '3':
            break

