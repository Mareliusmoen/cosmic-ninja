# Cosmic Ninja Adventure

This python project is made to give the user a good laugh and hopefully remind them of a childhood filled with imagination, epic stories that filled our minds and took us on amazing adventures in everyday life.
I guess you could say this story is a bit childish, but I believe for a text based adventure game
we all have to find our inner child and use our imagination for it to be engaging since the visual and audiotory stimuli is not very present.
The amazing story itself is created by AI with Chatgpt (https://chat.openai.com/), I gave it my requirements for the story:
- Ninjas wielding laser weapons.
- It's set to space.
- Devided into chapters and the player should get options at the end of each chapter, and depending on the choice made the storyline takes a new direction. Example:
   - Chapter 1 the player chooses option A.
   - The player is then shown chapter 2A because of his/her choice in chapter 1, and is the presented with two new options; A or B.
   - The player chooses option B.
   - Because of this choice the next chapter shown is 3AB, and so the story progresses.

During the construction I asked the AI for the next chapter depending of the previous choices and added any new requirements that I felt would give the story more of a creative and childish feel along the way, in the end there's 16 totally different endings to the game.

## Demo
Link to the live site: https://cosmic-ninja-adventure-b7514defc13d.herokuapp.com/ 
![Shows the page on laptop, desktop, tablet and mobile screen](files/images/ninja-screenshot.png)

## User Stories
This app is created for anyone with a special interest in any of its topics or the text based adventure game genre, among them:
- **Text based adventure game fans,** all of the people that miss the 'good old days' when you had to use your own imagination and nobody talked about game graphics (or if they did it was made up of letters, numbers, symbols and spaces). 
- **Those seeking a trip down memory lane,** anyone who played a computer game in the 80s or early 90s with all it's charm, ingenuity and mindblowing storylines, when people smoked inside, moustaches were the coolest thing for any man (it still is, but whatever..) and everybody looked like George or Elaine from the Seinfeld tv show. For those who want to reminisce about a time without all the grown-up issues of 2023 (or maybe just less of them) and just submerge their mind in epic laser-katana-sword-swinging ninjas!
- **For the new generation that never have to use their imagination anymore,** those that have no imagination because everything is in 4K, 3D with a splash of sorroundsound in their life. This is a great oppertunity to see the humble beginnings of what so many of us love today!
- **For the Ninja-enthusiast,** those that dress up as a ninja for halloween every year withuot exception, those that jumps down from the 2nd floor instead of taking the stairs because the stairs are 'not very ninja'.
- **For those that have litterally seen everything on the world-wide-web,** just those that feel like they have completed 99.9% of the internet and happend to come across this game.

## Strategy
The strategy in developing this text based adventure game was to make a fun and engaging story, where the player felt that the choices they made actually makes a difference in how the story progresses. If the player would play several times he/she/they would have completely different experiences if they made other choices. As a tribute to some of my favourite childhood story-themes I wanted to blend the mystical world of the ninja with space travelling sci-fi, and along the way emphasizing the importance of decicionmaking and the presentation of the story itself.

- **Focus on the narrative,** it was important to create a exciting story with branching narratives, and characters development as the tools to keep the player engaged in the game.
- **Players choice,** I implemented a choice-based system so the player controlled the direction of the story based on their own choices.
- **Thematically on-point,** keeping the cosmic ninja feel along the story we (my friend AI and me) incorporated things like laser katanas, shurikens, intergalactic conflict and cosmic powers.
- **User friendly,** one of the most important things with the game was to make it as user friendly as possible. It can be hard to get anyone used to the grafic-intens game of the 21st century interested or enjoying a text based game, so it had be stream-lined and immersive at the same time as to keep the player engaged.

## Wireframe/Flowchart
![Flowchart of the Cosmic Ninja Adventure Game](files/images/cosmic-ninja-flow-2.png)

## Features
### Welcome screen
Here the user will se a ASCII art 'COSMIC NINJA', and have two choices:
- Read the backstory of the app.
- Start the game.

![Screenshot of the welcome-screen in terminal](files/images/welcome-screen.png)

### Backstory screen
Here the user will read a short text about what I had in mind when I created the app, and just a little bit of explaining how the story came about.
![Screenshot of the backstory-screen in terminal](files/images/backstory-screen.png)

### Introduction and name choice screen
![Screenshot of the introduction- and name choice-screen](files/images/introduction-name-choice-screen.png)

### Wrong input screen
![Screenshot of terminal when player inputs are incorrect example 1](files/images/wrong-input1.png)
![Screenshot of terminal when player inputs are incorrect example 2](files/images/wrong-input2.png)

### Chapter with options
![Screenshot of the chapter and options screen](files/images/chapter-and-options-screen.png)

### Goodbye screen
![Screenshot of terminal when player decides to stop playing](files/images/goodbye-screen.png)

### Background image and favicon image
The back ground image is created by AI for free at https://gencraft.com/, the requirements  I gave the AI was "50 ninjas in space fighting with laser weapons".
It gave me both the background image and the favicon image that is in the same style and color-scheme.

## How to Play

It's very straight forward once the game is running, follow the on-screen instructions to navigate the story, make your own choices, and change the galaxy's destiny while you shape your own destiny as a cosmic ninja.

## Technologies

### Coding languages
- **Python,** used for the terminal application.
- **HTML,** with some inline styling.
- **JavaScript,** in the template from Code Institute to run the terminal app.

### Libraries and packages
- **'os' and 'platform',** for the clear function to work on all operating-
systems.

### Other tools
- **LucidCharts,** to create the flowchart.
- **GitHub,** to host the application source code.
- **VSCode,** to create/edit the source code.
- **Heroku,** to host the application.

## Features left to implement
- Typewriter effect for text to output terminal, want to implement this effect so it looks like the story is being written as you play the game.

## Testing

### Automated testing with Code Institutes Python Linter and autopep8 formatter in VSCode
The only errors that occurs are related to the ASCII art that uses symbols,
letters and spaces to create the art.

### Manual testing
| **Testing description**                              | **Expected action**                                                                                                                                      | **Actual output**                                                                                                                                        | **Result** |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| Game app start                                       | Shows logo + 'read backstory' and 'start game options'                                                                                                   | Shows logo + 'read backstory' and 'start game options'                                                                                                   | Confirmed  |
| Choose to read backstory                             | Show 'backstory' text and option to 'start game'                                                                                                         | Show 'backstory' text and option to 'start game'                                                                                                         | Confirmed  |
| from backstory to start the introduction             | clear the backstory and load introduction text                                                                                                           | clear the backstory and load introduction text                                                                                                           | Confirmed  |
| Enter you name in the input field                    | See introduction text input  printed to terminal                                                                                                         | See introduction text input  printed to terminal                                                                                                         | Confirmed  |
| Loading welcome screen                               | When name is entered and pressed 'enter', clear introduction text and print welcome text (that includes the name you entered) + option to start the game | When name is entered and pressed 'enter', clear introduction text and print welcome text (that includes the name you entered) + option to start the game | Confirmed  |
| Start the game                                       | When entering to start the game it clears the welcome text, prints chapter 1 with 2 options                                                              | When entering to start the game it clears the welcome text, prints chapter 1 with 2 options                                                              | Confirmed  |
| Chapter 2                                            | Clears chapter 1, prints the  correct chapter 2 depending  on which option you chose  in the previous chapter                                            | Clears chapter 1, prints the  correct chapter 2 depending  on which option you chose  in the previous chapter                                            | confirmed  |
| Chapter 3                                            | Clears chapter 2, prints the correct chapter 3 (and the connected 2 options) depending on previous choices of the  options presented to you              | Clears chapter 2, prints the correct chapter 3 (and the connected 2 options) depending on previous choices of the  options presented to you              | Confirmed  |
| Chapter 4                                            | Clears chapter 3, prints the correct chapter 4 (and the connected 2 options) depending on previous choices of the  options presented to you              | Clears chapter 3, prints the correct chapter 4 (and the connected 2 options) depending on previous choices of the  options presented to you              | Confirmed  |
| Chapter 5 (last chapter)                             | Clears chapter 4, prints the correct chapter 5 depending on previous choices of the  options presented to you. + 'play again' option                     | Clears chapter 4, prints the correct chapter 5 depending on previous choices of the  options presented to you. + 'play again' option                     | Confirmed  |
| Quit game If you chose not to play again             | clear chapter 5, print 'thank you for playing' message and exit the game                                                                                 | clear chapter 5, print 'thank you for playing' message and exit the game                                                                                 | Confirmed  |
| Play again If you chose to play again                | clear chapter 5, print logo + + 'read backstory' and 'start game options'. And the game loop has started again                                           | clear chapter 5, print logo + + 'read backstory' and 'start game options'. And the game loop has started again                                           | Confirmed  |
| Incorrect input when  given options in every chapter | Print 'wrong input' message, and reprint input choices.                                                                                                  | Print 'wrong input' message, and reprint input choices.                                                                                                  | Confirmed  |
| Trying to input empty text in name selector          | Show 'wrong name' name message, and ask for a new input                                                                                                  | Show 'wrong name' name message, and ask for a new input                                                                                                  | Confirmed  |

## Bugs
### Problems encountered during the creation-process
- Indentations are hard to keep track of as the while loop gets more and more if elif else with each chapter. **FIX:** Refactor the code and make functions in other .py files to make the overall code easier to read.
- Some ASCII art needed to be tweaked because some of the combination of symbols have a coding attribute and messed with the code (especially backslash which makes indentations). **FIX:** Add spaces after backslashes to prevent them from indenting is one example.
- Did not define the chapters and chapter options as functions but jus declared them as variables, this made them print to console as soon as program started because of the import command. **FIX:** Change all chapter-variables to chapter functions in their appropriate .py files and then call them in the run.py code.
- Problems that the clear command did not work as intende had to change the code to make it work on different operatingsystems. **FIX:** Seems like a macOs problem as it worked correctly on Linux, added more lines to the output terminal in the finished project to prevent scrolling and then the clear command removes all printed text (before when scroll was needed for longer text, only what was visible in the terminal when the clear() command ran was removed).
- Text to long in some chapters to be read in terminal without scrolling, had to reset index.html file back to template default to try again. **FIX** Added extra lines for the output terminal in the HTML file to prevent the need for scrolling within the output terminal. (depending on screensize the user might need to scroll on the webpage itself).
- Struggled to manage a code for the characters to be printed one by one, this was very import for the user experience because certain chapters or text is longer than the 24 lines that are shown in the players terminal, and with out this method of printing there would be no way for the player to know intuitively to scroll up or down to read the entire text. **FIX:** Unsolved and is added to future features.
- Music file will play in preview in vscode, but does not even load in the deployed browser. **FIX:** Added SoundClouds embedded music player.
- Problem with functions in queries.py not working as intended when called in run.py. **FIX:** add ‘return’ in front of input to make the function return the value so the rest of the code can interact with it.

## Unsolved bugs
- Background image is not fully responsive for all screensizes, but this is due the template from Code Institute used for this project (as it is a python-project) and not the code I added to it.

No other bugs found during testing.
## Deployment
### ***Final Deployment to Heroku:***  
  
The project was deployed to [Heroku](https://www.heroku.com) using the below procedure:-    
  
- **Log in to Heroku** or create an account if required.
-
**click** the button labeled **New** from the dashboard in the top right corner, just below the header.
- From the drop-down menu **select "Create new app"**.
- **Enter a unique app name**. I combined my GitHub user name and the game's name with a dash between them (dnlbowers-battleship) for this project.
- Once the web portal shows the green tick to confirm the name is original **select the relevant region.** In my case, I chose Europe as I am in Sweden.
- When happy with your choice of name and that the correct region is selected, **click** on the **"Create app" button**.
- This will bring you to the project "Deploy" tab. From here, navigate to the **settings tab** and scroll down to the **"Config Vars" section**. 
- **Click** the button labelled **"Reveal Config Vars"** and **enter** the **"key" as port**, the **"value" as 8000** and **click** the **"add"** button.
- Scroll down to the **buildpacks section of the settings page** and click the button labeled **" add buildpack," select "Python," and click "Save Changes"**.
- **Repeat step 11 but** this time **add "node.js" instead of python**. 
   -  ***IMPORTANT*** The buildpacks must be in the correct order. If node.js is listed first under this section, you can click on python and drag it upwards to change it to the first buildpack in the list.
- Scroll back to the top of the settings page, and **navigate to the "Deploy" tab.**
- From the deploy tab **select Github as the deployment method**.
- **Confirm** you want to **connect to GitHub**.
- **Search** for the **repository name** and **click** the **connect** button next to the intended repository.
- From the bottom of the deploy page **select your preferred deployment type** by follow one of the below steps:  
   - Clicking either "Enable Automatic Deploys" for automatic deployment when you push updates to Github.  
   - Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment. 

## NOTE
- Please note that some trailing white spaces and 'invalid… ' errors will show up in pep8 linter because of the ASCII art at the beginning of each chapter string.
- Please note I didnt know how to preview my total project (with html and styling) except for deploying, so some comits are trial and error for extra features I wanted in the project connected to the HTML and styling of that HTML to be fixed as I went along. 

## Acknowledgments
- Deployment description in this readme.md file is from dnlbowers and his battleship apps readme.md file; https://github.com/dnlbowers/battleships/tree/main

- Manual testing table created with:
   - Table generator at https://www.tablesgenerator.com/markdown_tables#

- Multiple choice gives multiple choice again inspiration and the occational code snippet:
   - https://www.youtube.com/watch?v=YPFss7hYBmg
   - https://stackoverflow.com/questions/49455318/calling-multiple-functions-based-on-user-selection-in-python
   - https://stackoverflow.com/questions/17166074/most-efficient-way-of-making-an-if-elif-elif-else-statement-when-the-else-is-don
   - https://stackoverflow.com/questions/54608432/how-to-use-while-loops-with-multiple-if-elif-statements
   - https://stackoverflow.com/questions/28443164/compound-if-elif-else-statements-python

- Making the ASCII logo for gamestart page: https://patorjk.com/software/taag/#p=display&h=1&v=1&c=vb&f=Star%20Wars&t=cosmic%0Aninja!%0A%0A%0A

- ASCII art from: https://ascii.co.uk/art/

- Background image generated for free by AI at site: https://gencraft.com/

- Favicon generated for free by AI at site: https://gencraft.com/

- Styling of the display background, positioning of terminal and 'run button'from: https://github.com/dnlbowers/battleships/blob/main/views/layout.html

- How to add the embedded Soundcloud adio player to HTML: https://help.soundcloud.com/hc/en-us/articles/115003568008-Embedding-a-track-or-playlist-#:~:text=Click%20on%20the%20embed%20tab,section%20of%20your%20site
-And the music itself from SoundCloud: https://soundcloud.com/sega-16bit-music/street-fighter-theme-of-chun-li

-**The most important of all,** my good friend AI from Chatgpt that made up this cosmic universe and helped me tell the stories of this young ninja. Link to AI's homepage: https://chat.openai.com/