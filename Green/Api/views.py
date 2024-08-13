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
        print('bomj')
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



    
