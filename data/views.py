from .table import User, session
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')    
        password = data.get('password')
        print(email,password)
        try:
            new_login = User(email=email, password=password)
            session.add(new_login)
            session.commit()
            return JsonResponse({'status': 'success', 'message': 'Login details stored successfully'})
        except Exception as e:
            print(str(e))
        finally:
            session.close()
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
  