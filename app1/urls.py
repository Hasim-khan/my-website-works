from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from app1 import views 

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .views import delete_record
urlpatterns = [
    path('',views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('Contact/', views.Contact, name='Contact'),
    path('faqs/', views.faqs, name='faqs'),
    path('our_blog/', views.ourblog.as_view(), name='our_blog'),
    path('blog_details/', views.blogdetails, name='blog_details'),
    path('services/', views.services, name='services'),
    path('service-details/', views.servicedetails, name='service-details'),
    path('team-details/', views.teamdetails, name='team-details'),
    path('pricingplans/', views.pricingplans, name='pricingplans'),
    path('ourprojects/', views.ourprojects.as_view(), name='ourprojects'),
    path('projectdetails/<slug>', views.projectdetails.as_view(), name='projectdetails'),
    path('contactform/', views.contactform, name='contactform'),

    ### Loginpage ###

    path('loginpage/', views.loginpage, name='loginpage'),
    path('adminform/', views.adminform, name='adminform'),
    path("userhome",views.userhome, name = 'userhome'),
    path("userlogout",views.userlogout, name = 'userlogout'),
    path("allrecord",views.allrecord, name = 'allrecord'),

    ### Forgotpassword ######
    # path('forgetpasspage/', views.forgetpasspage, name='forgetpasspage'),
    
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name='forgotpassword/forgetpass.html'), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='forgotpassword/password_reset_done.html'), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='forgotpassword/password_reset_confirm.html'), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name='forgotpassword/password_reset_complete.html'), name="password_reset_complete"),


    ### change password ###
    path('password-change/', PasswordChangeView.as_view(template_name='auth/password_change.html',success_url='/password-change/done/'),  name='password_change'),  # ✅ This should match the template     
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='auth/password_change_done.html'), name='password_change_done'),

    ### deleterecord #####
    path('delete/<int:record_id>/', views.delete_record, name='deleterecord'),



    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),


]
