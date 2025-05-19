from openai import OpenAI
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from dotenv import load_dotenv
from django.http import JsonResponse
from utils.affirmations import get_daily_affirmation
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
from .models import *
load_dotenv()



def affirmation_view(request):
    affirmation = get_daily_affirmation()
    return JsonResponse({"affirmation": affirmation})


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@csrf_exempt
def chat_with_bot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')

        if 'chat_history' not in request.session:
            request.session['chat_history'] = [
                {"role": "system", "content": "You are a friendly mental health assistant. Be kind, gentle, and helpful."}
            ]

        request.session['chat_history'].append({"role": "user", "content": user_message})

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=request.session['chat_history']
            )

            reply = response.choices[0].message.content.strip()

            request.session['chat_history'].append({"role": "assistant", "content": reply})
            request.session.modified = True 

            return JsonResponse({'response': reply})
        except Exception as e:
            return JsonResponse({'response': str(e)}, status=500)


from django.shortcuts import render

def chat_page(request):
    return render(request, "chat.html")

def home(request):
    return render(request, 'home.html')



@api_view(['POST'])
def chat(request):
    user_message = request.data.get('message', '')
    bot_response = "Mock response: " + user_message  
    ChatMessage.objects.create(user_input=user_message, bot_response=bot_response)
    return Response({'response': bot_response})

@api_view(['GET'])
def get_affirmation(request):
    affirmations = DailyAffirmation.objects.all()
    return Response({'affirmation': random.choice(affirmations).text if affirmations else "You matter!"})

@api_view(['GET'])
def get_resources(request):
    resources = SupportResource.objects.all()
    return Response([{'name': r.name, 'details': r.details} for r in resources])