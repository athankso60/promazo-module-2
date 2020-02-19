from django.contrib import admin
import nested_admin
# Register your models here.
from .models import Quiz, Question, Answer

class AnswerInline(nested_admin.NestedTabularInline):
 model = Answer
 extra = 4
 max_num = 4
class QuestionInline(nested_admin.NestedTabularInline):
 model = Question
 inlines = [AnswerInline,]
 extra = 19
class QuizAdmin(nested_admin.NestedModelAdmin):
 inlines = [QuestionInline,]

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
