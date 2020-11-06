from django.db import models
gender=(
    ("male","Male"),
    ("female","Female"),
)

STATUS=(
    ("Available","Available"),
    ("Not_Available","Not_Available"),

)

# Create your models here.
class Health_Professional_Account(models.Model):
    Health_Professional_Id = models.AutoField(primary_key=True)
    Full_Name=models.CharField(max_length=100, default="")
    First_Name=models.CharField(max_length=100, default="")
    Last_Name=models.CharField(max_length=100, default="")
    Email=models.CharField(max_length=100, default="")
    Username=models.CharField(max_length=100, default="")
    Gender=models.CharField(max_length=100, choices=gender,default="male")
    Date_of_Birth=models.CharField(max_length=200, default="")
    Password=models.CharField(max_length=3000, default="")
    Degree=models.CharField(max_length=200, default="")
    Affiliation=models.CharField(max_length=200, default="")
    Bio=models.TextField(default="")
    Street_Address=models.CharField(max_length=500, default="")
    City=models.CharField(max_length=500, default="")
    State=models.CharField(max_length=500, default="")
    Country=models.CharField(max_length=500, default="")
    Location=models.CharField(max_length=500, default="")
    Role=models.CharField(max_length=100,default="earhealthprofessional")
    Status=models.CharField(max_length=100, choices=STATUS,default="Available")
    
   
    Mobile_Number = models.CharField(max_length=200, default="")
    Email_Verification_Code = models.CharField(max_length=200, default="")
    OTP_Verification = models.CharField(max_length=200, default="12345")
    Doctor_rating = models.IntegerField(default=0)
    Doctor_rating_Count = models.IntegerField(default=0)




    def __str__(self):
        return self.Full_Name

