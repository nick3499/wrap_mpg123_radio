#!/usr/bin/env python3

from csv import reader
from subprocess import run


def wrap():
    '''List numbered Internet radio stations. Then enter a number which \
corresponds with a station. The `mpg123` module plays stations in the MP3 \
format.'''
    url_dict = {}  # key/value - station descrip/URL

    print(f'========== Station List (choose one) ==========')

    with open('stations_urls.csv', mode='r') as file_obj:
        reader_obj = reader(file_obj)  # reader obj iterates over CSV records
        for i, row in enumerate(reader_obj, start=1):
            print(f'{i:2} | {row[0]}')  # print Internet radio station list
            url_dict[i] = row[1]  # append keys/values to dict

    station_number = int(input('Enter number: '))  # enter station num

    run(['mpg123', url_dict[station_number]])  # pass args to CLI


if __name__ == '__main__':
    wrap()
