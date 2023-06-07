import csv
import requests

file_path = "./redirects.csv"
http_path = "https://docs.phala.network/v1/~/revisions/VqKGTgEXu3pvfGP8iACH/"


def test_redirects():
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            source, expected_dest = row
            source = http_path + source
            expected_dest = http_path + expected_dest
            try:
                response = requests.get(source, allow_redirects=True)
            except requests.exceptions.RequestException as e:
                print(f"Error sending request to {source}: {e}")
                continue

            # Check status code
            if response.status_code != 200:
                print(f"Non-200 status code {response.status_code} for URL {source}")
                continue

            # Check redirected URL
            actual_dest = response.url
            if actual_dest != expected_dest:
                print(f"URL {source} redirects to {actual_dest}, expected {expected_dest}")
