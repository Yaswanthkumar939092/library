import requests
def name_access():
    base_url = 'http://127.0.0.1:8008'
    url = f'{base_url}/api/method/frappe.auth.get_logged_user'
    headers = {
        'Authorization': 'token dedd001f11acaac:e4ba93f7fd16a6a'
    }

    response = requests.get(url, headers=headers)
    print(response)
    data = response.json()

    print(data)
