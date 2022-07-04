"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Login.as_view(), name="login"),
    path("main", Main.as_view(), name="main"),
    path("activity-book", Activity_Book.as_view(), name="activity-book"),
    path("teacher-guide", Teachers_Guide.as_view(), name="teacher-guide"),
    path("checkhomework", Checkhomework.as_view(), name="checkhomework"),
    path("tutorial-video", Videos.as_view(), name="videos"),
    path("tutorial-pdf", Files.as_view(), name="files"),
]

"""

    path("level/A", LevelA.as_view(), name="levelA"),
    path("level/B", LevelB.as_view(), name="levelB"),
    path("level/C", LevelC.as_view(), name="levelC"),

    path("book/1/A", Book_1A.as_view(), name="book_1A"),
    path("book/2/A", Book_1A.as_view(), name="book_2A"),
    path("book/3/A", Book_1A.as_view(), name="book_3A"),
    path("book/4/A", Book_1A.as_view(), name="book_4A"),
    path("book/5/A", Book_1A.as_view(), name="book_5A"),
    path("book/6/A", Book_1A.as_view(), name="book_6A"),
    path("book/7/A", Book_1A.as_view(), name="book_7A"),
    path("book/8/A", Book_1A.as_view(), name="book_8A"),
    path("book/9/A", Book_1A.as_view(), name="book_9A"),
    path("book/10/A", Book_1A.as_view(), name="book_10A"),
    path("book/11/A", Book_1A.as_view(), name="book_11A"),
    path("book/12/A", Book_1A.as_view(), name="book_12A"),

    path("book/1/B", Book_1B.as_view(), name="book_1B"),
    path("book/2/B", Book_1B.as_view(), name="book_2B"),
    path("book/3/B", Book_1B.as_view(), name="book_3B"),
    path("book/4/B", Book_1B.as_view(), name="book_4B"),
    path("book/5/B", Book_1B.as_view(), name="book_5B"),
    path("book/6/B", Book_1B.as_view(), name="book_6B"),
    path("book/7/B", Book_1B.as_view(), name="book_7B"),
    path("book/8/B", Book_1B.as_view(), name="book_8B"),
    path("book/9/B", Book_1B.as_view(), name="book_9B"),
    path("book/10/B", Book_1B.as_view(), name="book_10B"),
    path("book/11/B", Book_1B.as_view(), name="book_11B"),
    path("book/12/B", Book_1B.as_view(), name="book_12B"),

    path("book/1/C", Book_1C.as_view(), name="book_1C"),
    path("book/2/C", Book_1C.as_view(), name="book_2C"),
    path("book/3/C", Book_1C.as_view(), name="book_3C"),
    path("book/4/C", Book_1C.as_view(), name="book_4C"),
    path("book/5/C", Book_1C.as_view(), name="book_5C"),
    path("book/6/C", Book_1C.as_view(), name="book_6C"),
    path("book/7/C", Book_1C.as_view(), name="book_7C"),
    path("book/8/C", Book_1C.as_view(), name="book_8C"),
    path("book/9/C", Book_1C.as_view(), name="book_9C"),
    path("book/10/C", Book_1C.as_view(), name="book_10C"),
    path("book/11/C", Book_1C.as_view(), name="book_11C"),
    path("book/12/C", Book_1C.as_view(), name="book_12C"),

    path("board/notice", Board_Notice.as_view(), name="board_notice"),
    path("board/notice/4", Board_Notice4.as_view(), name="board_notice_4"),
    path("board/studyplan/34", Board_Studyplan34.as_view(), name="board_studyplan_34"),
    path("board/studyplan/40", Board_Studyplan40.as_view(), name="board_studyplan_40"),
    path("contents/nemies", Contents_Nemies.as_view(), name="contents_nemies"),
"""


