from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def omlet(request):
    servings = int(request.GET.get('servings', '1'))
    recipe = {}
    context = {}
    for k, v in DATA.get('omlet').items():
        recipe[k] = v * servings
    context['recipe'] = recipe
    print(context)
    return render(request, 'calculator/index.html', context)


def pasta(request):
    servings = int(request.GET.get('servings', '1'))
    recipe = {}
    context = {}
    for k, v in DATA.get('pasta').items():
        recipe[k] = v * servings
    context['recipe'] = recipe
    print(context)
    return render(request, 'calculator/index.html', context)


def buter(request):
    servings = int(request.GET.get('servings', '1'))
    recipe = {}
    context = {}
    for k, v in DATA.get('buter').items():
        recipe[k] = v * servings
    context['recipe'] = recipe
    print(context)
    return render(request, 'calculator/index.html', context)
