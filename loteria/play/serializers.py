"""
Form the JSON that we need
"""
from random import sample
from rest_framework import serializers
from play.models import Row, Card

def card_data(card):
      """ populates card with 4 rows of random data """
      first_col = sample(range(1, 16), k=4)
      second_col = sample(range(16, 31), k=4)
      third_col = sample(range(31, 46), k=4)
      fourth_col = sample(range(46, 61), k=4)

      for _ in range(4):
            first_val = first_col.pop()
            second_val = second_col.pop()
            third_val = third_col.pop()
            fourth_val = fourth_col.pop()
            row = Row.objects.create(first_val=first_val, second_val=second_val, third_val=
                                    third_val, fourth_val=fourth_val, card=card)
            row.save()

class CardSerializer(serializers.ModelSerializer):
      """ card JSON """
      class Meta:
            model = Card
            fields = ['id', 'created_on', 'rows']
            depth = 1
      
      def create(self, validated_data):
            card = Card.objects.create(**validated_data)
            card_data(card)
            card.save()
            return card

      def to_representation(self, instance):
            """ Get rid of excess data, makes it easier to consume on the client """
            ret = super().to_representation(instance)
            for row in ret['rows']:
                  row.pop('card')
                  row.pop('id')
            return ret