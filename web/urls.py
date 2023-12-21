from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='web'
urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contacts/',views.contacts,name='contact'),
    path('downloads/',views.downloads,name='downloads'),
    path('products/',views.product,name='products'),
    path('services/',views.services,name='services'),
    path('team/',views.team,name='teams'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('qc_search/',views.search_qc,name='qc_search'),
    path('pdf/',views.pdf_temp,name='pdf_temp'),
    path('pdf_download/<str:arg>',views.pdf_download,name="pdf_download"),
  #  path('pdf_view/', views.render_pdf_view, name="pdf_view"),
   # path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
