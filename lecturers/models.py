from django.db import models

class Lecturer(models.Model):
    firstName = models.CharField(max_length=200)
    middleName = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    idNumber = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=10)
    birthDate = models.DateField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName + ' ' + self.surname