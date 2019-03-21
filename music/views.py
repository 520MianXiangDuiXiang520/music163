from django.shortcuts import redirect,render
import requests
from bs4 import BeautifulSoup
from .models import 华语男歌手,欧美男歌手,日本男歌手,韩国男歌手,其他男歌手,华语女歌手,欧美女歌手,日本女歌手,韩国女歌手,其他女歌手,华语组合,欧美组合,日本组合,韩国组合,其他歌手组合
from urllib.request import urlretrieve
import re
from lxml.html import fromstring,tostring
from django.contrib.auth import authenticate,login,logout

artists = []
id = []

def get_artists(url,flag):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Cookie': '_iuqxldmzr_=32; _ntes_nnid=0e6e1606eb78758c48c3fc823c6c57dd,1527314455632; '
                         '_ntes_nuid=0e6e1606eb78758c48c3fc823c6c57dd; __utmc=94650624; __utmz=94650624.1527314456.1.1.'
                         'utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_TID=blBrSVohtue8%2B6VgDkxOkJ2G0VyAgyOY;'
                         ' JSESSIONID-WYYY=Du06y%5Csx0ddxxx8n6G6Dwk97Dhy2vuMzYDhQY8D%2BmW3vlbshKsMRxS%2BJYEnvCCh%5CKY'
                         'x2hJ5xhmAy8W%5CT%2BKqwjWnTDaOzhlQj19AuJwMttOIh5T%5C05uByqO%2FWM%2F1ZS9sqjslE2AC8YD7h7Tt0Shufi'
                         '2d077U9tlBepCx048eEImRkXDkr%3A1527321477141; __utma=94650624.1687343966.1527314456.1527314456'
                         '.1527319890.2; __utmb=94650624.3.10.1527319890',
               'Host': 'music.163.com',
               'Referer': 'http://music.163.com/',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/66.0.3359.181 Safari/537.36'}
    r = requests.get(url, headers=headers)
    text = r.text
    soup = BeautifulSoup(text, 'html.parser')
    s = soup.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'})

    r = '[1-9]+.+的'
    id_r = '([0-9]+[0-9])'
    art_r = '[0-9]+" title="'
    art_r2 = '的'

    for i in s:
        i = repr(i)
        ss = re.findall(r, i)
        ids = re.findall(id_r, ss[0])
        arts = re.sub(art_r, "", ss[0])
        arts = re.sub(art_r2, "", arts)
        if flag=='华语男歌手':

            obj = 华语男歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='欧美男歌手':

            obj = 欧美男歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='日本男歌手':

            obj = 日本男歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='韩国男歌手':

            obj = 韩国男歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='其他男歌手':

            obj = 其他男歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='华语女歌手':

            obj = 华语女歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='欧美女歌手':

            obj = 欧美女歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='日本女歌手':

            obj = 日本女歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='韩国女歌手':

            obj = 韩国女歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='其他女歌手':

            obj = 其他女歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='华语组合':

            obj = 华语组合(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='欧美组合':

            obj = 欧美组合(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='日本组合':

            obj = 日本组合(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='韩国组合':

            obj = 韩国组合(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='其他组合':

            obj = 其他歌手组合(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()


def pachong(flag,geshouid):
    initial = [-1, 0, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
               89, 90]
    for jj in initial:
        url = 'https://music.163.com/discover/artist/cat?id=' + repr(geshouid) + '&initial=' + repr(jj)
        get_artists(url, flag)


# Create your views here.
def home(request):
    return render(request, "music/home.html")

def about(request):
    return render(request, "music/about.html")

# 单击主页更新，跳转到管理员登录界面
def auth(request):
    if request.method=='POST':
        users = authenticate(request, username=request.POST['用户名'], password=request.POST['密码'])
        if users==None:
            flag={'错误':'用户名或密码错误'}
            return render(request,'music/auth.html',flag)
    else:
        return render(request, 'music/auth.html')

def superuser_page(request):
    return render(request, 'music/superuser.html')


def update(request):
    韩国男歌手.objects.all().delete()
    日本男歌手.objects.all().delete()
    华语女歌手.objects.all().delete()
    欧美女歌手.objects.all().delete()
    日本女歌手.objects.all().delete()
    韩国女歌手.objects.all().delete()
    其他女歌手.objects.all().delete()
    其他男歌手.objects.all().delete()
    华语男歌手.objects.all().delete()
    欧美男歌手.objects.all().delete()
    其他歌手组合.objects.all().delete()
    韩国组合.objects.all().delete()
    日本组合.objects.all().delete()
    欧美组合.objects.all().delete()
    华语组合.objects.all().delete()
    flag='华语男歌手'
    pachong(flag,1001)
    flag='华语女歌手'
    pachong(flag,1002)
    flag = '华语组合'
    pachong(flag, 1003)
    flag='欧美男歌手'
    pachong(flag, 2001)
    flag = '欧美女歌手'
    pachong(flag, 2002)
    flag = '欧美组合'
    pachong(flag, 2003)
    flag='日本男歌手'
    pachong(flag, 6001)
    flag = '日本女歌手'
    pachong(flag, 6002)
    flag = '日本组合'
    pachong(flag, 6003)
    flag='韩国男歌手'
    pachong(flag, 7001)
    flag = '韩国女歌手'
    pachong(flag, 7002)
    flag = '韩国组合'
    pachong(flag, 7003)
    flag = '其他男歌手'
    pachong(flag, 4001)
    flag = '其他女歌手'
    pachong(flag, 4001)
    flag = '其他组合'
    pachong(flag, 4001)

    connect={'ID':id,'NAME':artists}
    return render(request, "music/auth.html", connect)

def song(url):
    id_list = []
    name_list=[]
    headers = {'Host': 'music.163.com',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Content - Type': 'application / x - www - form - urlencoded',
               'Content - Length': '340',
               'Cache - Control': 'max - age = 0',
               'Cookie': 'JSESSIONID-WYYY=dCYq9jVg67nSVCCTjqH5tYIQv2IdFZze425qd6DYKM7ZGny0wiM%2Ber3cIksIp6RU6Et9PfoqY4ynxubWRUAJ6v%2B8odx%2F7GYEGG%5Cbpq0v%2FqrY7yokmngDiInZBPDz1d7bZxjkZW8aiMC5jj%5Cgig7TJ4p%2BTzTqlugDJMxChHxeK%2ByZqy%5CK%3A1549352253864; _iuqxldmzr_=32; _ntes_nnid=7fff421235022c5dfe3cba199f702822,1549350453885; _ntes_nuid=7fff421235022c5dfe3cba199f702822; WM_NI=7n2V78OQ%2BkhVDHhadVHANe8nXD7BT1Q1ZNahjJVh7hZVXhd3%2F4Mo4qP%2Bgo1Az9ZQrkkY4%2FkAz1wYPyuytAySNmgVn3okb%2FHE%2Fb%2BZOC1Cj%2Bx3cFFX5MpsLFw0Pp2OXtNhVm8%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed6e53eedb297bbe63ef1968ba3c44e879f9baaf37d8bf5ff86f77ef1ba8490c82af0fea7c3b92af5b2feb7b6348d8fe58ceb5e8898a882e75e8c9f8286bb669c9cf9a3d73b93ef96afe464aa969a89b6649a8a9889e739edec8390b77b94f5a990b44bbae796b2f161a987fcd0ea4bbaefb9bad373b7a7bca2fc598eb3a9b7ed39adb5aed0cb4fedbee5bbce49f39da6ccfb39a19a8ab9b847b4ad84a7f63c94b0feb0db808eb89a8ebb37e2a3; WM_TID=e4GH8XbWYNpBRQAEEQJshJuwL8vzeetE',
               'Referer': 'http://music.163.com/',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
    r=requests.get(url,headers=headers)
    text=r.text
    #print(text)
    soup = BeautifulSoup(text, 'html.parser')
    s=soup.find_all('ul', attrs={'class': 'f-hide'})

    s=repr(s[0])
    tree=fromstring(s)
    s=tostring(tree,pretty_print=True)
    soup=BeautifulSoup(s,'html.parser')
    s=soup.find_all('a')
    #print(s[0])
    r='[0-9]+.+[\u4e00-\u9fa5]'
    d='">'
    n='[0-9]+'
    nam='[\u4e00-\u9fa5]+'
    for i in s:
        try:
            s=re.findall(r,repr(i))
            s=re.sub(d,"",repr(s[0]))
            id=re.findall(n,s)
            name=re.findall(nam,s)
            id_list.append(id[0])
            name_list.append(name[0])
        except:
            continue
    dit = dict.fromkeys(id_list, "1")
    for a in range(len(id_list)):
        dit[id_list[a]]=name_list[a]
    return dit

def down(dit,get_path):
    for id in dit.keys():
        downloadurl='http://music.163.com/song/media/outer/url?id='+id
        path=get_path+'\%s.mp3'%dit[id]
        try:
            urlretrieve(downloadurl,path)
        except:
            continue

def chboy(request):
    name=华语男歌手.objects.all()
    connect={'a':name}
    return render(request, "music/ch.html",connect)

def chgir(request):
    name=华语女歌手.objects.all()
    connect = {'a': name}
    return render(request, "music/ch.html", connect)

def chzh(request):
    name=华语组合.objects.all()
    connect = {'a': name}
    return render(request, "music/ch.html", connect)

def usboy(request):
    name = 欧美男歌手.objects.all()
    connect = {'a': name}
    return render(request, "music/ch.html",connect)

def usgir(request):
    name = 欧美女歌手.objects.all()
    connect = {'a': name}
    return render(request, "music/ch.html",connect)

def uszh(request):
    name = 欧美组合.objects.all()
    connect = {'a': name}
    return render(request, "music/ch.html",connect)

def jpboy(request):
    name = 日本男歌手.objects.all()
    connect = {'a': name}
    return render(request, "music/ch.html",connect)

def jpgir(request):
    name = 日本女歌手.objects.all()
    connect = {'a': name}
    return render(request, "music/ch.html",connect)

def jpzh(request):
    name = 日本组合.objects.all()
    connect = {'a': name}
    return render(request, "music/ch.html",connect)

def smdboy(request):
    name = 韩国男歌手.objects.all()
    connect = {'a': name}
    return render(request, "music/ch.html",connect)

def smdgir(request):
    name = 韩国女歌手.objects.all()
    connect = {'a': name}
    return render(request, "music/ch.html",connect)

def smdzh(request):
    name = 韩国组合.objects.all()
    connect = {'a': name}
    return render(request, "music/ch.html",connect)

def qtboy(request):
    name = 其他男歌手.objects.all()
    connect = {'a': name}
    return render(request, "music/ch.html", connect)

def qtgir(request):
    name = 其他女歌手.objects.all()
    connect = {'a': name}
    return render(request, "music/ch.html", connect)

def qtzh(request):
    name = 其他歌手组合.objects.all()
    connect = {'a': name}
    return render(request, "music/ch.html", connect)

def songs(request,info_歌手ID):
    url = 'https://music.163.com/artist?id=' + info_歌手ID
    dit = song(url)

    #down(dit)
    info=dit.items()
    connect={'a':info,'ID':info_歌手ID}

    return render(request, "music/song.html", connect)

def alldownl(request):
    # 需要得到歌曲id列表

    if request.method == "POST":
        h = request.POST['下载']
        url = 'https://music.163.com/artist?id=' + h
        dit = song(url)
        info = dit.items()
        path=request.POST['下载路径']
        if path=='':
            connect={'a':info,'警告':'未输入路径'}
        else:
            down(dit, path)
            connect={'a':info,'成功提示':'开始下载'}
        return render(request, "music/song.html", connect)
    else:
        return render(request, "music/song.html")
