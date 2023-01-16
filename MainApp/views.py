from django.shortcuts import render
from django.http import HttpResponse

user_info = {
    "name": "Евгений",
    "surname": "Юрченко",
    "email": "eyurchenko@specialist.ru",

}

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
    {"id": 9, "name": "Яблоко", "quantity": 124000},
]


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
    Фамилия: <b>{user_info['surname']}</b> <br>
    email: <b>{user_info['email']}</b> <br>
    """
    return HttpResponse(result)


def item_page(request, id):
    for item in items:
        if item['id'] == id:
            result = f"""
            <h2>Название: {item['name']}</h2>
            <div>Количество: {item['quantity']}</div>
            <a href='/items'>Назад</a>
            """
            return HttpResponse(result)

    return HttpResponse(f"Товар с id={id} не найден")


def items_list(request):
    result = "<h1>Список товаров</h1> <ol>"
    for item in items:
        result += f"<a href='/item/{item['id']}'><li>{item['name']}</li></a>"
    result += "</ol>"

    return HttpResponse(result)