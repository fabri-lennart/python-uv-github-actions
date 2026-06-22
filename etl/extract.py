import httpx
import json

def fetch_data():
    print("Starting data download...")
    url = "https://jsonplaceholder.typicode.com/users"

    with httpx.Client() as client:
        response = client.get(url)

        if response.status_code == 200:
            user = response.json()
            with open("data/user_data.json", "w", encoding="utf-8") as json_file:
                json.dump(user, json_file, indent=4)
        else:
            print(f"Error fetching API: {response.status_code}")
            exit(1)

run_extract_process = fetch_data()
