import os
from argparse import ArgumentParser

def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument("-i", "--input", help="Specify a CSV file describing the title and the number of discs per season")
    arg_parser.add_argument("-o", "--output", help="Output directory where the title folder should be saved")
    args = arg_parser.parse_args()

    input_file_path = args.input
    output_directory_path = args.output

    assert input_file_path is not None and output_directory_path is not None

    show_title, season_disc_counts = parse_input_file(input_file_path)
    create_directories(show_title, season_disc_counts, output_directory_path)

def parse_input_file(input_file_path):
    with open(input_file_path, 'r') as csv_file:
        csv_values = csv_file.readline().split(',')
        show_title = csv_values.pop(0)

        counter = 1
        season_disc_counts = dict()
        for disc_count in csv_values:
            season_disc_counts[f'Season {counter:02}'] = int(disc_count)
            counter += 1

    return (show_title, season_disc_counts)

def create_directories(show_title, season_disc_counts, output_directory_path):
    show_directory_path = os.path.join(output_directory_path, show_title)
    if not os.path.exists(show_directory_path):
        os.makedirs(show_directory_path)
        print(f'Created Show Directroy: {show_directory_path}')
    else:
        print(f'Disc Directroy Exists: {show_directory_path}')
    
    for season, disc_count in season_disc_counts.items():
        season_directory_path = os.path.join(show_directory_path, season)
        if not os.path.exists(season_directory_path):
            os.makedirs(season_directory_path)
            print(f'\tCreated Season Directroy: {season_directory_path}')
        else:
            print(f'\tDisc Directroy Exists: {season_directory_path}')

        for i in range(disc_count):
            disc_directory_path = os.path.join(season_directory_path, f'Disc {i+1:02}')
            if not os.path.exists(disc_directory_path):
                os.makedirs(disc_directory_path)
                print(f'\t\tCreated Disc Directroy: {disc_directory_path}')
            else:
                print(f'\t\tDisc Directroy Exists: {disc_directory_path}')



if __name__ == '__main__':
    main()