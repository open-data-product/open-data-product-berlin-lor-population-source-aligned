import os

import pandas as pd

from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def convert_data_to_csv(source_path, results_path, clean=False, quiet=False):
    # Iterate over files
    for subdir, dirs, files in sorted(os.walk(source_path)):
        # Make results path
        subdir = subdir.replace(f"{source_path}/", "")
        os.makedirs(os.path.join(results_path, subdir), exist_ok=True)

        for file_name in sorted(files):
            source_file_path = os.path.join(source_path, subdir, file_name)
            convert_file_to_csv(source_file_path, clean=clean, quiet=quiet)


def convert_file_to_csv(source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}.csv"

    # Check if result needs to be generated
    if clean or not os.path.exists(file_path_csv):
        # Determine engine
        if (
            source_file_extension == ".xlsx"
            and "SB_A01-16-00_2020h01_BE" not in source_file_name
        ):
            engine = "openpyxl"
        elif source_file_extension == ".xls":
            engine = None
        else:
            return

        # Set default values
        drop_columns = []

        try:
            dataframes = []

            sheets = (
                ["T1a", "T2a", "T3a", "T4a"]
                if "berlin-lor-population-2020-02" in source_file_name
                else ["T1", "T2", "T3", "T4"]
            )

            # Iterate over sheets
            for sheet in sheets:
                if "T1" in sheet or "T1a" in sheet:
                    skiprows = 7
                    names = [
                        "district",
                        "forecast_area",
                        "district_region",
                        "planning_area",
                        "inhabitants",
                        "inhabitants_percentage",
                        "inhabitants_with_migration_background",
                        "inhabitants_with_migration_background_percentage",
                        "inhabitants_germans",
                        "inhabitants_germans_percentage",
                        "inhabitants_germans_without_migration_background",
                        "inhabitants_germans_without_migration_background_percentage",
                        "inhabitants_germans_with_migration_background",
                        "inhabitants_germans_with_migration_background_percentage",
                        "inhabitants_foreigners",
                        "inhabitants_foreigners_percentage",
                    ]
                    drop_columns = [
                        "inhabitants_percentage",
                        "inhabitants_with_migration_background_percentage",
                        "inhabitants_germans_percentage",
                        "inhabitants_germans_without_migration_background_percentage",
                        "inhabitants_germans_with_migration_background_percentage",
                        "inhabitants_foreigners_percentage",
                    ]
                elif "T2" in sheet or "T2a" in sheet:
                    skiprows = 4
                    names = [
                        "district",
                        "forecast_area",
                        "district_region",
                        "planning_area",
                        "inhabitants",
                        "inhabitants_age_below_6",
                        "inhabitants_age_6_15",
                        "inhabitants_age_15_18",
                        "inhabitants_age_18_27",
                        "inhabitants_age_27_45",
                        "inhabitants_age_45_55",
                        "inhabitants_age_55_65",
                        "inhabitants_age_above_65",
                        "inhabitants_female",
                        "inhabitants_foreigners",
                    ]
                elif "T3" in sheet or "T3a" in sheet:
                    skiprows = 4
                    names = [
                        "district",
                        "forecast_area",
                        "district_region",
                        "planning_area",
                        "inhabitants",
                        "inhabitants_with_migration_background_age_below_6",
                        "inhabitants_with_migration_background_age_6_15",
                        "inhabitants_with_migration_background_age_15_18",
                        "inhabitants_with_migration_background_age_18_27",
                        "inhabitants_with_migration_background_age_27_45",
                        "inhabitants_with_migration_background_age_45_55",
                        "inhabitants_with_migration_background_age_55_65",
                        "inhabitants_with_migration_background_age_above_65",
                        "inhabitants_with_migration_background_female",
                        "inhabitants_foreigners",
                    ]
                elif "T4" in sheet or "T4a" in sheet:
                    skiprows = 6
                    names = [
                        "district",
                        "forecast_area",
                        "district_region",
                        "planning_area",
                        "inhabitants",
                        "inhabitants_from_european_union",
                        "inhabitants_from_france",
                        "inhabitants_from_greece",
                        "inhabitants_from_italy",
                        "inhabitants_from_austria",
                        "inhabitants_from_spain",
                        "inhabitants_from_poland",
                        "inhabitants_from_bulgaria",
                        "inhabitants_from_rumania",
                        "inhabitants_from_croatia",
                        "inhabitants_from_united_kingdom",
                        "inhabitants_from_former_yugoslavia",
                        "inhabitants_from_bosnia_herzegovina",
                        "inhabitants_from_serbia",
                        "inhabitants_from_former_soviet_union",
                        "inhabitants_from_russia",
                        "inhabitants_from_ukraine",
                        "inhabitants_from_kazakhstan",
                        "inhabitants_from_islamic_countries",
                        "inhabitants_from_turkey",
                        "inhabitants_from_iran",
                        "inhabitants_from_arabic_countries",
                        "inhabitants_from_lebanon",
                        "inhabitants_from_syria",
                        "inhabitants_from_vietnam",
                        "inhabitants_from_united_states",
                        "inhabitants_from_undefined",
                    ]
                else:
                    skiprows = 0
                    names = []

                dataframes.append(
                    pd.read_excel(
                        source_file_path,
                        engine=engine,
                        sheet_name=sheet,
                        skiprows=skiprows,
                        usecols=list(range(0, len(names))),
                        names=names,
                    )
                    .drop(columns=drop_columns, errors="ignore")
                    .dropna()
                    .astype(int)
                    .assign(
                        id=lambda df: df[
                            [
                                "district",
                                "forecast_area",
                                "district_region",
                                "planning_area",
                            ]
                        ].apply(
                            lambda row: "".join(
                                map(
                                    str,
                                    pd.to_numeric(row, errors="coerce")
                                    .fillna(-1)
                                    .astype(int)
                                    .apply(lambda x: str(x).zfill(2)),
                                )
                            ),
                            axis=1,
                        )
                    )
                    .drop(
                        columns=[
                            "district",
                            "forecast_area",
                            "district_region",
                            "planning_area",
                        ],
                        errors="ignore",
                    )
                )

            # Concatenate data frames
            dataframe = (
                pd.concat([df.set_index("id") for df in dataframes], axis=1)
                .reset_index()
                .dropna()
            )

            # Write csv file
            if dataframe.shape[0] > 0:
                dataframe.to_csv(file_path_csv, index=False)
                if not quiet:
                    print(f"✓ Convert {os.path.basename(file_path_csv)}")
            else:
                if not quiet:
                    print(dataframe.head())
                    print(f"✗️ Empty {os.path.basename(file_path_csv)}")
        except Exception as e:
            print(f"✗️ Exception: {str(e)}")
    elif not quiet:
        print(f"✓ Already exists {os.path.basename(file_path_csv)}")
