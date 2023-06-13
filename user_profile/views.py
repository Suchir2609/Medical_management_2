from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Account
from users.forms import ProfileUpdateForm, AccountUpdateForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from fuzzywuzzy import fuzz, process
from users.models import User, Doctor
from django_tables2 import SingleTableView, SingleTableMixin
from .tables import UserTable, DoctorTable


def profile(request):
    pfile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your Account has been successfully updated! ')
            return redirect('patient-profile')
    else:
        p_form = ProfileUpdateForm()
    context = {'pfile': pfile, 'p_form':p_form}

    return render(request, 'users/patient_profile.html', context)


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    fields = ['patient', 'bill', 'status']
    template_name = 'users/account_create.html'
    success_url = '/staff_home'


class AccountListView(ListView):
    model = Account
    template_name = 'users/accounts.html'
    context_object_name = 'accounts'


def account_update(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account has been successfully updated! ')
            return redirect('patient-home')
    else:
        form = AccountUpdateForm(instance=account)
    return render(request, 'users/account_update.html', {'form': form})


# def fuzzy_search(query):
#     results = []
#     objects = Profile.objects.all()
#
#     for object in objects:
#         matches = find_near_matches(query,object.gender, max_substitutions=5,max_insertions=5,max_deletions=5)
#         if matches:
#             results.append(object)
#
#         return results
#
#
# def search(request):
#     query = request.GET.get('question')
#     results = fuzzy_search(query)
#
#     return render(request, 'users/profile_search.html', {'results': results})


def profile_search(request):
    searched_profile = request.GET.get('query')
    # choices = User.objects.all()
    choices = Profile.objects.all()


    if searched_profile:
        patients = process.extract(searched_profile, choices, scorer=fuzz.token_sort_ratio, limit=10)
        patientss = [patient[0] for patient in patients]

    context = {'searched_profile': searched_profile, 'patientss': patientss}

    return render(request, 'users/profile_search.html', context)


class UserListView(SingleTableView):
    model = User
    table_class = UserTable
    template_name = 'users/user_tables.html'


class DoctorListView(SingleTableView):
    model = Doctor
    table_class = DoctorTable
    template_name = 'users/doctor_list.html'

# def doctor_table(request):
#     queryset = Doctor.objects.all()
#     table = DoctorTable(queryset)
#     return render(request, 'users/doctor_list.html', {'table': table})
