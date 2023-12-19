from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import qc_datasheet_mueller_hinton_agar
import pdfkit 
from run.settings import BASE_DIR
import os
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View
from django.views.generic import ListView
from django.contrib.staticfiles import finders
from django.conf import settings
from django.http import HttpResponse


class qcListView(ListView):
     model=qc_datasheet_mueller_hinton_agar


def qc_render_pdf_view(request, *args,**kwargs):
     pass


def link_callback(uri, rel):
            
            if os.path.isabs(uri):
                  print(uri)   
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise RuntimeError(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path

def render_pdf_view(request):
    template_path = 'pdf_template.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response,link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None
# Create your views here.

data = {
	"company": "Dennnis Ivanov Company",
	"address": "123 Street name",
	"city": "Vancouver",
	"state": "WA",
	"zipcode": "98663",


	"phone": "555-555-2345",
	"email": "youremail@dennisivy.com",
	"website": "dennisivy.com",
	}
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('web/pdf_template.html', data)
		return HttpResponse(pdf, content_type='application/pdf')
     
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('web/pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response


def index(request):
    
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def contacts(request):
    return render(request,'contact.html')





def logoutUser(request):
    logout(request)
    return redirect('web:index')

def product(request):
    return render(request,'product.html')



def services(request):
    
    return render(request,'services.html')



def team(request):

    return render(request,'team-details.html')






def loginPage(request):
  
  if request.method=='POST':
        username=request.POST.get('email')
        password=request.POST.get('password')
        
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, "User Does Not Exist !")
        user =authenticate(request,username=username,password=password)       
       
        if user is not None:
            login(request,user)
            return redirect('web:downloads')
        else:
            messages.error(request,"Username is not registered")
    

  return render(request,'login.html')


@login_required(login_url='web:login')
def downloads(request):
    default='Nothing Found'
    user=request.user.username
   
    if request.method=='GET':
             searched=request.GET.get('search-qc') if request.GET.get('search-qc') !=None else ''               
             
             qc=qc_datasheet_mueller_hinton_agar.objects.filter(Lot_No=searched)         
             #print(qc[0].color)
             if not qc :
                
                print('qc is none')
                return render(request,'download.html',{
                            'data_searched':default,
                            'data' :user               
                })
             
             else :
                  print('qc is not none')
                  return render(request,'download.html',{
                    'data_searched':qc[0].Lot_No
,                    'data':user
                })      

    user=request.user.username
    return render(request,'download.html',{
        'data':user
    })



def pdf_temp(request):
     return render(request,'pdf_template.html')

def pdf_download(request,arg):
     actual_pdf_path=os.path.join(BASE_DIR,f"web/templates/pdf_template.html")
     print(actual_pdf_path)
     qc=qc_datasheet_mueller_hinton_agar.objects.filter(Lot_No=arg)
     return render(request,'pdf_template.html',{
          'title':qc[0],
          'qc_data':qc
     })
      


def search_qc(request):

            return render(request,'download.html')
