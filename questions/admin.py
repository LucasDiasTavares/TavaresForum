from django.contrib import admin
from questions.models import Question, Answer

admin.site.register(Question)
admin.site.register(Answer)
