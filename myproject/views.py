from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

class Login(LoginView):
    template_name = 'login.html'

class Activity_Book(TemplateView):
    template_name = "activity-book.html"

class Teachers_Guide(TemplateView):
    template_name = "teacher's-guide.html"

class Main(LoginView):
    template_name = 'main.html'

class Checkhomework(TemplateView):
    template_name = "checkhomework.html"

class Videos(TemplateView):
    template_name = "videos.html"

class Files(TemplateView):
    template_name = "files.html"

class LevelA(TemplateView):
    template_name = "level A/index.html"

class LevelB(TemplateView):
    template_name = "level B/index.html"

class LevelC(TemplateView):
    template_name = "level C/index.html"

class Book_1A(TemplateView):
    template_name = "level A/book1.html"


"""


class Book_1B(TemplateView):
    template_name = "level/B/1.html"

class Book_1C(TemplateView):
    template_name = "level/C/1.html"

class Board_Notice(TemplateView):
    template_name = "board/notice/index.html"

class Board_Notice4(TemplateView):
    template_name = "board/notice/4.html"

class Board_Studyplan40(TemplateView):
    template_name = "board/studyplan/40.html"

class Board_Studyplan34(TemplateView):
    template_name = "board/studyplan/34.html"

class Contents_Nemies(TemplateView):
    template_name = "contents/nemies.html"

"""