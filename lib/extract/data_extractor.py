import os

import requests
import yaml

from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def extract_data(manifest_path, results_path, clean=False, quiet=False):
    # Make results path
    os.makedirs(os.path.join(results_path), exist_ok=True)

    # Load manifest
    with open(manifest_path, "r") as file:
        manifest = yaml.safe_load(file)

        # Iterate over input ports
        for input_port in manifest["input_ports"]:
            # Make results path
            os.makedirs(os.path.join(results_path, input_port["id"]), exist_ok=True)

            # Iterate over files
            for url in input_port["files"]:
                # Determine file path
                file_name = url.rsplit("/", 1)[-1]
                file_path = os.path.join(results_path, input_port["id"], file_name)

                # Download file
                download_file(
                    file_path=file_path,
                    file_name=file_name,
                    url=url,
                    clean=clean,
                    quiet=quiet,
                )


def download_file(file_path, file_name, url, clean, quiet):
    # Check if result needs to be generated
    if clean or not os.path.exists(file_path):
        try:
            data = requests.get(url)
            if str(data.status_code).startswith("2"):
                with open(file_path, "wb") as file:
                    file.write(data.content)
                if not quiet:
                    print(f"✓ Download {file_name}")
            elif not quiet:
                print(f"✗️ Error: {str(data.status_code)}, url {url}")
        except Exception as e:
            print(f"✗️ Exception: {str(e)}, url {url}")
            return None

    elif not quiet:
        print(f"✓ Already exists {file_name}")
