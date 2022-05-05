from django.views.generic import View
from django.shortcuts import render, redirect
from Aboutme.models import AboutMe, SocialMedia
from Portfolio.models import WorkHistory, EducationHistory, Skill, Portfolio
from ContactUs.models import ContactUs
from ContactUs.forms import ContactForm


class Home(View):
    template_name = 'index.html'

    def get(self, request):
        about = AboutMe.objects.first()
        work_histories = WorkHistory.objects.all()
        education_histories = EducationHistory.objects.all()
        skills = Skill.objects.filter(is_circle=False)
        skills_chart = Skill.objects.filter(is_circle=True)
        social_media = SocialMedia.objects.all()
        portfolios = Portfolio.objects.all()
        form = ContactForm()
        context = {'about': about, 'work_histories': work_histories, "education_histories": education_histories,
                   'skills': skills, "skills_chart": skills_chart, "social_media": social_media,
                   "portfolios": portfolios, 'form': form}

        return render(request, self.template_name, context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            text = form.cleaned_data.get('text')
            ContactUs.objects.create(name=name, email=email, text=text)
            return redirect('Home:home_page')
        return redirect('Home:home_page')