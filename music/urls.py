from django.urls import path,include
from . import views

app_name='music'
urlpatterns = [
    path('home/',views.home,name='主页' ),
    path('about/',views.about,name='关于' ),
    path('chboy/',views.chboy,name='华语男'),
    path('chgir/', views.chgir, name='华语女'),
    path('chzh/',views.chzh,name='华语组合'),
    path('usboy/',views.usboy,name='欧美男'),
    path('usgir/',views.usgir,name='欧美女'),
    path('uszh/',views.uszh,name='欧美组合'),
    path('jpboy/',views.jpboy,name='日本男'),
    path('jpgir/', views.jpgir, name='日本女'),
    path('jpzh/', views.jpzh, name='日本组合'),
    path('smdboy/',views.smdboy,name='韩国男'),
    path('smdgir/', views.smdgir, name='韩国女'),
    path('smdzh/', views.smdzh, name='韩国组合'),
    path('qtboy/',views.qtboy,name='其他男'),
    path('qtgir/',views.qtgir,name='其他女'),
    path('qtzh/',views.qtzh,name='其他组合'),
    path('update/',views.auth,name='管理员登录'),
    path('songs/<info_歌手ID>',views.songs,name='歌曲'),
    path('alldownl/',views.alldownl,name='全部下载'),
    path('superuser_page/', views.superuser_page, name='管理员页面'),
    path('更新/', views.update, name='更新'),
]