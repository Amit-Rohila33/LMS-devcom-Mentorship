from django.contrib.auth import authenticate
#from django.contrib.auth import get_all_permissions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from authentication.models import Student
from authentication.serializers import StudentSerializer
from django.http import JsonResponse
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_403_FORBIDDEN
)
from rest_framework.response import Response


#Login View
@csrf_exempt
@api_view(["POST", "GET"])
@permission_classes((AllowAny,))
def login(request):
    
    #email = request.data.get("email")
    #password = request.data.get("password")
    print('request>>>>>')
    email = ((request.query_params.get("email")))
    password = ((request.query_params.get("password")))
    if email is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(request, email=email, password=password)
    #print(get_user_permissions(user,obj=None))
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    print(user.email)
    print(user.id)
    print(user.is_superuser)
    user_type = 'USER'
    if user.is_superuser:
        user_type = 'ADMIN'
    token, _ = Token.objects.get_or_create(user=user)
    print('token>>>')
    print(token)
    return Response({'token': token.key,'name':user.name,'email':user.email,'id':user.id,'user_type':user_type},
                    status=HTTP_200_OK)






'''This returns the views for the user, permission_class = DEFAULT_PERMISSION_CLASSES
 Admin can access student data for all the students and Student can GET, PUT, DELETE his/her data.
'''
@api_view(['GET'])
def user_based_access(request):
    if request.user.is_superuser:
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif not request.user.is_superuser:
        email = request.user.email
        student = Student.objects.get(email= email)
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data, safe=False)

'''This view gives details for some student , permission_class = DEFAULT_PERMISSION_CLASSES
Admin can access Student data and DELETE the Student.
Student can only access its data and PUT, DELETE itself.
'''

@api_view(['PUT', 'GET','DELETE'])
def student_details(request, slug):
    try:
        student = Student.objects.get(slug=slug)

    except Student.DoesNotExist:
        return Response(status =HTTP_404_NOT_FOUND, data={'detail':'This Student Does Not Exist'})
    
    if request.method=='GET' and (request.user.is_superuser or request.user == student) :
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    elif request.method=='PUT' and request.user==student:
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=HTTP_400_BAD_REQUEST)
    elif request.method =='PUT' and request.user.is_superuser and request.user!=student:
        return Response(data={'detail':'You are not authorised to alter this data'},status=HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE' and (request.user.is_superuser or request.user == student):
        student.delete()
        return Response(data={'detail':'Student Deleted Successfully'}, status=HTTP_404_NOT_FOUND)
    
    else:
        return Response(status=HTTP_403_FORBIDDEN)
    
    
    

    

