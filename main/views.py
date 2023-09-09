from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Abbilhaidar Farras Zulfikar',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
