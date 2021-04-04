from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def hello_world(request):
    # 왜 바로 안 읽어지냐면 , root app 의 setting.py 에서 추가해줘야한다
    return render(request, 'base.html')