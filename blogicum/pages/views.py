from django.shortcuts import render


# Create your views here.
def about(request):
    context = {
        'about': about
    }
    return render(request, 'pages/about.html', context)


def rules(request):
    context = {
        'rules': rules
    }    
    return render(request, 'pages/rules.html', context)
