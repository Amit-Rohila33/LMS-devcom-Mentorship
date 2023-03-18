from rest_framework import serializers
from .models import Student
from rest_framework import serializers
from .models import Student
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class StudentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Student.objects.all())]
            )
    class Meta:
        model = Student
        fields = ('id','email', 'name', 'slug','image', 'user_type')
        extra_kwargs = {
            'name': {'required': True},
            'image':{'required': False, 'allow_null' :True},
            'slug':{'required': False, 'allow_null' :True}
            
        }



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Student.objects.all())]
            )
    image = serializers.ImageField(required = False, allow_null = True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    slug = serializers.SlugField(read_only=True, required=False)

    class Meta:
        model = Student
        fields = ('id','password', 'password2', 'email', 'name', 'image', 'slug', 'user_type')
        extra_kwargs = {
            'name': {'required': True},
            'image':{'required': False, 'allow_null' :True}
            
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = Student.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
            image= validated_data['image']
            
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user