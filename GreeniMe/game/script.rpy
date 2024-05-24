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
        
    
label scene1:

    "The living room, with sunlight streaming through the windows."
    
    r "Auntie, I read about eco-friendly transportation alternatives. Should we consider biking or using public transportation more?"
    pause 0.6
    r "Let's start biking more often for short trips. Auntie says it's good for our health, reduces emissions, and saves money on gas. But what about safety concerns?"

    pause 0.6
    r "Or we could use public transportation for our daily commute. Auntie says it reduces traffic congestion, lowers emissions, and promotes community sustainability. What mode of transportation do you prefer?"
    pause 0.6
    menu:
        "1. Biking":
            jump scene2
        "2. Public Transportation":
            jump scene2

label scene2:
    "It's time to buy school supplies, Reyna went to the store with Aunt Camilla"
    pause 0.7
    r "Aunty, I'm surprised to see so many kinds of pencils in this store. I'm confused about which one to pick."
    pause 0.7
    r "Should I opt for pencils made from recycled materials, refillable pens, and notebooks with recycled paper content? They help reduce waste."
    pause 0.7
    r "Or should I stick with conventional school supplies? They're easier to find."
    pause 0.6
    menu:
        "1. Eco-Friendly School Supplies":
            jump scene3
        "2. Conventional School Supplies":
            jump scene3

label scene3:
    "Reyna and her Aunt decide to start composting but aren't sure what to compost."
    pause 0.6
    r "Auntie, what can we put in the compost bin? I want to make sure we're doing it right."
    pause 0.6
    r "We could put fruit and vegetable scraps in the compost bin. Auntie says they'll break down and turn into rich soil for our garden. But what about other things?"
    pause 0.6
    r "Or we could put paper and cardboard in the compost bin. Auntie says it's good for the environment and reduces waste. But will it smell bad?"
    menu:
        "1. Fruit and Vegetable Scraps":
            jump scene4
        "2. Paper and Cardboard":
            jump scene4

label scene4:
    "Reyna is out on a walk with her Aunt, when she gets a doubt"
    pause 0.6
    r "I want to be good to the planet, but I'm not sure what to do about my bags. What's the best way to carry my stuff, Auntie?"
    pause 0.6
    r "Auntie says we can buy a special bag called a tote bag. It's good for the planet because we can use it again and again. But it means spending money, and I already have lots of plastic bags. What should I do?"
    pause 0.6
    r "Or I could keep using the plastic bags we already have. Auntie says it's good to reuse things, and it saves money. It also makes use of things I already have instead of wasting them. But is it really better for the planet now?"
    pause 0.6
    menu:
        "1.Buying a Tote Bag":
            jump scene5
        "2. Reusing Plastic Bags":
            jump scene5