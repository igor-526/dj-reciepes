from django.shortcuts import render

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
}

def view_all(request):
    context = {'items': list(DATA)}
    return render(request, "calculator/main.html", context)

def view_one(request, name):
    context = {'recipe': DATA.get(name)}
    servings = request.GET.get("servings")
    if servings:
        for item in context['recipe']:
            context['recipe'][item] = context['recipe'][item] * int(servings)

    return render(request, "calculator/index.html", context)
