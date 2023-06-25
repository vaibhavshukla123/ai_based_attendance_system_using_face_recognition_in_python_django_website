import django_filters
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput

from .models import Attendance

class AttendanceFilter(django_filters.FilterSet):
    class Meta:
        model = Attendance
        fields = '__all__'
        exclude = ['Faculty_Name', 'status','branch','section','time']