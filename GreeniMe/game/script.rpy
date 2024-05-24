# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define r = Character(name="Reyna", image="")

label start:
    #scene bg
    show reyna  
    "As the sun painted the city in warm shades, a small child was running along the house, helping her parents to pack"
    pause 0.6
    "Meet Reyna, a 10 year old child preparing to move to her Aunt's house, in a small town near the edges of Elmwood trail"
    pause 0.6
    "But her Aunt isn't what meets the eye. Aunt Camilla is a soul loved by fairies"
    pause 0.6
    "She goes on adventures to meet her fairy friends during the winter solstice"
    pause 0.6
    "Reyna wishes to accompany her aunt to meet the fairies this winter solstice"
    pause 0.6
    "But, to do that Reyna first needs to increase her nature affinity"
    pause 0.6
    "This can be done by being sustainable. But Reyna isn't sure what it means to be sustainable"
    pause 0.6
    "Are you willing to help Reyna understand sustainability and meet the fairies?"
    menu:
        "yes!":
            jump scene1
        "no":
            return
        
    
