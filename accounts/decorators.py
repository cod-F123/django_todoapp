from django.shortcuts import redirect

def anonamous_required(func):
    
    def inner(request):
        if request.user.is_authenticated:
            return redirect('todo:index')
        
        return func(request)
    
    return inner