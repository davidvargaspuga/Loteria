from django.db import models

# Create your models here.

class Card(models.Model):
      """ A loteria card with 4 rows and 4 cols """
      created_on = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return "Card: " + str(self.id) + ", " + str(created_on)
      
class Row(models.Model):
      """ Each property is a column on a loteria card, should have 4 rows per card """
      first_val= models.CharField(max_length=3)
      second_val = models.CharField(max_length=3)
      third_val = models.CharField(max_length=3)
      fourth_val = models.CharField(max_length=3)
      card = models.ForeignKey(
            'Card',
            on_delete=models.CASCADE,
            related_name='rows')
      
      def __str__(self):
            return self.first_val + " " + self.second_val + " " + self.third_val + " " + self.fourth_val