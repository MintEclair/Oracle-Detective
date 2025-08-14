# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Dodona = Character('Dodona', color="#87d1ff")
define Howard = Character('Howard', color="#9e9e9e")
define Amber = Character('Amber', color="#ffb070")
define Perfume = Character('perfume')
define Book = Character('book')
define Hat = Character('hat')
define tarot = Character('tarot')

image backstage = "images/backstage.png"

transform half_size: 
    zoom 0.5 #adjust as required

# The game starts here.

label start:
    play music "audio/jazzy.mp3" fadein 1.0 volume 0.5
    scene backstage
    with fade
    show dodona at half_size 
    "Dodona" "It's going to be another exciting night at Oracle's Alley!"
    show dodona at half_size 
    "Dodona" "Charles is hard at work pouring the drinks, Louis is getting ready to play some fantastic tunes, and Howard..."
    show dodona at half_size 
    "Dodona" "..."
    show dodona at half_size 
    "Dodona" "...hopefully he doesn't come barging in asking for another ice tray to be remade..."
    show dodona at half_size 
    "Dodona" "MOCKUP OF OBJECT INTERACTIONS TIME!!!"
    show perfume at half_size
    "Dodona" "Perfume Bottle - Gotta smell nice for the show! This fancy bottle cost me a fortune...but it was worth it."
    show book at half_size
    hide perfume
    "Dodona" "Book of Magic - My trusty lady's Grimoire! Full of all my spells and incantations...I've been keeping tabs on ice magic because Howard keeps dropping ice cubes..."
    show tarot at half_size 
    hide book
    "Dodona" "Tarot Cards - My tarot cards, it's what people come to see! Nice to have a place where I can practice my divination...amongst my other magic."
    show hat at half_size
    hide tarot
    "Dodona" "Hat - My trusty hat! It adds allure and charisma! Perhaps in another world, it could provide more than that."
    show dodona
    hide hat
    "Dodona" "Thank you for a mockup of the object interactions. More to come in the future-stay tuned. Back to our regularly scheduled program!"
    "KNOCK KNOCK KNOCK"
    show howard at half_size, right 
    "Howard" "MISS DODONA!!! WE HAVE A PROBLEM"
    "Dodona" "(Here he is again...asking me to make him another ice tray...)"
    "Dodona" "HOWARD, sweetie, you gotta learn to stop dropping the ice. I'll make another for you but-"
    "Howard" "Miss Dodon...uh...this isn't about an ice tray. Can I speak to you privately for a minute?"
    "Dodona" "Curious..."
    "Dodona" "Sure!"
    "Howard Walks in."
    "Howard" "Miss Dodona, there's a private eye here who wants to speak to you."
    "Dodona" "This...isn't the best thing that's happened today. What do they want?"
    "Howard" "No clue, miss, but I'm hoping she's not here to shut us down-"
    "Dodona" "What do you mean, she?"
    "Howard" "That's what I thought, too! But when I told them I was surprised they sent a woman...she threatened to kick my ass..."
    "Dodona" "Interesting. Let her in, but leave us alone, Howard."
    hide howard
    show amber at half_size, right
    "Howard leaves, and in exchnage, a sutied woman walks in."
    "Amber" "Greetings, Miss Dodona, a pleasure to be in the presence of such a fine lady. My name is Amber Hart, private eye."
    "Dodona" "(Her choice of words indicates a hint of formality, but her tone reeks of brashness. Her tomboyish nature is...rather cute.)"
    "Dodona" "Greetings to you as well, Miss Hart, what brings you to my fine corner?"
    "Amber" "Look, little lady, I know what you're thinking. I ain't here to shut you down, I'm here because I think we could help each other out."
    "Dodona" "In what way?"
    "Amber" "No disrespect to your wonderful establishment, but I couldn't help notice some very colorful clientele frequent this place. Would you say that's true?"
    "Dodona" "(I know what she's implying, but I won't give up any information about my clientele so easily.)"
    "Dodona" "I understand not everyone who is here to seek a fortune comes from clean backgrounds, but I will say they trust me for a good reason. I don't blab about other people's secrets and that's that."
    "Amber" "Okay, I understand, but god damn, you're making my job so much harder, tuts. I thought you would be easy since you seem like such a relaxed lady."
    "Dodona" "(EASY?! Oh, this bitch-)"
    "Dodona" "Unless something bad is going to happen, or if someone is going to die, or if another plans to disturb my establishment, my opinions remain grounded."
    "Amber" "Alright, look. Let's cut a deal, here. If you give me the information I need to know, then maybe I won't go to the police and have this speakeasy that's also serving booze shut down."
    "Dodona" "Hm. Good maneuver. Puts me in between the devil and the deep blue sea, here..."
    "Dodona" "Alright, what do you wanna know?"
    "Amber" "In case you already aren't aware, the city of Portallis is facing a huge problem with mobsters and other occultists running around and causing havoc. My job has been getting intel on how to stop them and hopefully bring peace back to our city. Long story short I-"
    "Dodona" "She drones on and on for what feels like a century. Trust me, I'd rather experience another century than listen to things I already know."
    "Dodona" "I've been alive for well over 80 years, and I'll probably continue to keep living for even longer, so OF COURSE I already know what's been happening in the world around me. How could I not?"
    "Amber" "Oh my apologies, miss, I seem to be boring you."
    "Dodona" "Apology accepted, but just tell me what I don't already know."
    "Amber" "Alright, I guess. Basically, there's someone here who has some deep connections with the Mafia that runs this city. Al Wilson. Based on what I've seen, he frequents this place a lot, and I'm starting to suspect other shady characters are here too."
    "Dodona" "Al Wilson. He's one of my regulars and frequently seeks tarot readings from me. He usually keeps his personal life close to his chest..."
    "Dodona" "I actually have an appointment with him."
    "Dodona" "(I look at the time and see it's well past our appointment date.)"
    "Dodona" "I'm very sorry, but it seems like we have an upcoming appointment together. I hate to cut our lovely chat short, but my clients deserve punctuality. "
    "Amber" "Oh, come on! I think he can handle you being late for once!"
    "Dodona" "I'm sorry, but I'm afraid I must leave and put this conversation away for another time. We can continue talking after I'm done."
    "Amber" "Fine. But you can't stop me from staying for a while. I'll admit, been a long night, and I could use a drink on the house...to help me observe, of course."
    "Dodona" "Do as you wish, but don't expect Charles to give you any free drinks just because you're a pretty girl and a fancy detective."
    "Amber" "Warms my heart to hear you think I'm pretty, tuts!"



    


    return
