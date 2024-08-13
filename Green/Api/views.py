import json
from django.http import HttpResponse
import requests
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')




def get_settings(request):
    response_data = None
    if request.method == 'POST':
        id_instance = request.POST.get('idInstance')
        api_token_instance = request.POST.get('apiTokenInstance')
        apiUrl = f'https://{id_instance[:4]}.api.greenapi.com'
        url = f"{apiUrl}/waInstance{id_instance}/getSettings/{api_token_instance}"
        request.session['idInstance'] = id_instance
        request.session['apiTokenInstance'] = api_token_instance
        try:
            # Отправляем GET-запрос на API
            response = requests.get(url)

            # Проверяем статус ответа и обрабатываем данные
            if response.status_code == 200:
                response_data = response.json()
            else:
                response_data = {
                    'error': f"Ошибка при получении данных: {response.status_code}"
                }
        except requests.exceptions.RequestException as e:
            # Обрабатываем исключения при запросе
            response_data = {
                'error': f"Произошла ошибка при попытке связаться с API: {str(e)}"
            }

    return render(request, 'index.html', {'response': response_data})



def get_state(request):
    response_data = None
    if request.method == 'POST':
        id_instance = request.session.get('idInstance')
        api_token_instance = request.session.get('apiTokenInstance')
        apiUrl = f'https://{id_instance[:4]}.api.greenapi.com'
        url = f"{apiUrl}/waInstance{id_instance}/getStateInstance/{api_token_instance}"
        try:
            # Отправляем GET-запрос на API
            response = requests.get(url)

            # Проверяем статус ответа и обрабатываем данные
            if response.status_code == 200:
                response_data = response.json()
            else:
                response_data = {
                    'error': f"Ошибка при получении данных: {response.status_code}"
                }
        except requests.exceptions.RequestException as e:
            # Обрабатываем исключения при запросе
            response_data = {
                'error': f"Произошла ошибка при попытке связаться с API: {str(e)}"
            }

    return render(request, 'index.html', {'response': response_data})


def send_message(request):
    if request.method == 'POST':
        id_instance = request.session.get('idInstance')
        api_token_instance = request.session.get('apiTokenInstance')
        apiUrl = f'https://{id_instance[:4]}.api.greenapi.com'
        url = f"{apiUrl}/waInstance{id_instance}/sendMessage/{api_token_instance}"
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        headers = {
                    'Content-Type': 'application/json'
                }
        payload = {
            "chatId": f"{phone_number}@c.us",
            "message": message
        }

        payload_json = json.dumps(payload)

        try:
            # Отправляем POST-запрос к API
            response = requests.request("POST", url, headers=headers, data=payload_json)
            
            # Обрабатываем ответ от API
            if response.status_code == 200:
                response_data = response.json()
                return HttpResponse(f"Сообщение успешно отправлено! Ответ сервера: {response_data}")
            else:
                return HttpResponse(f"Ошибка при отправке сообщения: {response.status_code} {response.text}")
        except requests.exceptions.RequestException as e:
            return HttpResponse(f"Произошла ошибка при выполнении запроса: {str(e)}")
    else:
        return render(request, 'index.html', {'response': response_data})
    



def send_file(request):
    if request.method == 'POST':
        id_instance = request.session.get('idInstance')
        api_token_instance = request.session.get('apiTokenInstance')
        apiUrl = f'https://{id_instance[:4]}.api.greenapi.com'
        url = f"{apiUrl}/waInstance{id_instance}/sendFileByUrl/{api_token_instance}"
        phone_number = request.POST.get('phone_number')
        url_file = request.POST.get('file')
        file_name = request.POST.get('file_name')
        headers = {
                    'Content-Type': 'application/json'
                }
        payload = {
            "chatId": f"{phone_number}@c.us",
            "urlFile": url_file,
            "fileName": file_name
        }

        payload_json = json.dumps(payload)

        try:
            # Отправляем POST-запрос к API
            response = requests.request("POST", url, headers=headers, data=payload_json)
            
            # Обрабатываем ответ от API
            if response.status_code == 200:
                response_data = response.json()
                return HttpResponse(f"Сообщение успешно отправлено! Ответ сервера: {response_data}")
            else:
                return HttpResponse(f"Ошибка при отправке сообщения: {response.status_code} {response.text}")
        except requests.exceptions.RequestException as e:
            return HttpResponse(f"Произошла ошибка при выполнении запроса: {str(e)}")
    else:
        return render(request, 'index.html', {'response': response_data})