import django_tables2 as tables
from users.models import User, Doctor


class UserTable(tables.Table):
    class Meta:
        model = User
        template_name = "django_tables2/bootstrap.html"
        fields = ('username', 'email', 'is_staff', 'is_patient')


class DoctorTable(tables.Table):
    class Meta:
        model = Doctor
        template_name = "django_tables2/bootstrap.html"
        fields = ('doctor_name', 'specialization')
