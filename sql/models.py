from django.db import models

# Create your models here.
class Visits(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_email = models.CharField(max_length=50)
    student_id = models.IntegerField()
    #tags = models.CharField(max_length=50)
    classification = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    care_unit = models.CharField(max_length=50)
    services = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    check_in_date = models.DateField()
    check_in_time = models.TimeField()
    check_out_date = models.DateField()
    check_out_time = models.TimeField()
    staff_name = models.CharField(max_length=50)
    staff_id = models.CharField(max_length=50)
    staff_email = models.CharField(max_length=50)


class Demographics(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_email = models.CharField(max_length=50)
    student_id = models.IntegerField()
    student_alt_id = models.CharField(max_length=50)
    classification = models.CharField(max_length=50)
    cumulative_gpa = models.DecimalField(max_digits=5, decimal_places=3)
    assigned_staff = models.CharField(max_length=50)
    cell_phone = models.CharField(max_length=16)
    home_phone = models.CharField(max_length=16)
    gender = models.CharField(max_length=10)
    ethnicity = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=50)
    additional_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    term_credit_hours = models.DecimalField(max_digits=6, decimal_places=3)
    term_gpa = models.DecimalField(max_digits=5, decimal_places=3)
    total_credit_hours_earned = models.DecimalField(max_digits=6, decimal_places=3)
    sms_opt_out = models.BooleanField()
    datetime_opt_out = DateTimeField()
    can_be_sent_messages = models.BooleanField()
    
    
    
class Tags(models.Model):
    student_id = models.IntegerField()
    tag = models.CharField(max_length=50)
    date = models.DateField()

#class Services(models.Model):
#    student_id = models.IntegerField()
#    service = models.CharField(max_length=50)
#    date = models.DateField()
    
class Categories(models.Model):
    student_id = models.IntegerField()
    category = models.CharField(max_length=50)
    date = models.DateField()
