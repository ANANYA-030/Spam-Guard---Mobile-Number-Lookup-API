from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.db.models import Q as query
from django.shortcuts import get_object_or_404

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = RegisteredUser.objects.all()
    serializer_class = RegisteredUserSerializer

class RegisteredUserListView(APIView):
     def get(self, request, user_id):
        user = get_object_or_404(RegisteredUser, pk=user_id)
        serializer = RegisteredUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
'''       
class LoginView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password') 
        print(password)
        print(phone_number)
        
        print("request", request)
        user = authenticate(request, phone_number=phone_number, password=password)
        print("login issue", authenticate(request, phone_number=phone_number, password=password))
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
'''
class SpamReportView(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        phone_number = request.data.get('phone_number')

        if not phone_number:
            return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

        if SpamReport.objects.filter(phone_number=phone_number).exists():
            return Response({'error': 'This number is already reported as spam'}, status=status.HTTP_400_BAD_REQUEST)

        spam_report = SpamReport(phone_number=phone_number)
        spam_report.save()

        return Response({'status': 'Number marked as spam'}, status=status.HTTP_200_OK)


class SearchByNameView(APIView):
    def get(self, request):
        name = request.query_params.get('name')

        if not name:
            return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)

        contacts_starts_with = Contact.objects.filter(contact_name__istartswith=name)
        contacts_contains = Contact.objects.filter(~query(contact_name__istartswith=name) & query(contact_name__icontains=name))
        users_starts_with = RegisteredUser.objects.filter(name__istartswith=name)
        users_contains = RegisteredUser.objects.filter(~query(name__istartswith=name) & query(name__icontains=name))
        
        spams = SpamReport.objects.all()
        
        results = []

        for contact in contacts_starts_with:
            if any(spam.phone_number == contact.contact_phone_number for spam in spams):
                results.append({
                    'Name': contact.contact_name,
                    'Phone Number': contact.contact_phone_number,
                    'Spam Status': 'This number is marked as spam'
                })
        
        for user in users_starts_with:
            if any(spam.phone_number == user.phone_number for spam in spams):
                results.append({
                    'Name': user.name,
                    'Phone Number': user.phone_number,
                    'Spam Status': 'This number is marked as spam'
                })
        
        for contact in contacts_contains:
            if any(spam.phone_number == contact.contact_phone_number for spam in spams):
                results.append({
                    'Name': contact.contact_name,
                    'Phone Number': contact.contact_phone_number,
                    'Spam Status': 'This number is marked as spam'
                })
        
        for user in users_contains:
            if any(spam.phone_number == user.phone_number for spam in spams):
                results.append({
                    'Name': user.name,
                    'Phone Number': user.phone_number,
                    'Spam Status': 'This number is marked as spam'
                })
        
        if not results:
            return Response({'message': 'No spam reported for this name'}, status=status.HTTP_404_NOT_FOUND)

        return Response(results, status=status.HTTP_200_OK)
    
class SearchByPhoneNumberView(APIView):
    def get(self, request):
        phone_number = request.query_params.get('phone_number')

        if not phone_number:
            return Response({'error': 'Phone Number is required'}, status=status.HTTP_400_BAD_REQUEST)

        contacts = Contact.objects.filter(contact_phone_number=phone_number)
        users = RegisteredUser.objects.filter(phone_number=phone_number)
        spams = SpamReport.objects.filter(phone_number=phone_number)

        results = []

        for contact in contacts:
            spam_status = 'This number is marked as spam' if any(spam.phone_number == contact.contact_phone_number for spam in spams) else 'Not marked as spam'
            results.append({
                'Name': contact.contact_name,
                'Phone Number': contact.contact_phone_number,
                'Spam Status': spam_status
            })

        for user in users:
            spam_status = 'This number is marked as spam' if any(spam.phone_number == user.phone_number for spam in spams) else 'Not marked as spam'
            results.append({
                'Name': user.name,
                'Phone Number': user.phone_number,
                'Spam Status': spam_status
            })

        if not results:
            return Response({'message': 'No results found for this phone number'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(results, status=status.HTTP_200_OK)
        
