from .models import Account
from  rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields =( 
                'id',
                'email',
                'username',
                'password', 
                'roleID',
                )
    def validate(self, args):
        email = args.get('email', None)
        if Account.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})

        return super().validate(args)

    def create(self, validated_data):
        return Account.objects.create(**validated_data)
    

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
    
    
class UpdateAccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = Account
        fields = ('username', 'email')


    def validate_email(self, value):
        user = self.context['request'].user
        if Account.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if Account.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):

        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()

        return instance

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = Account
        fields = ['token']