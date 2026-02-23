from django.shortcuts import redirect
from django.http import JsonResponse

def anonamous_required(func):
    
    def inner(request):
        if request.user.is_authenticated:
            return redirect('todo:index')
        
        return func(request)
    
    return inner

def login_required_json(func):
    
    def inner(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'status':'error', 'message':'Authentication requied !'}, status=403)
    
        return func(request,*args,**kwargs)
    
    return inner
