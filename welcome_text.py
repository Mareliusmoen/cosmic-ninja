def welcome_logo():
    """
    Print the welcome page logo to terminal.

    This function prints the multiline text string representing the welcome
    logo to terminal.

    Note:
        For this function to work in run.py file, I've imported this file
        to make the files functions available to call in run.py.

    """
    print("""
              ______   ______        _______..___  ___.  __    ______
             /      | /  __  \      /       ||   \/   | |  |  /      |
            |  ,----'|  |  |  |    |   (----`|  \  /  | |  | |  ,----'
            |  |     |  |  |  |     \   \    |  |\/|  | |  | |  |
            |  `----.|  `--'  | .----)   |   |  |  |  | |  | |  `----.
             \______| \______/  |_______/    |__|  |__| |__|  \______|
            .__   __.  __  .__   __.        __       ___       __
            |  \ |  | |  | |  \ |  |       |  |     /   \     |  |
            |   \|  | |  | |   \|  |       |  |    /  ^  \    |  |
            |  . `  | |  | |  . `  | .--.  |  |   /  /_\  \   |  |
            |  |\   | |  | |  |\   | |  `--'  |  /  _____  \  |__|
            |__| \__| |__| |__| \__|  \______/  /__/     \__\ (__)    """)


def introduction():
    """
    Print introduction text to terminal.

    This function prints the multiline text string representing the
    introduction to terminal.

    Note:
        For this function to work in run.py file, I've imported this file
        to make the files functions available to call in run.py.

    """
    print("""
           /\                                                 /\.
 _         )( ______________________   ______________________ )(         _
(_)///////(**)______________________> <______________________(**)\\\\\\\(_)
           )(                                                 )(
           \/                                                 \/

"Starshadows: The Cosmic Ninja Chronicles"

In a galaxy far beyond our own, where stars burn brighter than the sharpest
blades and the cosmic winds whisper secrets of ancient arts, the Galactic Ninja
Academy stands as a bastion of excellence in the art of space ninjutsu. You,
a promising young ninja apprentice, have embarked on a journey through the
cosmos to become a legendary cosmic ninja. But beware, for darkness lurks among
the stars, and the shadows cast by celestial bodies hide secrets that can shape
the destiny of entire galaxies. As you step into this cosmic adventure, your
path will be marked by choices that will define your legacy among the stars.
Will you emerge as a hero, a master of the cosmic arts, or will you succumb to
the temptations of power?
Before we embark on this interstellar odyssey, what is your name, young ninja?
""")


def start_message(name):
    """
    Print the start message to terminal.

    This function prints the multiline text string representing the start
    message to terminal, and adds the 'name' that the player input.

    Note:
        For this function to work in run.py file, I've imported this file
        to make the files functions available to call in run.py.

    """
    print(f"""
.______________________________________________________|_._._._._._._._._._.
 \_____________________________________________________|_#_#_#_#_#_#_#_#_#_|
                                                       l
Welcome, {name}...

The cosmic currents have whispered your name among the constellations, and the
stars themselves have awaited your arrival with bated breath. You, {name},
are the starlight's chosen one, destined to carve your legend across the galaxy
as a cosmic ninja.With shurikens of stardust and the cosmos as your canvas, you
shall paint your fate among the celestial tapestry. The galaxies are your
playground, and the very universe your canvas. You will harness the power of
laser ninja-weapons, master the art of stealth, and unravel mysteries as vast
and ancient as the cosmos itself. The stars align in your favor, {name}, as you
embark on this epic adventure through the cosmos. Your choices will echo
through the void and ripple through the fabric of space and time.
Your destiny awaits among the starshadows.
Prepare to journey beyond the stars, {name}, and may your cosmic ninja spirit
burn brighter than a supernova in the night sky. The galaxy is yours to
explore, to protect, and to conquer!""")


def backstory():
    """
    Print the backstory to terminal.

    This function prints the multiline text string representing the
    backstory to terminal.

    Note:
        For this function to work in run.py file, I've imported this file
        to make the files functions available to call in run.py.

    """
    print("""
    Backstory about this super duper cool nunchuck slingingly good story

So the story behind this text based adventure game is my love for a really
cheezy sci-fi story, and let's be honest who doesn't love a ninja with laser-
weapons? Thats what I knew, everybody loves space travelling,
Shuriken throwing, assasinating, powerful Ninjas! I hope you where like me when
you were a kid, running all over the place with sticks and in your imagination
you were the most lethal, awesome and kick-ass NINJA-girl or NINJA-boy.
Please enjoy, have a laugh and remember:
EVERYBODY HAS A LETHAL SPACE-NINJA IN THEM""")

def goodbye_text(name):
    print(f"""
Fairwell, {name}, your cosmic journey comes to a close for now.
Should you ever wish to return to the path of the cosmic ninja, the universe
will be here, ready to embrace your ninja spirit once more. Until then,
may the stars guide your way!""")