from cryptography.fernet import Fernet
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
# from .models import Post, PostActivity, Comment
from .models import Post

def Home(request):
    message = 'Home Page'
    return HttpResponse("Home")

ENCRYPTION_KEY = b"PczoyJQgy_xRAnp_YNkecV6KGROpqDv94_6COdyHrT8='"

def encrypt_data(data):
    fernet = Fernet(ENCRYPTION_KEY)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data):
    fernet = Fernet(ENCRYPTION_KEY)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

def all_posts(request):
    posts = Post.objects.all()

    serialized_posts = []

    for post in posts:
        serialized_post = {
            "content": post.content,
            "date_posted": post.date_posted.strftime('%Y-%m-%d %H:%M:%S'),
            "author": encrypt_data(post.author.username).decode('utf-8'),
            'mentioned_user': None,

        }

        if post.mentioned_user:
            serialized_post['mentioned_user'] = {
                'username': post.mentioned_user.username,
            }

        serialized_posts.append(serialized_post)

    return JsonResponse(serialized_posts, safe=False)