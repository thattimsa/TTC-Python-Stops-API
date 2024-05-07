import csv
import requests

url = "https://transit.ttc.com.ge/pis-gateway/api/v2/stops"
params = {
    "locale": "ka"
}

headers = {
    "X-Api-Key": "c0a2f304-551a-4d08-b8df-2c53ecd57f9f",
    "Accept": "application/json"
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    stops = response.json()

    # Define CSV file path
    csv_file = "stops.csv"

    # Define CSV fieldnames
    fieldnames = ['id', 'name', 'code']

    # Write stops data to CSV
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        for stop in stops:
            writer.writerow({
                'id': stop['id'],
                'name': stop['name'],
                'code': stop['code'],
            })
    
    print(f"Stops data exported to {csv_file}")
else:
    print("Failed to fetch stops. Status code:", response.status_code)