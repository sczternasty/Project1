import pandas as pd

from kamernet import web_scrape
import pandas as pd

if __name__ == '__main__':
    print('Welcome to real estate aggregator')
    options = {'1': 'Update data', '2': 'Present data','3': 'Exit'}
    options_restrict = {'1': 'Price range', '2': 'Type', '3': 'Surface range', '4': 'Furnished', '5': 'Exit'}
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
            restrict = (input('Would you like to restrict search (Y/N): ')).capitalize()
            if restrict == 'Y':
                while True:
                    print(options_restrict)
                    option = input('Choose option: ')
                    if option == '1':
                        p_upper = int(input('Enter upper-bound: '))
                        p_lower = int(input('Enter lower-bound: '))
                        print(df[(df['Price'] > p_lower) & (df['Price'] < p_upper)])
                    if option == '2':
                        choose_type = input('Choose type (room, apartment, studio): ').lower()
                        if choose_type == 'room':
                            print(df[df['Type'] == 'Room'])
                        if choose_type == 'apartment':
                            print(df[df['Type'] == 'Apartment'])
                        if choose_type == 'studio':
                            print(df[df['Type'] == 'Studio'])
                    if option == '3':
                        s_upper = int(input('Enter upper-bound: '))
                        s_lower = int(input('Enter lower-bound: '))
                        print(df[(df['Surface'] > s_lower) & (df['Surface'] < s_upper)])
                    if option == '4':
                        choose_furnished = (input('Furnished (Y/N): ')).capitalize()
                        if choose_furnished == 'Y':
                            print(df[(df['Furnished'] == 'furnished')])
                        if choose_furnished == 'N':
                            print(df[(df['Furnished'] == 'uncarpeted')])
                    if option == '5':
                        break

        if user_input == '3':
            break

