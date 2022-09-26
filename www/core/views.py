from django.shortcuts import render

# Create your views here.
def index_view(request):
    template = 'base.html'
    return render(request, template, {})
