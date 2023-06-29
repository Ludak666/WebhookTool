import requests

url = input("Enter the Webhook-URL: ")

headers = {
  'authority': 'discord.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'authorization': 'MTA3MDUwODI4NTY0OTc0Nzk3OA.GLPGLh.Vn3fzauOq4MKYcO7krxg_3QRH0hJTJyXOKkMM4',
  'cookie': '__dcfduid=a0a6ff0014e111eeab874763194a1f3f; __sdcfduid=a0a6ff0114e111eeab874763194a1f3fccd3a80474bc3e96e8f18cfd05e375301cdbae05cad90382c766b523066864fc; locale=en-US; __cfruid=950262489e11d5f9231a744605b673d812deac20-1687992063; _gid=GA1.2.1193136347.1687993959; OptanonAlertBoxClosed=2023-06-28T23:15:57.179Z; _gcl_au=1.1.1860127309.1687994157; _ga=GA1.1.1017035945.1687993959; OptanonConsent=isIABGlobal=false&datestamp=Thu+Jun+29+2023+01%3A32%3A41+GMT%2B0200+(Central+European+Summer+Time)&version=6.33.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false&geolocation=AT%3B9; __cf_bm=Sh9h45PXN4VfUFG2uw3uFbhOwRTC6gyv_oUqRnK1Jxk-1687995162-0-ASO7svT7MKnwNI/b4UulWd6x7poBI8ksyN2JnS4FFQmFlWLOBU1zo11KAt9nOrVTCg==; _ga_Q149DFWHT7=GS1.1.1687994157.1.1.1687995168.0.0.0; __cf_bm=eo0H7iwW4VknZaaYcjOdL2r4cabY8jiALjWeT_dekwI-1687995999-0-AYUrniUzEhL+zMI+NQnxmla4SbhhrW0Ib9LKxwmVA2lrbgRzrguuxMOUxO/E+stecrerHvzji8xd3s/jS9BZqe0=; __cfruid=807b5834c470d819975863d786c59c85b119416e-1687995999',
  'referer': 'https://discord.com/',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58',
  'x-track': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTQuMC4xODIzLjU4IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vd3d3LnlvdXR1YmUuY29tLyIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6Ind3dy55b3V0dWJlLmNvbSIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'
}

def get_data():
    response = requests.get(url, headers=headers)
    print(response.text)

def delete_data():
    response = requests.delete(url, headers=headers)
    print("You have successfully deleted the WebHook")

def main():
    while True:
        choice = input("Enter your choice (GET or DELETE), or Q to quit: ")

        if choice.upper() == 'GET':
            get_data()
        elif choice.upper() == 'DELETE':
            delete_data()
        elif choice.upper() == 'Q':
            break
        else:
            print("Invalid choice. Please try again.")
        print("")

if __name__ == '__main__':
    main()
