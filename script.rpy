# Remember to press Ctrl+S to save o_o

# Define a Python function during game initialization. It is like writing in a notebook, "Who is speaking right now?"
init python:
    def active(event, name, interact=True, **kwargs):
        global current_speaker

        if not interact:
            return

        if event == "begin":
            current_speaker = name

default current_speaker = None

define p = Character(None, image='pb', callback=active, cb_name='pb')
define reporter = Character("Reporter")
# Declare the characters here. This makes it easier to write larger sections of dialogue later.
define d = Character("David",image='David', callback=active, cb_name='d')
define s = Character("Scott",image='Scott', callback=active, cb_name='s')
define a = Character("Alex",image='Alex', callback=active, cb_name='a')
define b = Character("Buddy", callback=active, cb_name='b')
define den = Character("Dennis",image='Dennis', callback=active, cb_name='den')
define chief = Character("Coordinator",image='协调员', callback=active, cb_name='chief')

default first_inquiry = None
default search_approach = None
default requested_support = False
default water_review_requested = False
# The game resolution is 1920x1080. This defines the path for the "Cover" image. 
# Zoom controls its size, xanchor and yanchor set its anchor point, and xpos and ypos set its position.
image Cover:
    "images/Cover.png"
    zoom 0.35
image table:
    "images/远景桌子.png"
    zoom 1.15
image rescue:
    "images/救助中.png"
    zoom 1.15
image Scott blanket:
    ConditionSwitch(
        "current_speaker == 's'", "images/毛毯Scott.png",
        "True", Transform(
            "images/毛毯Scott.png",
            matrixcolor=SaturationMatrix(0.4) * BrightnessMatrix(-0.2)
        )
    )
    zoom 0.75
    anchor (0.5, 0.5)
    pos (960, 716)

image backgroundlight:
    "images/场景白.png"
    zoom 1.15
image backgrounddark:
    "images/场景黑.png"
    zoom 1.15
image table2:
    "images/工作台.png"
    zoom 1.15
image wait:
    "images/等待.png"
    zoom 1.15
image cavee:
    "images/黑洞.png"
    zoom 1.15
image hei:
    "images/挽救.png"
    zoom 1.15
image boom:
    "images/彩蛋.png"
    zoom 1.15
image zhuo:
    "images/工作台夜.png"
    zoom 1.15
image hui:
    "images/回归.png"
    zoom 1.15
image backgroundmid:
    "images/场景中.png"
    zoom 1.15
image yiyuan:
    "images/病床上.png"
    zoom 1.15
image qiang:
    "images/医院中景.png"
    zoom 1.15
image dong:
    "images/无光水下.png"
    zoom 1.15
image xia:
    "images/下降.png"
    zoom 1.15
image end:
    "images/希望.png"
    zoom 1.15
image end2:
    "images/幻觉.png"
    zoom 1.15
image guang:
    "images/有光水下.png"
    zoom 1.15

# This uses the function above to highlight the current speaker and dim everyone else. 
# The blue-purple code was shared by a helpful developer online.
image Davidh:
    ConditionSwitch(
        "current_speaker == 'd'", "images/恢复中.png",
        "True", Transform(
            "images/恢复中.png",
            matrixcolor=SaturationMatrix(0.4) * BrightnessMatrix(-0.2)
        )
    )
    zoom 0.75
    xanchor 0.5
    yanchor 0.5
    xpos 1433
    ypos 716

image David:
    ConditionSwitch(
        "current_speaker == 'd'", "images/抓鱼David.png",
        "True", Transform(
            "images/抓鱼David.png",
            matrixcolor=SaturationMatrix(0.4) * BrightnessMatrix(-0.2)
        )
    )
    zoom 0.75
    xanchor 0.5
    yanchor 0.5
    xpos 1433
    ypos 716

image Dennis:
    ConditionSwitch(
        "current_speaker == 'den'", "images/Dennis.png",
        "True", Transform(
            "images/Dennis.png",
            matrixcolor=SaturationMatrix(0.4) * BrightnessMatrix(-0.2)
        )
    )
    zoom 0.75
    xanchor 0.5
    yanchor 0.5
    xpos 1433
    ypos 716

image 协调员:
    ConditionSwitch(
        "current_speaker == 'chief'", "images/协调员.png",
        "True", Transform(
            "images/协调员.png",
            matrixcolor=SaturationMatrix(0.4) * BrightnessMatrix(-0.2)
        )
    )
    zoom 0.75
    xanchor 0.5
    yanchor 0.5
    xpos 1433
    ypos 716

image 手机:
    ConditionSwitch(
        "current_speaker == 'chief'", "images/co手机.png",
        "True", Transform(
            "images/co手机.png",
            matrixcolor=SaturationMatrix(0.4) * BrightnessMatrix(-0.2)
        )
    )
    zoom 0.75
    xanchor 0.5
    yanchor 0.5
    xpos 1433
    ypos 716

image Scott:
    ConditionSwitch(
        "current_speaker == 's'", "images/抓鱼Scott.png",
        "True", Transform(
            "images/抓鱼Scott.png",
            matrixcolor=SaturationMatrix(0.4) * BrightnessMatrix(-0.2)
        )
    )
    zoom 0.65
    xanchor 0.5
    yanchor 0.5
    xpos 1433
    ypos 716

image Alex:
    ConditionSwitch(
        "current_speaker == 'a'", "images/第三个人.png",
        "True", Transform(
            "images/第三个人.png",
            matrixcolor=SaturationMatrix(0.4) * BrightnessMatrix(-0.2)
        )
    )
    zoom 0.75
    xanchor 0.5
    yanchor 0.5
    xpos 1433
    ypos 716

image cood:
    ConditionSwitch(
        "current_speaker == 'chief'", "images/协调员半身.png",
        "True", Transform(
            "images/协调员半身.png",
            matrixcolor=SaturationMatrix(0.4) * BrightnessMatrix(-0.2)
        )
    )
    zoom 1.0
    xanchor 0.5
    yanchor 0.5
    xpos 1433
    ypos 800
image dan:
    ConditionSwitch(
        "current_speaker == 'den'", "images/丹尼斯半身.png",
        "True", Transform(
            "images/丹尼斯半身.png",
            matrixcolor=SaturationMatrix(0.4) * BrightnessMatrix(-0.2)
        )
    )
    zoom 0.9
    xanchor 0.5
    yanchor 0.5
    xpos 400
    ypos 800

image half:
    ConditionSwitch(
        "current_speaker == 's'", "images/Scott半身.png",
        "True", Transform(
            "images/Scott半身.png",
            matrixcolor=SaturationMatrix(0.4) * BrightnessMatrix(-0.2)
        )
    )
    zoom 0.5
    xanchor 0.5
    yanchor 0.5
    xpos 1700
    ypos 750
with dissolve
# A larger xpos moves the image farther right; a larger ypos moves it farther down.
image catfish_shadow = "images/catfish_shadow.png"
# A label marks a point in the game, and the game starts running from here. The name after "label" identifies the label; "start" is Ren'Py's default starting label.
label start:

    
    scene backgroundlight
    with fade
    play sound "audio/脚步.mp3" 
  
    window auto

    p "By the time we reach the lake, a crowd has gathered near the shore."
    p "Wet equipment lies scattered beside the water."

    stop sound
    show Dennis:
        xpos 500
    with dissolve
    den "Buddy. Over here."

    b "What do we know?"
    show 协调员:
        xpos 1433
    with dissolve
    chief "A young man is missing inside the cave."
    chief "His friend made it out. He hasn't."
    chief "Buddy, Dennis. I need you to review the reports and help coordinate the search."

    b "Has anyone spoken to the friend?"

    chief "He's right over there."

    call clear_characters
    play sound "audio/转场.mp3"

    scene wait
    with fade
    show Scott blanket:
        xpos 1433
    with dissolve
    
    p "The young man looks up as we approach."
    p "A blanket is draped over his shoulders, but he is still wearing his soaking-wet wetsuit."
    p "Maybe he'll stay like this until his friend is found."

    b "I'm Buddy. This is Dennis."
    b "Can you tell us what happened?"

    s "Is the new team going in soon?"
    s "David is still in there."

    b "Take your time. Start from the beginning."

    s "Yesterday... there were three of us."
    s "We saw this huge catfish."

    # Call the memory scene; when it ends, execution returns here.
    call fishing_memory

    # The memory scene has ended; show the present-day scene again.
    play sound "audio/转场.mp3"

    scene wait
    with fade

    show Scott blanket:
        xpos 1433
    with dissolve
    s "We came back today. Alex got held up with something. Just David and me"
    s "We thought we could find it again."

    b "And then?"

    s "We lost our way."
    s "We tried different directions."
    s "I found a way out. I thought he would too."

    call clear_characters

    p "Dennis looks toward the water."
    scene rescue
    with fade
    show Dennis:
        xpos 500
    with dissolve

    p "For a moment, neither of us says anything."

    den "We need to understand what happened down there."

    call clear_characters
    # First choice: decide which information to ask about first.
    menu:
        "What should I ask about first?"

        "Ask Scott where they separated.":
            $ first_inquiry = "last_location"

            show Scott blanket:
                xpos 1433
            with dissolve

            b "Where did you last see David?"

            s "Inside the cave. At a place where we couldn't agree which way to go."
            s "I'm sorry. I don't know how to explain where it was."

            b "That's okay. Tell me what you remember seeing."

            call clear_characters
            show expression "images/笔记.png":
                zoom 0.75
                xpos 200
                ypos 150
            with dissolve
            p "Dennis takes out a notebook."

        "Ask what the search teams have found.":
            $ first_inquiry = "search_report"

            show 协调员:
                xpos 1433
            with dissolve

            b "What have the search teams found?"

            chief "Nothing confirmed yet."

            b "Then let's go through what they've checked."

            den "And what they haven't."
            call clear_characters
    # Both choices converge here and continue along the same main story.
    play sound "audio/转场.mp3"
    scene table
    with fade

    p "We spread the available notes out in front of us."
    show expression "images/笔记.png" as notebook:
        zoom 1.0
        xpos 150
        ypos 150
    with dissolve
    den "Let's start with what we actually know."

    p "The search is far from over."

    hide notebook
    with dissolve
  
    jump rescue_assessment

# ==================================================
# First memory: fishing the day before
# ==================================================

label fishing_memory:

    scene Cover
    with fade
    
    play sound "audio/飞溅.mp3"
    window hide


    show catfish_shadow:
        zoom 0.5
        anchor (0.5, 0.5)
        ypos 540
        xpos 2400
        linear 1.0 xpos -500

    $ renpy.pause(1.0, hard=True)

    hide catfish_shadow

    play sound "audio/水花.mp3"

    $ renpy.pause(0.5, hard=True)

    show David:
        xpos 1500
    with dissolve
    d "Hey! I hit it!"
    
    show Scott:
        xpos 960
    with dissolve
    s "Hey, quick! Gotta stop it!"
   
    show Alex:
        xpos 350
    with dissolve
    a "No way! It's too big. We're gonna get knocked flying!"

    d "The catfish thrashes at the surface, scattering water around us."
    
    s "We didn't come all this way for nothing."

    a "Look at the size of it. What if it pulls us in?"
    
    d "For a moment, nobody moves."
    d "Then the shape slips beneath the water."
    d "It's gone."

    s "We could come back tomorrow."

    call clear_characters

    return


# ==================================================
# Section 2: What are we looking for?
# ==================================================

label rescue_assessment:

    scene table2
    with fade
    
    p "Dennis places his notebook beside the search reports."
    p "There are gaps in the notes. Places nobody can account for."

    show cood
    with dissolve
    chief "We've had people searching."
    chief "But so far, no sign of him."

    b "Who has been inside?"

    chief "The divers who were available."
    show dan
    with dissolve
    den "Do any of them have experience searching flooded caves?"

    p "The coordinator pauses."

    chief "Not that I can confirm."

    den "Then we need to be careful about what these reports tell us."
    den "Not finding him doesn't tell us where he is."

    chief "And it doesn't tell us he's alive."
    chief "His air tank wouldn't have lasted this long."
    chief"Too much time has passed..."

    menu:
        "What should we be preparing for?"

        "A rescue. He may still be alive.":
            $ search_approach = "rescue"

            b "Until we know more, we should keep that possibility open."

            chief "I can't promise his family anything."

            b "Neither can I."
            b "But we can tell them what we're doing."

            den "Then let's find out where he could have gone."

        "A recovery. We may already be too late.":
            $ search_approach = "recovery"

            b "We need to prepare for the possibility that he didn't survive."

            chief "That's what some of the team are saying."

            p "Dennis looks down at the notes."

            den "Preparing for that is one thing."
            den "Being certain is another."

            b "Do you think we've missed something?"

            den "I think we haven't ruled everything out."

    
    jump examine_cave_map


# ==================================================
# Section 3: The gaps on the map
# ==================================================
# Don't forget to show the image and character sprites.
label examine_cave_map:

    p "Dennis unfolds a copy of the cave survey."
    # <to 3.0> plays the sound for three seconds and then stops it; the free audio clip I found online can't be trimmed.
    play sound "<to 2.0>audio/纸张.mp3"
    show expression "images/map.png" as cave_map
    with dissolve
    p "I follow the lines with my eyes, trying to connect them to Scott's account."

    b "Can Scott show us where they separated?"
    call clear_characters

    show half
    with dissolve

    s "I can try."

    p "His finger moves across the page, then stops."
    play sound "audio/笔.mp3"
    hide cave_map

    show expression "images/map2.png" as cave_map2
    with dissolve

    hide half
    s "It might have been here."

    show half
    with dissolve
    s "Everything looked different underwater."

    b "Don't guess for our sake."
    b "Tell us which parts you're sure about."

    s "There was a place where we could lift our heads out of the water."
    s "Before we got lost."
    hide cave_map2
    hide half
    call clear_characters

    p "Dennis bends closer to the page."
    show dan
    with dissolve
    den "There are spaces above the water in parts of this cave."
    show expression "images/map2.png" as cave_map2:
        zoom 0.75
        xpos 700
    with dissolve

    b "Could David have reached one?"

    den "Possibly."
    den "It's a long way. His air supply might not have lasted that far."
    den "But if he kept swimming, there's a chance, isn't there?"
    den "If he reached that air pocket, his chances of survival wouldn't be zero."
    call clear_characters
    # The earlier choice only affects the response here.
    if search_approach == "recovery":

        p "I look at the search reports again."
        p "A missing answer is not the same as a final answer."

        b "Then we shouldn't treat this as a recovery yet."

    else:

        b "Then there's somewhere we still need to look."
    hide cave_map2
    show cood
    with dissolve
    chief "A possibility isn't much to send people in on."
    show dan
    with dissolve
    den "It isn't."
    den "That's why we need people who understand this kind of cave."

    b "And someone who can help us understand the water conditions."

    chief "More people means more coordination."
    chief "And more time."

    p "I look from the survey to the lake."
    p "We don't know how much time David has."
    p "We don't even know if he has any."

    menu:
        "What should I do next?"

        "Ask for specialist help now.":
            $ requested_support = True

            b "Start making calls."
            b "We need cave-diving experience and reliable information about the water."

            chief "I'll see who we can reach."

            den "I'll put together what they need to know."

        "Understand the current search before making more calls.":
            $ requested_support = False

            b "First, show us exactly what has been searched."

            p "We go through the reports one by one."
            p "Some locations are marked clearly."
            p "Others are described with only a few uncertain words."

            den "We still can't account for these sections."

            b "Then we need help assessing them."

            chief "I'll start making calls."

            p "I slide the reports back across the table."
            p "They haven't given us the certainty I was looking for."

    jump waiting_for_support


# ==================================================
# Section 4 opening: waiting for a response
# ==================================================

label waiting_for_support:

    call clear_characters
    scene backgrounddark
   
    play sound"<to 2.0>audio/脚步.mp3"
    queue sound"<to 2.0>audio/电话1.mp3"
    # "queue" plays sounds in sequence; using "play" for both would prevent the phone from ringing.
    p "The coordinator steps away to make the calls."
    show Dennis
    if requested_support:
        
        den "Let's have the survey and Scott's account ready."

    else:

        den "At least we can tell them where the gaps are now."

    p "For the first time since arriving, I have nothing to ask."
    p "Only a reply to wait for."

    jump outside_support

# ==================================================
# Section 5: The other end of the phone
# ==================================================

label outside_support:

    call clear_characters

    p "The coordinator returns with a phone in his hand."

    show 手机
    with dissolve

    chief "We've reached someone with cave-diving experience. They're arranging specialist support."

    b "Send them the survey and Scott's account."

    show Dennis:
        xpos 500
    with dissolve

    den "Make clear which parts Scott is certain about."

    p "My eyes return to the possible air pockets."

    b "If David reached one..."

    den "He might still be alive. But we don't know the water level in there."

    chief "We can contact the dam authority."

    b "Could they lower the water?"

    chief "We'll need them to assess whether it's possible."

    den "And how it would affect anyone inside."

    menu:
        "What should I ask for?"

        "Ask them to assess a controlled water-level change.":
            $ water_review_requested = True

            b "Tell them about the air pockets. Ask whether lowering the water could help."

            chief "I'll put you through."

            show expression "images/老电话.png" as phone:
                zoom 0.30
                xpos 800
                ypos 150
            with dissolve

            p "I take the phone."

            b "I'm Buddy. A diver is missing inside the cave."
            b "The survey shows possible air pockets. Could the water level be lowered safely?"

            p "Dennis brings the notes closer as I explain what we know."

            hide phone
            with dissolve

        "Keep the water unchanged while we seek more information.":
            $ water_review_requested = False

            b "Get the current water-level information first. Keep things unchanged for now."

            chief "All right."

            den "We'll review it with the cave-diving specialists."

    jump search_preparation

# ==================================================
# Section 6: Preparing for the search
# ==================================================

label search_preparation:

    hide 手机
    call clear_characters

    p "We spend the next hour checking reports and preparing for the search."

    if water_review_requested:

        show 手机
        with dissolve

        chief "The dam authority is reviewing the request with the specialist team."

        b "Any decision yet?"

        chief "Not yet."

    else:

        show 手机
        with dissolve

        chief "The specialists have the water-level information. No change has been requested."

        b "Keep us updated."

    hide 手机
    with dissolve

    show Dennis:
        xpos 1433
    with dissolve

    den "Scott is still waiting."

    show Scott blanket:
        xpos 500
    with dissolve

    s "Are you going in?"

    b "The cave-diving team is preparing to search."

    s "Do they know where to look?"

    menu:
        "How should I answer him?"

        "Be honest about what we still don't know.":
            b "We have places to check, but we haven't located David."

            s "But you're still looking?"

            b "Yes."

        "Explain how his account has helped.":
            b "Your account has helped the team narrow down where to search."

            s "I wish I could remember more."

            b "Tell us if anything comes back to you."

    s "If I'd stayed with him..."

    b "You got out and called for help."
    b "That's why we're here."

    call clear_characters

    p "Someone calls for Dennis."
    show Dennis
    den "They're ready to brief us."

    jump before_the_search


# ==================================================
# Section 7 opening: before the search
# ==================================================

label before_the_search:
    
    p "We join the specialist team beside the equipment."
    p "The survey is spread out once more."

    show Dennis
    den "They've reviewed the reports."
    den "Now we let them explain the plan."

    p "I step back to make room."

    p "Until now, David has been a name in every conversation."
    p "Somewhere beyond the entrance, there may still be someone waiting to hear his own."

    jump first_search


# ==================================================
# Section 8: The first search
# ==================================================

label first_search:

    call clear_characters

    scene hei
    play sound "audio/水.mp3"
    
    show 协调员
    show Dennis:
        xpos 500
    if water_review_requested:

        chief "The dam authority is still reviewing the request."
        chief "The team will begin searching under the current conditions."

        b "Keep us updated."

    else:

        chief "The specialists will search under the current water conditions."

    den "They'll check the unsearched passages near Scott's mark."
    call clear_characters

    show expression "images/潜水员半身.png" as ban:
        zoom 0.65
        xpos 400
        ypos 200
    with dissolve

    play sound "<to 1.0>audio/气.mp3"
  

    p "The divers finish checking their equipment and move toward the entrance."
    hide ban
    b "Dennis."
    show Dennis
    den "Yeah?"

    b "If they find something..."

    den "They'll tell us."

    p "He waits for me to finish."
    p "I don't."

    hide Dennis
    window hide

    scene cavee
    with dissolve

    play sound "audio/水花2.mp3"

    window auto

    p "The last diver disappears beneath the surface."
    pause 1.0

    jump waiting_on_shore
# ==================================================
# Section 9: Time on shore
# ==================================================

label waiting_on_shore:

    scene backgrounddark
    with dissolve

    play sound"audio/晚上.mp3" fadein 3.0

    show Dennis
    with dissolve

    p "I read the same report twice before noticing."

    den "You've checked it, Buddy."

    p "I put it down."

    call clear_characters

    show Scott blanket:
        xpos 500
    with dissolve

    s "How long has it been?"

    p "I check the time, but Scott speaks before I can answer."

    s "It feels like hours."

    p "His eyes stay on the entrance."

    call clear_characters

    show 协调员:
        xpos 1433
    with dissolve

    chief "Buddy. His family is asking for an update."

    b "Tell them the search is underway."

    chief "They want to know if we think he's still alive."

    if search_approach == "rescue":

        p "Saying he might be alive was easier before I imagined his family hearing it."

    else:

        p "I had prepared myself for the worst."
        p "I hadn't thought about saying it to his family."

    b "Tell them we don't know yet."
    b "But we're still looking."

    chief "All right."

    hide 协调员
    with dissolve

    window hide
    pause 1.0
    window auto

    p "The conversations grow quieter."
    p "I watch the entrance."
    stop sound fadeout 2.0
    jump first_search_returns
# ==================================================
# Section 10: No one found
# ==================================================

label first_search_returns:
    
    show hui
    with fade
    b "They're back."

    p "I move before Dennis does."
    p "Then I see how many people are returning."
    p "The same number that went in."

    show 协调员
    with dissolve
    chief "They haven't found him."

    b "What did they check?"

    p "Dennis marks their route on the survey."

    show Dennis:
        xpos 500
    with dissolve
    den "They searched these passages, but couldn't reach the possible air pocket."
    den "They need to review the route and water levels before trying again."

    chief "We have to consider the risks of another search."

    show Scott blanket
    with dissolve

    s "You're stopping? But he's still in there."

    b "We're working out what the team needs to try again."

    call clear_characters

    menu:
        "What should I do?"

        "Ask the specialist team to assess another search.":
            b "Ask the team what another attempt would require."
            show Dennis
            with dissolve
            den "I'll go through it with them."

        "Ask for a pause before deciding.":
            b "Let the divers rest. Then we'll review the options."
            show 协调员
            with dissolve
            chief "I'll arrange it."

        "Wait... what's that?":
            jump meteor_ending

    jump another_possibility

# ==================================================
# Section 11 opening: Areas not yet checked
# ==================================================

label another_possibility:
    play sound "audio/转场.mp3"
    scene zhuo
    with dissolve
    p "Dennis places the updated survey in front of me."

    show dan
    with dissolve
    den "Look here."
    play sound "<to 1.0>audio/笔.mp3"

    show expression "images/map3.png" as mapp:
        zoom 0.5
        xpos 1000
        ypos 300

    p "He points to a section without a search mark."

    b "They couldn't reach it?"

    den "No. But the team has identified a possible route to this section."
    den "They've asked the dam authority to review whether lowering the water could help."

    hide mapp
    if water_review_requested:
        show cood
        with dissolve
        chief "We've added their findings to your earlier request."

    else:

        chief "With the team's findings, we're requesting a water-level assessment now."

    b "Let us know as soon as they respond."

    jump second_search


# ==================================================
# Section 12: Searching again
# ==================================================

label second_search:

    call clear_characters
    play sound "audio/转场.png"

    scene backgrounddark
    with fade
    p "Later, the coordinator brings us the decision."
    show 协调员
    with dissolve
    chief "The controlled release has been approved."
    chief "The dam authority will coordinate it with the search team."

    p "We wait while the water level is lowered."

    show expression "images/降水位洞口.png" as dong:
        zoom 1.15
    play sound "audio/流水.mp3" fadein 1.5

    p "Once conditions have been checked, the team revises its search plan."
    show cood
    with dissolve
    den "They're going to try the passage they couldn't reach before."

    b "And the air pocket?"

    den "That's where they're hoping to look."
    stop sound fadeout 2.0
    hide cood

    play sound "audio/水花2.mp3"
    p "The team returns to the water."

    window hide
    pause 1.5
    window auto

    scene backgroundmid
    with fade
    show Scott blanket
    with dissolve
    p "Scott sits a short distance away."
    p "This time, he doesn't ask how long it has been."
    p "I sit beside him."

    s "Do you think he knows we're looking?"

    b "I don't know."

    s "I hope he does."

    p "So do I."

    jump news_from_the_cave


# ==================================================
# Section 13: The message
# ==================================================

label news_from_the_cave:

    call clear_characters

    p "Someone calls my name."
    
    show 协调员
    with dissolve
    chief "Buddy."

    p "The coordinator is coming toward us."
    p "I stand."

    b "What happened?"

    chief "One of the divers has surfaced with news."

    show Scott blanket:
        xpos 500
    with dissolve

    p "Scott gets to his feet beside me."

    chief "They've found David."

    p "The next question catches in my throat."

    window hide
    pause 1.0
    window auto

    b "Is he alive?"

    chief "Yes!"
    play sound "audio/黎明.mp3"

    chief "But they're still bringing him out."
    chief "We need to keep the entrance clear."
    hide Scott
    show expression "images/Scott捂脸.png" as wulian:
        zoom 0.75
        xpos 200
        ypos 200
    with dissolve

    p "Scott presses both hands against his face."


    jump rescue_success
# ==================================================
# Section 14: Successful rescue
# ==================================================

label rescue_success:
    hide wulian
    call clear_characters

    p "Later, I find myself standing beside the survey again."
    p "The page is creased where we kept folding it open."

    if search_approach == "recovery":

        p "I remember how close I came to speaking about David in the past tense."
        p "I fold the survey carefully."

    else:

        p "I had kept saying that he might be alive."
        p "Now I can finally stop saying might."

    show 协调员
    with dissolve
    chief "He's on his way to the hospital."

    b "And Scott?"

    chief "Going with him."

    show Dennis:
        xpos 450
    with dissolve
    den "We should pack up."

    b "Yeah. In a minute."

    p "Around us, people begin gathering the equipment."
    p "For the first time all night, I stop watching the entrance."

    scene end
    with fade
    play sound "audio/结局.mp3"
    p "Ending: Brought Back"


    menu:
        "The rescue is over. Would you like to hear David's story?"

        "Continue to the hospital interview.":
            jump hospital_interview

        "End the story here.":
            jump credits


# ==================================================
# Optional epilogue: David's memory
# ==================================================

label hospital_interview:
    stop sound

    scene black
    with fade

    p "Some time later."
    p "A hospital room."
    play sound "audio/转场.mp3"

    scene yiyuan
    with fade

    p "David sits against the pillows."
    p "A reporter beside him."

    reporter "Is it all right if we begin?"

    scene qiang
    with fade
    show Davidh
    with dissolve
    d "Yeah."

    reporter "What do you remember about being alone in the cave?"

    p "David looks down at his hands."

    d "At first, I thought I just had to wait."
    d "Scott would get out."
    d "He'd tell someone."

    call trapped_memory

    scene black
    with fade
    play sound "audio/转场.mp3"

    scene qiang
    with fade
    show Davidh
    with dissolve
    p "The recorder is still running."
    p "David reaches for the water beside his bed."

    reporter "What was it like when they found you?"

    d "I heard someone."
    d "I didn't believe it at first."

    p "He takes a drink."

    d "Then they answered me."

    reporter "Would you go back?"

    p "David sets the cup down."

    call clear_characters

    scene yiyuan
    with fade
    d "No."
    scene end2
    with fade
    play sound "audio/结局一.mp3"
    p "Ending: Lucky to alive"

    jump credits


# ==================================================
# Memory: waiting to be found
# ==================================================

label trapped_memory:

    scene black
    with fade
    play music "audio/水里.mp3"
    play sound "audio/呼吸.mp3" fadein 1.0
    scene dong 
    with fade
  

    p "My head breaks the surface."
    p "I take the mouthpiece out and breathe."

    p "Air."

    p "For a moment, I think I'm safe."
    stop sound fadeout 1.0

    p "Then my feet sink beneath me."
    p "There is nothing to stand on."

    p "I reach for the rock."
    p "My fingers slide off."

    p "I have to keep treading water."
    p "Every time I stop, the water reaches my mouth."

    d "Scott?"
    play sound "audio/水滴.mp3"
    p "I listen."

    d "Scott!"

    p "Only the water answers."
    stop sound fadeout 1.5
    window hide
    pause 1.0
    window auto

    p "My legs begin to ache."
    p "I kick harder, trying to keep my mouth clear."
    p "My breathing gets faster."

    p "There is air above me."
    p "But I can't rest long enough to catch my breath."

    p "I try to count my kicks."
    p "I lose track."

    p "I start again."

    play sound "audio/心跳.png"
    window hide
    pause 1.0
    window auto

    p "At some point, the space above my face seems different."
    p "The ceiling doesn't feel as close."

    show xia
    with fade

    p "I lift my chin."
    p "There seems to be more room to breathe."

    p "That can't be right."

    p "I blink and look again."
    p "I don't trust what I'm seeing anymore."

    p "Maybe I'm imagining it."
    p "Maybe I just need it to be true."

    p "My feet still find nothing."
    p "I keep kicking."

    window hide
    pause 1.0
    window auto

    p "I think about Scott reaching the shore."
    p "I try to picture him telling someone where I am."

    p "Then I remember."
    p "He doesn't know where I am."

    p "I want to close my eyes."
    p "Just for a moment."

    p "Water touches my lips."
    p "I force my legs to move again."

    p "Then I hear something different."

    p "I wait."
    p "I've imagined sounds before."

    scene guang
    with fade
    d "Hello?"
#I couldn’t find a suitable calling sound online, so I recorded it myself and tweaked it a little.
#It ended up sounding more like a ghost, but I tried my best. Hang in there, David.
    play sound "audio/David_call.mp3"
    p "There is another sound."
    p "Closer this time."

    d "I'm here."

    p "A voice answers."

    return
# ==================================================
# Hidden ending: deadline-induced resentment
# ==================================================

label meteor_ending:

    call clear_characters

    b "Wait... what's that?"

    den "A shooting star?"
    scene boom
    # Hide the dialogue window and pause briefly.
    window hide
    pause 0.5

    # Use a white screen to simulate the impact flash, then shake the screen.
    scene expression Solid("#ffffff")
    with vpunch

    pause 0.3

    scene black
    with fade

    window auto

    p "The world has been destroyed."

    pause 0.8

# I'm gonna die T-T
    "Author" "Let it all burn!"
    "Author" "This ending was brought to you by deadline-induced resentment!"

    "Author" "No more caves. No more choices!"
    "Author" "And absolutely no more debugging!"

    p "Secret Ending: Deadline Impact"
    return

# Hide all characters while keeping the background.
label clear_characters:

    hide David
    hide Scott
    hide Alex
    hide Dennis
    hide 协调员
    hide dan
    hide cood

# Hide characters shown using the helper below.
    hide solo_sprite
    hide temporary_picture

    with dissolve
    return


# Show only the specified character.
label solo_character(sprite):

    hide David
    hide Scott
    hide Alex
    hide Dennis
    hide 协调员
    hide temporary_picture
    hide dan
    hide cood

    # Use the solo_sprite tag consistently.
    # The next call replaces the previously shown character.
    show expression sprite as solo_sprite:
        xpos 960

    with dissolve
    return


transform credits_scroll:
    xalign 0.5
    ypos 1080
    linear 10.0 ypos -1600



screen end_credits():

    add Solid("#000000")

    vbox:
        at credits_scroll
        spacing 55
        xsize 1500

        text "CREDITS":
            xalign 0.5
            size 70
            color "#ffffff"

        null height 80

        text "A game by\nZiqi Yin":
            text_align 0.5
            xalign 0.5
            size 42
            color "#ffffff"

        text "Story & Script\nZiqi Yin":
            text_align 0.5
            xalign 0.5
            size 42
            color "#ffffff"

        text "Programming\nZiqi Yin":
            text_align 0.5
            xalign 0.5
            size 42
            color "#ffffff"

        text "Art\nChat GPT & Ziqi Yin":
            text_align 0.5
            xalign 0.5
            size 42
            color "#ffffff"

        text "Music & Sound\npixabay.com & Ziqi Yin":
            text_align 0.5
            xalign 0.5
            size 42
            color "#ffffff"

        null height 80

        text "Special Thanks\nAnna Douglass & 花间莉萝 & 德田秋声 & Renpy & Chat GPT":
            text_align 0.5
            xalign 0.5
            size 42
            color "#ffffff"

        text "Thank you for playing.":
            xalign 0.5
            size 50
            color "#ffffff"



label credits:

    window hide

    stop music fadeout 2.0

    scene black
    with dissolve

    show screen end_credits

    pause 25.0

    hide screen end_credits

    return