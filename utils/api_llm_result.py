import requests

def fetch_result(requestID, userID, task_id):
    # Define the URL for the request
    url = 'http://ec2-54-251-99-208.ap-southeast-1.compute.amazonaws.com:8010/result'

    # Define the headers as per the curl command
    headers = {
        'x-marketplace-token': '1df239ef34d92aa8190b8086e89196ce41ce364190262ba71964e9f84112bc45',
        'x-request-id': requestID,
        'x-user-id': userID,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # Define the payload with the taskId
    payload = {
        "taskId": task_id
    }

    # Send the POST request
    try:
        response = requests.post(url, json=payload, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Request successful.")
            # Print the response text
            print(response.json())
            return response.json()
        else:
            print(f"Request failed with status code {response.status_code}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage of the function
# task_id = "7cd5d3a1-dc7c-4f7b-aff3-e7d40d22804d"
# fetch_result("abc123", "abc123", task_id)
