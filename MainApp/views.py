from django.shortcuts import render
from django.http import HttpResponse
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound

user_info = {
    "name": "Евгений",
    "surname": "Юрченко",
    "email": "eyurchenko@specialist.ru",

}


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
    try:
        item = Item.objects.get(pk=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Товар с id={id} не найден")
    context = {
        "item": item
    }
    return render(request, "item_page.html", context)


def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)
