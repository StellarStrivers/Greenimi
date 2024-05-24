# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define r = Character(name="Reyna", image="")

label start:
    #scene bg
    show reyna  
    "As the sun painted the city in warm shades, a small child was running along the house, helping her parents to pack"
    pause 0.6
    scene bg apartment
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
        "1. Buying a Tote Bag":
            jump scene5
        "2. Reusing Plastic Bags":
            jump scene5

label scene5:
    "On their way, Reyna feels hungry"
    pause 0.6
    r "Auntiee, what's the best way to have a quick snack?"
    pause 0.6
    r "should I eat a pre-packaged snack? It’s quick and convenient, but it usually comes with a lot of plastic waste."
    pause 0.6
    r "Should I make a snack from scratch with fresh ingredients? It’s healthier and has less packaging, but it takes more time."
        menu:
        "1. Eating Packaged Snacks":
            jump scene6
        "2. Making a Homemade Snack":
            jump scene6

label scene6:
    "Back at their home"
    pause 0.6
    r "Auntie, our house is getting chilly. How should we keep warm without using too much energy?"
    pause 0.6
    r "Should we use extra blankets and wear warmer clothes? It’s a good way to save energy, but it might not be as instantly comfortable."
    pause 0.6
    r "Or should we turn up the heater? It will make the house warm quickly, but ituses more energy and increases our carbon footprint."
        menu:
        "1. Using Extra Blankets:":
            jump scene7
        "2. Turning Up the Heater":
            jump scene7

label scene7:
    "As she aproaches the cupboard, she notices there are a lot of un-used clothes"
    pause 0.6
    r "Auntie, we have a lot of clothes we don’t wear anymore. What should we do with them?"

    pause 0.6
    r "Should we donate the clothes to a local charity? It helps others and reduces waste, but it might take some effort to sort and deliver them."
    pause 0.6
    r "Or should we just throw them away? It’s easier and quicker, but it adds to landfill waste."
        menu:
        "1. Donating Clothes:":
            jump scene8
        "2. Throwing Clothes Away":
            jump scene8

label scene8:
    "Reyna found a lot of bottles in her storeroom"
    pause 0.6
    r "I've got so much stuff, Auntie! It's time to get them sorted out. But what should I do with them?"
    pause 0.6
    r "Auntie says we can send our plastic bowtles for recycling. It's good for the environment because they can be turned into new things. But is it worth the effort, and will they really get recycled?"
    pause 0.6
    r "Or I could keep using the plastic bowtles we already have. Auntie says it's good to reuse things, and it saves energy. But what if they end up in the trash anyway?"
    pause 0.5
    menu:
        "Sending Plastic Bottles for Recycling":
            jump scene9
        "Reusing Plastic bottles":
            jump scene9

label scene9:
    "After finishing their dinner, Reyna has the habit of washing her own plates. In the kitchen she finds the light flickering."
    pause 0.6
    r "Auntie, the kitchen light is flickering. What should we do about it?"

    pause 0.6
    r "Should we replace the old bulb with an LED one? It uses less energy and lasts longer, but it's more expensive as you told me while we went for shopping."
    pause 0.6
    r "Or should we use a regular bulb? It’s cheaper initially, but it uses more energy and doesn’t last as long."
        menu:
        "1. Replacing with LED Bulbs":
            jump scene10
        "2. . Using a Regular Bulb":
            jump scene10

label scene10:
    "Reyna after her dinner feels bored. So she asks her aunt to suggest some books but she is finding difficulty in making a better choice"

    pause 0.6
    "Auntie, I want to read a new book. What’s the best way to get one?"

    pause 0.6
    r "Aunty suggests to  borrow a book from the library as it’s free and eco-friendly."

    pause 0.6
    r "Or she asks me to  buy a new book from the store? It’s nice to own my own books, but it uses more resources and money."
    pause 0.5
    menu:
        "1. Borrow a book":
            jump scene11
        "2. Buy a new book":
            jump scene11

label scene11:
    