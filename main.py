import httpx

def fetch_data():
    print("Starting data download...")
    url = "https://jsonplaceholder.typicode.com/users/1"

    with httpx.Client() as client:
        response = client.get(url)

        if response.status_code == 200:
            user = response.json()
            print("Data successfully retrieved:")
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Company: {user['company']['name']}")
        else:
            print(f"Error fetching API: {response.status_code}")
            exit(1)

if __name__ == "__main__":
    fetch_data()
