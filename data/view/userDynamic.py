from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..model.userQueryDynamic import userRegisterInsertDynamic  # Adjust the import path

from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

@csrf_exempt
def userDynamicInsert(request):
    if request.method == 'POST': 
        try:
            firstName = request.POST.get('firstName')
            lastName = request.POST.get('lastName')
            mobileNumber = request.POST.get('mobileNumber')
            email = request.POST.get('email')
            userSportsInterest = request.POST.get('userSportsInterest')
            token = request.POST.get('token')
                
            print(" 1 ---------------------------------")
            
            if 'profilePhoto' in request.FILES:
                print("<<<<<<<<<<>>>>>>>>>>>>>>>>")
                profilePhoto = request.FILES['profilePhoto']
                print(profilePhoto, "------------()")
                fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'profilePhotos'))
                filename = fs.save(profilePhoto.name, profilePhoto)
                file_url = fs.url(filename)
                print("--------------",file_url,"------------------------><")
            else:
                file_url=None


            response = userRegisterInsertDynamic(firstName,lastName, mobileNumber, email, profilePhoto, userSportsInterest)
            
            
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)
