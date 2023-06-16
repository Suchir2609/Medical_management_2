from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, DoctorCreationForm, AppointmentUpdateForm, AppointmentStatusForm, DoctorUpdationForm
from django.contrib import messages
from .models import  User, Doctor, Appointment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView


def index(request):
    return render(request, 'users/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to log in ')
            return redirect('staff-login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


def staff_home(request):
    return render(request,'users/staff_home.html')


def patient_home(request):
    return render(request, 'users/patient_home.html')


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    fields = ['problems', 'doctors_wanted', 'date']
    template_name = 'users/appointment_new.html'
    success_url = '/patient_home'

    def form_valid(self, form):
        form.instance.patient_name = self.request.user
        return super().form_valid(form)


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'users/staff_home.html'
    context_object_name = 'appointments'


class AppointmentListViewPatient(ListView):
    model = Appointment
    template_name = 'users/patient_home.html'
    context_object_name = 'appointments'


def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentUpdateForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Appointment has been successfully updated! ')
            return redirect('patient-home')
    else:
        form = AppointmentUpdateForm(instance=appointment)
    return render(request, 'users/appointment_update.html', {'form': form})


def doctor_create(request):
    if request.method == 'POST':
        form = DoctorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Doctor has been successfully added! ')
            return redirect('staff-home')
    else:
        form = DoctorCreationForm()
        return render(request, 'users/doctor_create.html', {'form': form})


def doctor_update(request,pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorUpdationForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Doctor has been successfully updated! ')
            return redirect('doctor-list')
    else:
        form = DoctorUpdationForm(instance=doctor)
    return render(request, 'users/doctor_update.html', {'form': form})


class DoctorListView(ListView):
    model = Doctor
    template_name = 'users/doctor_list.html'
    context_object_name = 'doctors'


def appointment_status(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentStatusForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, f'status has been changed')
            return redirect('staff-home')
    else:
        form = AppointmentStatusForm(instance=appointment)
    return render(request, 'users/appointment_status.html', {'form': form})

# def login_view(request):
#     form = LoginForm(request.POST or None)
#     msg = None
#     if request.method == 'POST':
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None and user.is_customer:
#                 login(request, user)
#                 return redirect('customer')
#             elif user is not None and user.is_vendor:
#                 login(request, user)
#                 return redirect('vendor')
#             else:
#                 msg= 'invalid credentials'
#         else:
#             msg = 'error validating form'
#     return render(request, 'users/login.html', {'form': form, 'msg': msg})
