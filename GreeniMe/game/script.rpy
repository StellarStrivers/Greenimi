# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define r = Character(name="Reyna", image="reyna")

label start:
    scene bg city
    show reyna sad at left
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
    scene bg hall
    "The living room, with sunlight streaming through the windows."
    show reyna sad at right
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
    scene bg stationary
    show reyna sad at left
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
    scene bg kitchen
    show reyna sad at right
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
    scene bg foresty
    show reyna sad at left
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
    scene bg shop
    show reyna sad at right
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
    scene bg aunt_home
    show reyna sad at left
    "Back at their home"
    pause 0.6
    scene bg hall
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
    scene bg clothes
    show reyna sad at right
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
    scene bg bottles
    show reyna sad at left
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
    scene bg dinner_kitchen
    show reyna sad at right
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
    #scene
    show reyna sad at left
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
    scene bg hall
    show reyna sad at right
    "Reyna and her Aunt decide to challenge themselves to reduce their waste to zero"
    pause 0.6
    r "Auntie, can we try to make zero waste? I want to see if we can do it!"
    pause 0.6
    r "We could use reusable containers instead of disposable ones. Auntie says it reduces waste and saves money in the long run. But will it be inconvenient?"
    pause 0.6
    "Or we could buy products that don't have any packaging. Auntie says it's better for the environment, but it might be hard to find everything we need. What should we do?"
    pause 0.5
    menu:
        "Using Reusable Containers":
            jump scene12
        "Buying Package-Free Products":
            jump scene12

label scene12:
    scene bg before_beach
    show reyna sad at left
    "Reyna and her Aunt,along with her friends visited the local beach"
    pause 0.6
    r "I'm so excited to come to the beach with Auntie and my friends! I can't wait to see the turtles. But there are no turtles, just lots and lots of trash everywhere. Auntie, what should I do?"
    pause 0.6
    r "Should I take the initiative and clean the beach so that the next time when I visit the beach I can meet the turtles? But will my friends join hands with me in this cleaning?"
    pause 0.6
    r  "Maybe I can continue to play with my friends; that's the best thing I can do."
    pause 0.5
    menu:
        "1. Cleaning Up the Beach":
            scene bg after_beach
            r "It feels so refreshing to clean this place up!"
            jump scene13
        "2. Continue to Play":
            jump scene13

label scene13:
    scene bg hall
    show reyna sad at right

    "Reyna and her Aunt are in the hall early in the morning"
    pause 0.6
    r "I've been thinking, Auntie. What if we switch to digital versions of newspapers, magazines, and books?"
    pause 0.6
    r "Should we start using digital versions? It's eco-friendly and convenient."
    pause 0.6
    r "Or should we stick with print? Some like the physical feel, but it wastes paper."
    pause 0.6
    menu:
        "1. Go Digital":
            jump scene14
        "2. Stick with Print":
            jump scene14

label scene14:
    scene bg wash
    show reyna sad at left
    "Reyna just washed her own clothes today, now she has a dilemma"
    pause 0.6
    r "I just now washed my clothes as Aunt guided me. What is the next step?"
    pause 0.6
    r "should I start using a clothesline to dry our clothes? But what if it's raining or takes too long?"
    pause 0.6
    r "Or should I stick to using the dryer? It's faster and more convenient."
    pause 0.5
    menu:
        "Use Clothesline":
            jump scene15
        "Use Dryer":
            jump scene15

label scene15:
    scene bg wash
    show reyna sad at right
    "Reyna noticed a lot of water being evicted from the washing machine"
    pause 0.6
    r " But while washing, I noticed enormous amount of water being wasted,  What should I do to overcome this?"
    pause 0.6
    r "I remember Aunty telling me about something like low water using faucets and machines, should we buy those? But how much do they cost anyways?"
    pause 0.6
    r "Or can I pour this water to the little plants along the house?"
    pause 0.6
    menu:
        "1. Install Low Water Faucets and Machines":
            jump scene16
        "2. Water for Plants":
            jump scene16
        
label scene16:

    "Reyna is watching a heavy downpour outside her house"
    pause 0.6
    r "Awwww I can feel the smell of rain and yeah it started to pour all of a sudden. We get enormous water thru rain, right? How should we save this?"
    pause 0.6
    r "Should I install something called rainwater harvesting system with my aunt in our house??"
    pause 0.6
    r "Or can I ask Aunty to mark a common point to use buckets for storing rainwater whenever it rains??"
    pause 0.6
    menu:
        "1. Rainwater Harvesting System":
            jump scene17
        "2. Use Buckets":
            jump scene17


label scene17:
    "Reyna is in her room, trying to draw"
    pause 0.6
    r "I love drawing, but I use so much paper. Auntie, how can I make my hobby more eco-friendly?"
    pause 0.6
    r "Should I start using recycled paper for my drawings? Itʼs better for the environment, even if itʼs a bit more expensive."
    pause 0.6
    r "Or should I continue using the regular paper we already have? Itʼs cheaper and more convenient."
    pause 0.6
    menu:
        "1. Switching to Recycled Paper":
            jump scene18
        "2. Using Regular Paper":
            jump scene18
    
label scene18:
    "Reyna is in her room plannning to decorate it to suit her aesthetics"
    pause 0.6
    r "Auntie, I want to decorate my room. Whatʼs the best way to do it sustainably?"
    pause 0.6
    r  "Should I upcycle old items and turn them into decorations? Itʼs creative and eco-friendly, but it requires more effort and imagination."
    pause 0.6
    r "Or should I buy new decorations from the store? Itʼs easier and faster, but itʼs not as good for the environment."
    pause 0.5
    menu:
        "1. Upcycling Old Items": 
            jump scene19
        "2.  Buying New Decorations":
            jump scene19

label scene19:
    "By the end of the day, aunt gives her another book with fairy stories and she wants to meet fairies "
    pause 0.6
    r "I wish I could meet these fairies someday"
    pause 0.6
    r " could I try casting a magic spell?"
    pause 0.6
    r "Or I could make a wish on a star at night?"

    menu
        "cast a magic spell"
        jump scene20
        "wish on a star"
        jump scene10

label scene20:

    "As Reyna is deeply fascinated by fairies, she asks her aunt how to meet them"
    r " As I become more intrigued by the idea of meeting fairies, I wonder how I can incorporate sustainable 
    living into our quest for magical encounters. What steps can I take to ensure our adventures are eco-friendly?"
    pause 0.6
    r "Should I emphasize the importance of respecting nature's habitat and avoiding any actions that could harm the environment while searching for fairies. It's essential to prioritize conservation and sustainability in our quest."
    pause 0.6
    r " or should I pursue our quest to meet fairies without considering the impact on the environment. After all, fairies are magical beings, and our focus should be solely on finding them, regardless of environmental concerns"
    pause 0.6

    menu
        " Respect nature's habit to meet fairies"
        jump scene21
        " Pursue fairies without regard for nature"
        jump scene21
label scene21
    "Reyna is still on her quest to increase her nature affinity by living sustainably. You can meet Reyna and help her on her quest soon, stay tuned!"
    return
