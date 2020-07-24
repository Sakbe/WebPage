from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile

from .models import WorkExperience, Education, Award, Skill, Language

# Create your views here.
def home(request):
    return render(request, 'about/home.html', 
    {
        
    })

def cv(request):
    workexp = WorkExperience.objects.order_by('-start_date')
    eduexp = Education.objects.order_by('-start_date')
    awards = Award.objects.all
    skills = Skill.objects.all
    languages = Language.objects.all
    return render(request, 'about/cv.html', 
    {
        'workexp': workexp,
        'eduexp': eduexp,
        'awards': awards,
        'skills': skills,
        'languages': languages,        
    })

def generate_pdf(request):
    """Generate pdf."""
    # Model data
    workexp = WorkExperience.objects.order_by('-start_date')
    eduexp = Education.objects.order_by('-start_date')
    awards = Award.objects.all
    skills = Skill.objects.all
    languages = Language.objects.all    
    # Rendered
    html_string = render_to_string('about/pdf.html', {
        'workexp': workexp,
        'eduexp': eduexp,
        'awards': awards,
        'skills': skills,
        'languages': languages,
    })
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    doc = html.render()
    pdf = doc.write_pdf()
    # Creating http response
    response = HttpResponse(pdf, content_type='application/pdf;')
    #Download as attachment
    response['Content-Disposition'] = 'attachment; filename=CV-{0}.pdf'.format("JHV-SoftwareDeveloper")
    # Display in browser
    # response['Content-Disposition'] = 'inline; filename=CV-{0}.pdf'.format("JHV-SoftwareDeveloper")
    return response