from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import path
from .forms import *
from .models import *
    
 
def show_panel(request):
    if request.user.is_authenticated:
        user_pages = Pages.objects.filter(user=request.user)
        return render(request, 'Home.html', context={"user":request.user, "active":"Home", "code_form":code_form, "upload_form":UploadFileForm, "pages":user_pages})
    else:
        return HttpResponseRedirect("/auth/login")
  
def show_page(request, user, page_id):
    try:
        page = Pages.objects.get(user=user, id=page_id)
        return HttpResponse(page.code)
    except Pages.DoesNotExist:
        return HttpResponse("Page not found", status=404)
 
 
  
def upload_html_file(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                uploaded_file = request.FILES['file']
                file_extension = uploaded_file.name.split('.')[-1]
                file_content = uploaded_file.read().decode('utf-8')
                
                if file_extension == "html":
                    # save in model
                    new_book = Pages(code=file_content, user=request.user)
                    new_book.save()
                    new_book_id = new_book.id
                    new_book_url = f"/pages/xx/{request.user}/{new_book_id}"
                    
                    return render(request, 'Message.html', context={"Text":f"Creating Successful  <a href='{new_book_url}'>Click here</a>", "time":3})
                else:
                    return render(request, 'ERROR.html', context={"Text":"Your File is not Valid", "time":3}) 
            else:
                return render(request, 'ERROR.html', context={"Text":"Creating faild", "time":3})
        else:
            return render(request, 'ERROR.html', context={"Text":"Creating faild", "time":3})
    else:
        return HttpResponseRedirect("/auth/login")

def upload_html_text(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = code_form(request.POST)
            if form.is_valid():
                code = form.cleaned_data['code']
                # save in model
                new_book = Pages(code=code, user=request.user)
                new_book.save()
                new_book_id = new_book.id
                new_book_url = f"/pages/xx/{request.user}/{new_book_id}"
                
                return render(request, 'Message.html', context={"Text":f"Creating Successful  <a href='{new_book_url}'>Click here</a>", "time":3})
            else:
                return render(request, 'ERROR.html', context={"Text":"Creating faild", "time":3})
            
        else:
            return render(request, 'ERROR.html', context={"Text":"Creating faild", "time":3})
    else:
        return HttpResponseRedirect("/auth/login")


def delete_page(request, user, page_id):
    try:
        page = Pages.objects.get(user=user, id=page_id)
        page.delete()
        return HttpResponseRedirect("/Panel")
    except Pages.DoesNotExist:
        return render(request, 'ERROR.html', context={"Text":"Deleting faild", "time":3})
        

