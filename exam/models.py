from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return  self.name


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

# on_delete = CASCADE , SET_NULL , PROTECT->XAVSIZLIKGA

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class Subject(models.Model):
    name = models.CharField(max_length=255)
    group = models.OneToOneField(Group, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Exam(models.Model):
    name = models.CharField(max_length=255)
    time = models.DateTimeField(auto_created=True)
    subject = models.OneToOneField(Subject, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name},{self.time}"

class Question(models.Model):
    name = models.CharField(max_length=255)
    exam = models.OneToOneField(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Option(models.Model):
    name = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    question= models.OneToOneField(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.is_correct}"


class Price(models.Model):
    name = models.CharField(max_length=255)
    option = models.OneToOneField(Option,  on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"