import requests

def check_phone(phone_number):
    url = 'https://cleaner.dadata.ru/api/v1/clean/phone'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Token fbc670c69a5e6f36f90f18f269b4c722bf9161ab',
        'X-Secret': '8120dba2d3470f64838223d9fc951e87f15eacad'
    }
    data = [phone_number]
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raises exception for bad responses (4xx or 5xx)
        
        json_data = response.json()
        if json_data:
            result = json_data[0]
            region = result.get('region', 'N/A')
            country = result.get('country', 'N/A')
            provider = result.get('provider', 'N/A')
            
            print(f"Регион: {region}")
            print(f"Страна: {country}")
            print(f"Провайдер: {provider}")
        else:
            print("Нет данных для указанного номера")
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")

if __name__ == "__main__":
    phone_number = input("Введите номер телефона (в формате без пробелов и разделителей, например, 79123456789): ")
    check_phone(phone_number)
