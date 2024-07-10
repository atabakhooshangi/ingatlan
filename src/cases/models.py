# from django.contrib.auth.models import User
# from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
#
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=15)
#     profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
#     bio = models.TextField(null=True, blank=True)
#
#     def __str__(self):
#         return self.user.username
#
#
# class Flat(models.Model):
#     owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='flats')
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
#     max_guests = models.PositiveIntegerField()
#     number_of_rooms = models.PositiveIntegerField()
#     availability_start_date = models.DateField()
#     availability_end_date = models.DateField()
#
#     def __str__(self):
#         return self.title
#
#
# class Reservation(models.Model):
#     flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='reservations')
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reservations')
#     start_date = models.DateField()
#     end_date = models.DateField()
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#
#     def __str__(self):
#         return f'Reservation {self.id} for {self.flat.title} by {self.user.user.username}'
#
#
# class Review(models.Model):
#     flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='reviews')
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews')
#     rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
#     comment = models.TextField()
#     date_posted = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'Review {self.id} for {self.flat.title} by {self.user.user.username}'
#
#
# class Message(models.Model):
#     sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sent_messages')
#     recipient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_messages')
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'Message {self.id} from {self.sender.user.username} to {self.recipient.user.username}'
