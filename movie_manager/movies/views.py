from django.shortcuts import render

# Create your views here.

def create(request):
    if request.POST:
        print(request.POST)
    return render(request, 'create.html')


def list(request):
    movie_data = {
        'movies': [
            {
                'title': 'God father',
                'year': '1999',
                'author': 'padmarajan',
                'success': True
            },
            {
                'title': 'goldfish',
                'year': '1990',
                'author': 'unknown',
                'success': True
            },
            {
                'title': 'great father',
                'year': '1999',
                'author': 'padmarajan',
                'success': True
            },
            {
                'title': 'bha ba bha',
                'year': '1999',
                'author': 'padmarajan',
                'success': True
            }
        ]
    }

    return render(request, 'list.html', movie_data)


def edit(request):
    return render(request, 'edit.html')


