from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactUs
from django.contrib import messages
from SiteSetting.models import Setting


def contact_us(request):
    form = ContactForm(request.POST or None)
    site_setting = Setting.objects.first()
    title = 'تماس با ما'
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        text = form.cleaned_data.get('text')
        ContactUs.objects.create(name=name, email=email, subject=subject
                                 , text=text)
        messages.success(request, 'پیام شما با موفقیت ارسال شد ')
        form = ContactForm()
        return redirect('ContactUs:contact-us')
    context = {'form': form, 'site_setting': site_setting, 'title': title}
    return render(request, 'ContactUs/contact-us.html', context)
