'''
Retrieve User Credentials:
●	Use HTTP GET request to fetch user credentials from the endpoint: [GET] https://api.escuelajs.co/api/v1/users.
●	Save the email and password data from the response.

Validate Response Status Code:
●	Check the status code of the HTTP response.
●	Validate that the status code is as expected.

'''
import requests


def test_and_dump():
    URL = 'https://api.escuelajs.co/api/v1/users'
    EXPECTED_STATUS_CODE = 200
    FILE_TO_SAVE_DUMPED_DATA = './dumped.txt'

    response = requests.get(URL)

    if response.status_code == EXPECTED_STATUS_CODE:
        print("[+] fetched successfully")
        
    assert response.status_code == EXPECTED_STATUS_CODE, f'Failed to retrieve data. Status code: {response.status_code}'


    response_data = response.json()
    dumped_data = []

    for item in response_data:
        details = f'{item["email"]}:{item["password"]}'
        dumped_data.append(details)
        print(f'{details}')

    with open(FILE_TO_SAVE_DUMPED_DATA, 'w') as file:
        for line in dumped_data:
            file.write(line + '\n')


if __name__ == "__main__":
    test_and_dump()