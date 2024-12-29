def categories(request):
    categories = [
    'Programming',
    'Food',
    'Travel',
    ]
    return {'username':'sorin',
            'categories': categories }