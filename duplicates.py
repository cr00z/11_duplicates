import os
from collections import defaultdict


def get_file_candidates(start_path):
    dup_candidates = defaultdict(lambda: defaultdict(list))
    for directory, _, filenames in os.walk(start_path):
        for filename in filenames:
            filepath = os.path.join(directory, filename)
            if os.path.exists(filepath):
                filesize = os.path.getsize(filepath)
                dup_candidates[filename.lower()][filesize].append(filepath)
    return dup_candidates


def find_duplicates(start_path):
    dup_candidates = get_file_candidates(start_path)
    dup_report = ''
    for filename, filesizes in dict(dup_candidates).items():
        for filesize, filepaths in dict(filesizes).items():
            if len(filepaths) > 1:
                dup_output = [filename, filesize, '\n'.join(filepaths)]
                dup_report += '\n{d[0]} ({d[1]})\n\n{d[2]}\n'.format(d=dup_output)
    return dup_report


if __name__ == '__main__':
    start_path = input("Input start path to find duplicates: ")
    dup_report = find_duplicates(start_path)
    if dup_report == '':
        print("No matches")
    else:
        print(dup_report)
