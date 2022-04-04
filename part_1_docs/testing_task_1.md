### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # if card.value = 1: ### Needs to have == equality comparison operator instead of = assignment operator ###
      return True
    # else  ### needs colon : ###
      return False
   

  # dif highest_card(self, card1 card2):  ### Spelling mistake 'def' instead of "dif" | should have a comma between card1 and card2 to separate parameters ###
  if card1.value > card2.value:
    return card ### Should return "card1" as that is the parameter passed in ###
  else:
    return card2
  


def cards_total(self, cards):
  # total  ### should be set to 0 initally ###
  for card in cards:
    total += card.value
    return "You have a total of" + total ### incorrect indentation ###

  ### entire function should be indented one more level ###
  
```
