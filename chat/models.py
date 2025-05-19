from django.db import models

class ChatMessage(models.Model):
    user_input = models.TextField()
    bot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class DailyAffirmation(models.Model):
    text = models.TextField()
    category = models.CharField(max_length=100, default="general")

class SupportResource(models.Model):
    name = models.CharField(max_length=200)
    resource_type = models.CharField(max_length=20)  
    details = models.CharField(max_length=200)