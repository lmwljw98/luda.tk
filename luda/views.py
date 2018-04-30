from django.shortcuts import render, HttpResponse
import os
import random, datetime, shutil
from luda.models import My, Gmy, Time
from .forms import UploadFileForm
import zipfile
from django.views import View


def test(request):
    entry_list = list(My.objects.values_list('image_name', flat=True))
    entry_list2 = list(Gmy.objects.values_list('gif_name', flat=True))
    update_time = list(Time.objects.values_list('update_time', flat=True))
    # for i in range(len(entry_list)):
    #    entry_list[i] = entry_list[i].replace("&#39;", "'")
    random.shuffle(entry_list)
    random.shuffle(entry_list2)

    return render(request, 'luda/main.html', {'my': entry_list, 'my2': entry_list2, 'update': update_time})


def up(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadFileForm()
    return render(request, 'luda/upload.html', {'form': form})


def image(request):
    '''
    My.objects.all().delete()
    Time.objects.all().delete()
    ret_list = os.listdir("./static/image/")
    for i in range(len(ret_list)):
        q = My(image_name=ret_list[i])
        q.save()
    m = Time(update_time=datetime.datetime.now())
    m.save()
    return HttpResponse('Image Update')
    '''

    My.objects.all().delete()
    Time.objects.all().delete()
    ret_list = os.listdir("./static/image/")
    for i in range(len(ret_list)):
        if os.path.isdir(ret_list[i]):
            new = os.listdir("./static/image/" + ret_list[i])
            for file in new:
                q = My(image_name=ret_list[i] + '/' + file)
                q.save()
        else:
            q = My(image_name=ret_list[i])
            q.save()
    m = Time(update_time=datetime.datetime.now())
    m.save()
    return HttpResponse('Image Update')


def gif(request):
    Gmy.objects.all().delete()
    Time.objects.all().delete()
    ret_list2 = os.listdir("./static/gif/")
    for i in range(len(ret_list2)):
        a = Gmy(gif_name=ret_list2[i])
        a.save()
    m = Time(update_time=datetime.datetime.now())
    m.save()
    return HttpResponse('Gif Update')


def refresh(request):
    Time.objects.all().delete()
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')

    if not os.path.isdir('./static/image/' + nowDate):
        os.mkdir('./static/image/' + nowDate)
        #shutil.chown('./static/image/' + nowDate, user=pi, group=pi)
        #os.chmod('./static/image/' + nowDate, 0755)
    if not os.path.isdir('./static/gif/' + nowDate):
        os.mkdir('./static/gif/' + nowDate)
        #shutil.chown('./static/gif' + nowDate, user=pi, group=pi)
        #os.chmod('./static/gif/' + nowDate, 0755)

    current_dir = os.getcwd()

    for path, dirs, files in os.walk("./upload/"):
        if files:
            for filename in files:
                if not filename.endswith(".gif"):
                    #shutil.chown('./upload/' + nowDate + '/' + filename, user=pi, group=pi)
                    #os.chmod('./upload/' + nowDate + '/' + filename, 0755)
                    os.chdir("./upload/")
                    # append mode ( 압축파일에 또 다른 파일 추가하기 )
                    with zipfile.ZipFile('../static/zip/luda_tk_image.zip', mode='a') as f:
                        f.write(nowDate + '/' + filename, compress_type=zipfile.ZIP_DEFLATED)
                    os.chdir(current_dir)
                    q = My(image_name=nowDate + '/' + filename)
                    q.save()
                    shutil.move('./upload/' + nowDate + '/' + filename, './static/image/' + nowDate)
                else:
                    #shutil.chown('./upload/' + nowDate + '/' + filename, user=pi, group=pi)
                    #os.chmod('./upload/' + nowDate + '/' + filename, 0755)
                    os.chdir("./upload/")
                    with zipfile.ZipFile('../static/zip/luda_tk_gif.zip', mode='a') as f:
                        f.write(nowDate + '/' + filename, compress_type=zipfile.ZIP_DEFLATED)
                    os.chdir(current_dir)
                    a = Gmy(gif_name=nowDate + '/' + filename)
                    a.save()
                    shutil.move('./upload/' + nowDate + '/' + filename, './static/gif/' + nowDate)
    m = Time(update_time=datetime.datetime.now())
    m.save()
    return HttpResponse(nowDate + ' New Update')
