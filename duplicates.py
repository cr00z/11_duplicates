import os
from collections import defaultdict
# from colorama import Fore, Style  # Валл Ли сломался


def get_file_candidates(start_path):
    dup_candidates = defaultdict(lambda: defaultdict(list))
    for directory, _, filenames in os.walk(start_path):
        for filename in filenames:
            filepath = os.path.join(directory, filename)
            if os.path.exists(filepath):
                filesize = os.path.getsize(filepath)
                dup_candidates[filename.lower()][filesize].append(filepath)
    return dup_candidates


def find_and_out_duplicates(dup_candidates):
    dup_report = ''
    green_print_bgn = ''    # f'{Fore.GREEN}'
    green_print_end = ''    # f'{Style.RESET_ALL}'
    for filename, filesizes in dict(dup_candidates).items():
        for filesize, filepaths in dict(filesizes).items():
            if len(filepaths) > 1:
                filepaths = '\n'.join(filepaths)
                dup_report += '\n{}{}{} ({})\n\n{}\n'.\
                    format(green_print_bgn, filename, green_print_end, filesize,
                           filepaths)
    return dup_report


if __name__ == '__main__':
    start_path = input("Input start path to find duplicates: ")
    dup_candidates = get_file_candidates(start_path)
    dup_report = find_and_out_duplicates(dup_candidates)
    if dup_report == '':
        print("No matches")
    else:
        print(dup_report)
