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
    path('up1/',views.up1,name='up1'),
    path('up2/',views.up2,name='up2'),
    path('up3/', views.up3, name='up3'),
    path('up4/', views.up4, name='up4'),
    path('up5/', views.up5, name='up5'),
    path('up6/', views.up6, name='up6'),
    path('up7/', views.up7, name='up7'),
    path('up8/', views.up8, name='up8'),
    path('up9/', views.up9, name='up9'),
    path('up10/', views.up10, name='up10'),
    path('up11/', views.up11, name='up11'),
    path('up12/', views.up12, name='up12'),
    path('up13/', views.up13, name='up13'),
    path('up14/', views.up14, name='up14'),
    path('up15/', views.up15, name='up15'),

]