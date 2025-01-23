from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from chat.models import User, Message
from django.http import HttpResponse
from django.db.models import Q
import boto3
from django.conf import settings
from django.shortcuts import render



def signup(request):
    if request.method == "POST":
        # Example logic: Process the signup form
        username = request.POST['username']
        password = request.POST['password']
        # Create a new user (make sure you handle exceptions properly)
        user = User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'signup.html')  # Render the signup page


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('chat_room')  # Redirect to the chat room upon successful login
        else:
            return HttpResponse("Invalid credentials")  # Replace this with a proper error display
    return render(request, 'login.html')  # Render the login page


def logout(request):
    auth_logout(request)
    return redirect('login')


def chat_room(request):
    if not request.user.is_authenticated:
        return redirect('login')

    # Get all users except the logged-in user
    users = User.objects.exclude(pk=request.user.pk)

    # Get messages for the logged-in user
    messages = Message.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user)
    ).order_by('-timestamp')

    # Handle form submission (if applicable) for sending messages
    if request.method == 'POST':
        # Example form handling
        receiver_id = request.POST['receiver']
        content = request.POST['content']
        receiver = User.objects.get(pk=receiver_id)
        Message.objects.create(sender=request.user, receiver=receiver, content=content)
        return redirect('chat_room')  # Redirect back to the chat room

    context = {
        'users': users,
        'messages': messages,
    }
    return render(request, 'chat/chat_room.html', context)
def upload_to_aws(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
        s3.upload_fileobj(file, settings.AWS_STORAGE_BUCKET_NAME, file.name)

        return HttpResponse("File uploaded successfully.")
    return render(request, 'upload.html')