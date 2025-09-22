from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from .models import Product
from .serializers import UserSerializer, ProductSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response

# User Registration API
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



# ---------------pro-----------------------

class ProductsByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        queryset = Product.objects.filter(category__slug=category_slug)
        # Handle filters (e.g., brand, color, etc.)
        brand = self.request.query_params.get('brand')
        if brand:
            queryset = queryset.filter(brand=brand)
        return queryset
    
# ------------------------------------------

from rest_framework.views import APIView
from .models import ContactMessage
from .serializers import ContactMessageSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

class ContactMessageView(APIView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        phone = request.data.get('phone')
        message = request.data.get('message')

        subject = f"New Contact Form Submission from {name}"
        body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """

        send_mail(
            subject,
            body,
            'muppuraj11@gmail.com',    # From email
            ['recipient-email@example.com'],  # To email
            fail_silently=False,
        )

        return Response({"success": "Message sent successfully"}, status=status.HTTP_200_OK)
    
# product detail----------------------------------
