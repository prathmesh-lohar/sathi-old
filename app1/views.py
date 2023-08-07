from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from app1.models import profile,family_details,media
# Create your views here.

def home(request):
    from app1.models import profile,family_details,media
    featured1 = profile.objects.filter(is_featured=1)[:8]
    featured2 = profile.objects.filter(is_featured=1)[8:]

    data={
        'featured1':featured1,
        'featured2':featured2,
    }

    return render(request, "index.html",data)

def login(request):
    
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        
        user = auth.authenticate(username=uname, password=pwd)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return HttpResponse("uname , password invalid ")

    return render(request, "login.html")

def login1st(request):
    
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        
        user = auth.authenticate(username=uname, password=pwd)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/new_profile')
        else:
            return HttpResponse("uname , password invalid ")

    return render(request, "login.html")


def logout(request):
    auth.logout(request)

    return redirect('/')

def register(request):
    
    if request.method == "POST":
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
    
        # u = User(password=pwd, username=uname, email=email,first_name=fname, last_name=lname)    
        User.objects.create_user(password=pwd, username=uname, email=email,first_name=fname, last_name=lname)
        
 
        return redirect('/login')
    else:
        HttpResponse("faield")
    


def profile(request):
    return render(request, "profile.html")

def new_profile(request):
    return render(request, "new_profile.html")


def save_personal_detail(request):
    if request.method == "POST":
        mobile = request.POST.get('mobile')
        mstatus = request.POST.get('mstatus')
        dob = request.POST.get('dob')
        height = request.POST.get('height')
        color = request.POST.get('color')
        qualification = request.POST.get('qualification')
        work = request.POST.get('work')
        experience = request.POST.get('experience')
        Hobbies = request.POST.get('Hobbies')
        Income = request.POST.get('Income')
        medical_condition = request.POST.get('medical_condition')
        city = request.POST.get('city')
        about = request.POST.get('about')
        userid = request.POST.get('userid')
        gender = request.POST.get('gender')
        age = request.POST.get('age')


        from app1.models import profile
        obj=profile(user=User.objects.get(pk=request.user.id),mobile=mobile,marrital_status=mstatus,dob=dob,height=height,color=color,Qualification=qualification,work=work,experience=experience,hobbies=Hobbies,income=Income,medical_condition=medical_condition,city=city,about_me=about,gender=gender,age=age)
        obj.save()


    return redirect('/family_details')



def family_details(request):

    if request.method == "POST":
        father_name = request.POST.get('father_name')
        father_education = request.POST.get('father_education')
        father_occupation = request.POST.get('father_occupation')
        mother_name = request.POST.get('mother_name')
        mother_education = request.POST.get('mother_education')
        mother_occupation = request.POST.get('mother_occupation')
        sister = request.POST.get('sister')
        brother = request.POST.get('brother')
        native_place = request.POST.get('native_place')
        relatives = request.POST.get('relatives')

        from app1.models import family_details
        obj=family_details(user=User.objects.get(pk=request.user.id),father_name=father_name,father_education=father_education,father_occupation=father_occupation,mother_name=mother_name,mother_education=mother_education,mother_occupation=mother_occupation,brother=brother,sister=sister,relatives=relatives,native_place=native_place)
        obj.save()

        return redirect('/cdp')

    return render(request, "family_details.html")

def cdp(request):
    if request.method == "POST":
        picture__input = request.FILES['picture__input']
        from app1.models import media
        obj=media(user=User.objects.get(pk=request.user.id),dp=picture__input)
        obj.save()

        return redirect('/')

    return render(request, "cdp.html")


def all_profiles(request):
    from app1.models import profile,family_details,media
    male_profiles = profile.objects.all()
    # male_profiles = profile.objects.filter(gender="Male").order_by('-id')
    female_profiles = profile.objects.filter(gender="Female").order_by('-id')

    data ={
        'male_profiles':male_profiles,
        'female_profiles':female_profiles
    }
    return render(request,"all_profiles.html",data)
