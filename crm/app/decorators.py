from django.http import HttpResponseForbidden
from functools import wraps

def role_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.role in roles:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden()
        return wrapper
    return decorator