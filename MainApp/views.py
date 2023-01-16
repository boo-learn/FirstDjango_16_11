from django.shortcuts import render
from django.http import HttpResponse

user_info = {
    "name": "Евгений"
}

# Create your views here.
def home(request):
    result = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Юрченко Е.В.</i>
    """
    return HttpResponse(result)


def about(request):
    result = f"""
    Имя: <b>{user_info['name']}</b> <br>
    Отчество: Петрович
    Фамилия: Иванов
    телефон: 8-923-600-01-02
    email: vasya@mail.ru
    """
    return HttpResponse(result)