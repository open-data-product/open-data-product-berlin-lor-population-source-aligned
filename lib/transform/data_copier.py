import os
import shutil

from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def copy_data(source_path, results_path, clean=False, quiet=False):
    # Iterate over files
    for subdir, dirs, files in sorted(os.walk(source_path)):
        # Make results path
        subdir = subdir.replace(f"{source_path}/", "")
        os.makedirs(os.path.join(results_path, subdir), exist_ok=True)

        for source_file_name in sorted(files):
            results_file_name = get_results_file_name(source_file_name)

            source_file_path = os.path.join(source_path, subdir, source_file_name)
            results_file_path = os.path.join(results_path, subdir, results_file_name)

            # Check if file needs to be copied
            if clean or not os.path.exists(results_file_path):
                shutil.copyfile(source_file_path, results_file_path)

                if not quiet:
                    print(f"✓ Copy {results_file_name}")
            else:
                print(f"✓ Already exists {results_file_name}")


def get_results_file_name(source_file_name):
    if source_file_name == "SB_A01-06-00_2015h01_BE.xlsx":
        return "berlin-lor-population-2015-01.xlsx"
    elif source_file_name == "SB_A01-06-00_2015h02_BE.xlsx":
        return "berlin-lor-population-2015-02.xlsx"
    elif source_file_name == "SB_A01-16-00_2016h01_BE.xlsx":
        return "berlin-lor-population-2016-01.xlsx"
    elif source_file_name == "SB_A01-16-00_2016h02_BE.xlsx":
        return "berlin-lor-population-2016-02.xlsx"
    elif source_file_name == "SB_A01-16-00_2017h01_BE.xlsx":
        return "berlin-lor-population-2017-01.xlsx"
    elif source_file_name == "SB_A01-16-00_2017h02_BE.xlsx":
        return "berlin-lor-population-2017-02.xlsx"
    elif source_file_name == "SB_A01-16-00_2018h01_BE.xlsx":
        return "berlin-lor-population-2018-01.xlsx"
    elif source_file_name == "SB_A01-16-00_2018h02_BE.xlsx":
        return "berlin-lor-population-2018-02.xlsx"
    elif source_file_name == "SB_A01-16-00_2019h01_BE.xlsx":
        return "berlin-lor-population-2019-01.xlsx"
    elif source_file_name == "SB_A01-16-00_2019h02_BE.xlsx":
        return "berlin-lor-population-2019-02.xlsx"
    elif source_file_name == "SB_A01-16-00_2020h01_BE.xlsx":
        return "berlin-lor-population-2020-01.xlsx"
    elif source_file_name == "SB_A01-16-00_2020h02_BE.xlsx":
        return "berlin-lor-population-2020-02.xlsx"
    elif source_file_name == "SB_A01-16-00_2021h01_BE.xlsx":
        return "berlin-lor-population-2021-01.xlsx"
    elif source_file_name == "SB_A01-16-00_2021h02_BE.xlsx":
        return "berlin-lor-population-2021-02.xlsx"
    elif source_file_name == "SB_A01-16-00_2022h01_BE.xlsx":
        return "berlin-lor-population-2022-01.xlsx"
    elif source_file_name == "SB_A01-16-00_2022h02_BE.xlsx":
        return "berlin-lor-population-2022-02.xlsx"
    elif source_file_name == "SB_A01-16-00_2023h01_BE.xlsx":
        return "berlin-lor-population-2023-01.xlsx"
    else:
        return source_file_name
