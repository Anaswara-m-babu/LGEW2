from django.db import models

# # Create your models here.
class login(models.Model):
    UserId = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=25)
    Password = models.CharField(max_length=25)
    Type = models.CharField(max_length=25)

class Conductor(models.Model):
    UserId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=20, null=True)
    LastName = models.CharField(max_length=20, null=True)
    Contact = models.BigIntegerField(null=True)
    Place = models.CharField(max_length=20,null=True)
    Post = models.CharField(max_length=20, null=True)
    pin = models.BigIntegerField(null=True)
    Bus = models.CharField(max_length=20, null=True)
    lid=models.ForeignKey(login,on_delete=models.CASCADE)

class feedback(models.Model):
    User_id = models.ForeignKey(Passenger,on_delete=models.CASCADE)
    Feedback = models.CharField(max_length=120)
    Date = models.DateField()

class BusRegister(models.Model):
    BusId = models.AutoField(primary_key=True)
    BusRegisterNUmber = models.CharField(max_length=40)
    SeatCapacity = models.IntegerField()
    RouteId = models.IntegerField()

class Passenger(models.Model):
    UserId = models.AutoField(primary_key=True)
    LoginId = models.IntegerField()
    FirstName = models.CharField(max_length=20, null=True)
    LastName = models.CharField(max_length=20, null=True)
    Contact = models.BigIntegerField(null=True)
    Place = models.CharField(max_length=20, null=True)
    Post = models.CharField(max_length=20, null=True)
    pin = models.BigIntegerField(null=True)

class Bank(models.Model):
    BankId = models.autoField(primary_key = True)
    PassangerId = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    AccountNumber = models.IntegerField()
    IFSE_code = models.CharField(max_length=20)
    Amount = models.IntegerField()

class BusLocation(models.Model):
    LocationId = models.IntegerField(primary_key=True)
    BusId = models.ForeignKey(BusRegister, on_delete=models.CASCADE)
    Latitude = models.FloatField()
    Longitude = models.FloatField()

class BusStop(models.Model):
    StopId = models.AutoField(primary_key=True)
    BusId = models.ForeignKey(BusRegister, on_delete=models.CASCADE)
    stop = models.CharField(max_length=30)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    TicketCharge = models.IntegerField()

class Bustime(models.Model):
    TimeId = models.IntegerField(primary_key=True)
    StopId = models.IntegerField()
    Time = models.CharField(max_length=30)
class PassengerBooking(models.Model):
    BookingId=models.IntegerField(Primary_key=True)
    PassengerId=models.IntegerField()
    BusId=models.IntegerField()
    StopId=models.IntegerField()
 class payment(models.Model):
     PayId=models.IntegerField(primary_key=True)
     Passenger_id=models.ForeignKey(Passenger,on_delete=models.CASCADE)
     Amount=models.FloatField()
     Status=models.charField(max_length=110)
     BusId=models.IntegerField()
 class QRcode(models.Model):
     id=models.IntegerField(primary_key=True)
     BusId=models.ForeignKey(BusRegister,on_delete=models.CASCADE)

 class Route(models.Model):
     RouteId=models.IntegerField(primary_key=True)
     StartingStop=models.charField(max_length=50)
     EndingStop=models.charfield(max_length=50)