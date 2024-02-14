from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User, auth
from . models import *
from . forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from django.conf import settings

from web.views import *

from django.shortcuts import render, get_object_or_404
from django.http import Http404

from django.contrib.auth import get_user_model

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.db.models import Sum
from django.shortcuts import get_list_or_404

# Create your views here.
# @login_required(login_url='signin')
def admin(request):
    return render(request, 'sims/admin.html')
@login_required(login_url='signinsims')
def addstudents(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # id = request.POST.get('id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyStaff.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('addstudents')
            elif MyStaff.objects.filter(username=username).exists():
                messages.info(request, f"Id Number {username} Already Taken")
                return redirect('addstudents')
            else:
                user = MyStaff.objects.create_user(username=username, email=email, password=password)
                user.save()
                # messages.info(request, 'Registered Student Succesefull.')
                return redirect('addPatient')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('addstudents')

    else:
        return render(request, 'sims/addstudents.html')
    
# @login_required(login_url='signinsims')
def addstaff(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        # id = request.POST.get('id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyStaff.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('addstaff')
            elif MyStaff.objects.filter(username=username).exists():
                messages.info(request, f"Id Number {username} Already Taken")
                return redirect('addstaff')
            else:
                user = MyStaff.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, 'Registered Staff Succesefull.')
                return redirect('addstaffcontactinfo')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('addstaff')

    else:
        return render(request, 'sims/addstaff.html')


def signinsims(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.info(request, 'Loged in succesefull.')
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('signinsims')

    else:
        return render(request, 'sims/signinsims.html')

@login_required(login_url='signinsims')
def logout(request):
    auth.logout(request)
    messages.info(request, 'Loged out succesefull.')
    return redirect('signinsims')

@login_required(login_url='signinsims')
def news(request):
    return render(request, 'sims/news.html')

@login_required(login_url='signinsims')
def dashboard(request):
    return render(request, 'sims/dashboard.html')

# def base(request):
#     # Assuming 'username' is the attribute in MyStaff that corresponds to the user's username
#     logged_in_user = MyStaff.objects.get(username=request.user.username)

#     # Fetching CA results related to the logged-in user using the obtained 'logged_in_user' instance
#     profilename = Patient.objects.filter(Ca_Number__user=logged_in_user)
    
#     context={
#         "profilename":profilename,
#         # "countstaff":countstaff
#     }
#     return render(request, 'sims/base.html', context)

@login_required(login_url='signinsims')
def base(request):
    # Assuming 'username' is the attribute in MyStaff that corresponds to the user's username
    logged_in_user = MyStaff.objects.get(username=request.user.username)

    # Fetching related Patient for the logged-in user
    student_contact_info = Patient.objects.filter(user=logged_in_user).first()

    if student_contact_info:
        # Accessing first name and last name from Patient
        first_name = student_contact_info.First_Name
        last_name = student_contact_info.Last_Name

        return render(request, 'sims/base.html', {'first_name': first_name, 'last_name': last_name})
    else:
        # Handle scenario where there's no related Patient
        return render(request, 'sims/base.html')  


@login_required(login_url='signinsims')
def patient(request):
    patient = Patient.objects.all().order_by("-pk")
    context={
        "patient":patient
    }
    return render(request, 'sims/patient.html', context)



class viewpatient(DetailView):
    model = Patient
    template_name = 'sims/viewpatient.html'
    # count_hit = True
    # HII NI CODES KWA AJILI YA POST DETAIL PAGE KWA KUTUMIA CLASS VIEW ZINAISHIA HAPA

#SASA HIZI ZINAZOANZIA HAPA NI KWA AJILI YA COMMENT KWENYE POST HUSIKA
    form = PatientinfoForm

    def post(self, request, *args, **kwargs):
        form = PatientinfoForm(request.POST)
        if form.is_valid():
            Title = self.get_object()
            form.instance.user = request.user
            form.instance.Title = Title
            form.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        #kwa ajili ya kudisplay comment huo mstari wa chini
        post_comments = Patientinfo.objects.all().filter(Title=self.object.pk)
        
        #zinaendelea za kupost comment kwa admin
        context = super().get_context_data(**kwargs)
        #context["form"] = self.form
        context.update({
                'form':self.form,
                'post_comments':post_comments,
                # 'post_comments_count':post_comments_count,
            })
        return context
    
    

@login_required(login_url='signinsims')
def studentaccount(request):
    studentaccount = MyStaff.objects.all()
    # countstaff= MyStaff.objects.all().count()
    context={
        "studentaccount":studentaccount,
        # "countstaff":countstaff
    }
    return render(request, 'sims/studentaccount.html', context)

@login_required(login_url='signinsims')
def staff(request):
    stafflist = StaffContactinfo.objects.all().order_by("-pk")
    # countstaff= MyStaff.objects.all().count()
    context={
        "stafflist":stafflist,
        # "countstaff":countstaff
    }
    return render(request, 'sims/staff.html', context)


@login_required(login_url='signinsims')
def news(request):
    return render(request, 'sims/news.html')

@login_required(login_url='signinsims')
def payments(request):
    return render(request, 'sims/payments.html')

@login_required(login_url='signinsims')
def profile(request):
    current_user = request.user
    
    try:
        user_instance = get_object_or_404(MyStaff, username=current_user.username)
        Patient= Patient.objects.filter(user=user_instance)

        context={
            "Patient":Patient,
            "user_instance":user_instance,
            "current_user":current_user
        }
        return render(request, 'sims/profile.html', context)

    except MyStaff.DoesNotExist:
        raise Http404("User does not exist")  # Handle case where user is not found

@login_required(login_url='signinsims')
def myprofile(request):
    current_user = request.user
    
    try:
        user_instance = get_object_or_404(MyStaff, username=current_user.username)
        staffcontactinfo= StaffContactinfo.objects.filter(user=user_instance)

        context={
            "staffcontactinfo":staffcontactinfo,
            "user_instance":user_instance,
            "current_user":current_user
        }
        return render(request, 'sims/myprofile.html', context)

    except MyStaff.DoesNotExist:
        raise Http404("User does not exist")  # Handle case where user is not found

@login_required(login_url='signinsims')
def addPatient(request):
    Patient = PatientForm()
    if request.method == "POST":
        Patient = PatientForm(request.POST, files=request.FILES)
        if Patient.is_valid():
            Patient.save()
            messages.info(request, 'Patient Added Succesefull.')
            return redirect('addPatient')

    context={
        "Patient":Patient
    }
    return render(request, 'sims/addPatient.html', context)

@login_required(login_url='signinsims')
def addstaffcontactinfo(request):
    staffcontactinfo = StaffContactinfoForm()
    if request.method == "POST":
        staffcontactinfo = StaffContactinfoForm(request.POST, files=request.FILES)
        if staffcontactinfo.is_valid():
            staffcontactinfo.save()
            messages.info(request, 'Student Registered Succesefull.')
            return redirect('addstaff')

    context={
        "staffcontactinfo":staffcontactinfo
    }
    return render(request, 'sims/addstaffcontactinfo.html', context)

# views for viewing
@login_required(login_url='signinsims')
def viewstudentaccount(request, id):
    studentaccountview = MyStaff.objects.get(id=id)
    
    context = {"studentaccountview":studentaccountview}
    return render(request, 'sims/viewstudentaccount.html', context)

@login_required(login_url='signinsims')
def viewpatientinfo(request, id):
    patientinfoview = Patient.objects.get(id=id)
    
    context = {"patientinfoview":patientinfoview}
    return render(request, 'sims/viewpatientinfo.html', context)

@login_required(login_url='signinsims')
def viewstaffinfo(request, id):
    staffinfoview = StaffContactinfo.objects.get(id=id)
    
    context = {"staffinfoview":staffinfoview}
    return render(request, 'sims/viewstaffinfo.html', context)

# view for updating the information
@login_required(login_url='signinsims')
def updatepatient(request, pk):
    a = Patient.objects.get(pk=pk)
    patient =PatientForm(instance=a)
    if request.method == "POST":
        patient = PatientForm(request.POST, files=request.FILES, instance=a)
        if patient.is_valid():
            patient.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('patient')
    context = {"patient":patient}
    return render(request, 'sims/updatepatient.html', context)

@login_required(login_url='signinsims')
def updatestaffcontactinfo(request, id):
    b = StaffContactinfo.objects.get(id=id)
    staffinfo =StaffContactinfoForm(instance=b)
    if request.method == "POST":
        staffinfo = StaffContactinfoForm(request.POST, files=request.FILES, instance=b)
        if staffinfo.is_valid():
            staffinfo.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('staff')
    context = {"staffinfo":staffinfo}
    return render(request, 'sims/updatestaffcontactinfo.html', context)

@login_required(login_url='signinsims')
def updatestudentaccount(request, id):
    c = MyStaff.objects.get(id=id)
    studentaccount =MyStaffForm(instance=c)
    if request.method == "POST":
        studentaccount = MyStaffForm(request.POST, files=request.FILES, instance=c)
    if studentaccount.is_valid():
        cleaned_data = studentaccount.cleaned_data
        # Check if the new username is different from the existing one
        if 'username' in cleaned_data and cleaned_data['username'] != c.username:
            # If it's different, update the instance and save
            c.username = cleaned_data['username']
            c.save()
            messages.info(request, 'Updated successfully.')
            return redirect('students')
        else:
            # Username remains unchanged, proceed without modifying
            messages.info(request, 'No changes made.')
            return redirect('students')
    context = {"studentaccount":studentaccount}
    return render(request, 'sims/updatestudentaccount.html', context)

# view for deleting information
@login_required(login_url='signinsims')
def deletepatient(request, pk):
    patientdelete = Patient.objects.get(pk=pk)
    if request.method == "POST":
        patientdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('patient')
    
    context = {"patientdelete":patientdelete}
    return render(request, 'sims/deletepatient.html', context)

@login_required(login_url='signinsims')
def deletestaffcontactinfo(request, id):
    staffcontactinfodelete = StaffContactinfo.objects.get(id=id)
    if request.method == "POST":
        staffcontactinfodelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('staff')
    
    context = {"staffcontactinfodelete":staffcontactinfodelete}
    return render(request, 'sims/deletestaffcontactinfo.html', context)

@login_required(login_url='signinsims')
def deletestudentaccount(request, id):
    studentaccountdelete = MyStaff.objects.get(id=id)
    if request.method == "POST":
        studentaccountdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('studentaccount')
    
    context = {"studentaccountdelete":studentaccountdelete}
    return render(request, 'sims/deletestudentaccount.html', context)


@login_required(login_url='signinsims')
def change_password(request):
    if request.method == 'POST':
        passwordchange = PasswordChangeForm(request.user, request.POST)
        if passwordchange.is_valid():
            user = passwordchange.save()
            # This is to keep the user logged in after password change
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('signinsims')  # Redirect to the same page after successful password change
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        passwordchange = PasswordChangeForm(request.user)
    return render(request, 'sims/change_password.html', {'passwordchange': passwordchange})


