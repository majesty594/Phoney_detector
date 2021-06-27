from django.shortcuts import render
from .forms import get_data
from .predict import article_predict
# Create your views here.

def homepage(request):
    global result
    result = None
    form = get_data
    if request.method == 'POST':
        data = request.POST
        url = data['search']
        result = article_predict(str(url))
    return render(request, 'index.html', {'form':form, 'result':result})