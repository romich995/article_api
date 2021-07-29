"""simpleapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .apps.article.views import ArticleView, CommentView
urlpatterns = [
        path('article/', ArticleView.as_view({'post': 'create'})),
        path('comment/', CommentView.as_view({'post': 'create'})),
        path('article/<pk>/shadow_comments/', ArticleView.as_view({'get': 'get_comments_by_article'})),
        path('comment/<pk>/nested_third_levels_comments/', CommentView.as_view({'get': 'get_all_comments_wth_incl_level'}))
    #    path('admin/', admin.site.urls),
]
