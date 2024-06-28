# paling banyak penyefongnya
# paling banyak lib / modul (katanya)
# dev yg pake piton rada setres
import requests

url = 'https://api.simsimi.vn/v1/simtalk'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

while True:
    input_text = input("you>: ")

    if input_text.lower() in ["exit", "quit", "keluar", "murtad"]:
        print("quit..")
        break

    data = {
        'text': input_text,
        'lc': 'id'
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        response_data = response.json()
        message = response_data.get('message', 'no msg')
        print("bot>: " + message)
    else:
        print(f"error {response.status_code}")
