from django.shortcuts import render
from django.http import HttpResponse
from MainApp.models import Item

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
    context = {
        "name": "Евгений"
    }
    return render(request, "index.html", context)


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
            context = {
                "item": item
            }
            return render(request, "item_page.html", context)

    return HttpResponse(f"Товар с id={id} не найден")


def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)