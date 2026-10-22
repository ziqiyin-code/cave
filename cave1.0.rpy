# 游戏的脚本可置于此文件中。

#remerber ctrl S to save o_o

# 在游戏初始化时，定义一个 Python 函数。它相当于在记录本上写下：“现在是谁在说话”
init python:
    def active(event, name, interact=True, **kwargs):
        global current_speaker

        if not interact:
            return

        if event == "begin":
            current_speaker = name

default current_speaker = None
#定义一个旁白，名字是空的
define p = Character(" ",image='pb', callback=active, cb_name='pb')

#这里分别声明了“dsa"三个角色，分别是David、Scott和Alex。这样的操作有助于后面大面积的文字撰写
define d = Character("David",image='David', callback=active, cb_name='d',what_prefix="「",what_suffix="」")
define s = Character("Scott",image='Scott', callback=active, cb_name='s',what_prefix="「",what_suffix="」")
define a = Character("Alex",image='Alex', callback=active, cb_name='a',what_prefix="「",what_suffix="」")


define flag = 0
#这个游戏的画面只有1920x1080大小 这里的代码是图片“Cover”的路径 zoom控制显示的大小 x and yanchor控制图片的锚点位置 xpos和ypos控制图片的显示位置
image Cover:
    "images/Cover.png"
    zoom 0.35
#这里呼应上面写的函数 标记谁在说话谁变亮 其他人变暗
image David:
    ConditionSwitch(
        "current_speaker == 'd'", "images/David.png",
        "True", im.MatrixColor(
            "images/David.png",
            im.matrix.saturation(0.4) * im.matrix.brightness(-0.2)
        )
    )
    zoom 0.75
    xanchor 0.5
    yanchor 0.5
    xpos 1433
    ypos 716

image Scott:
    ConditionSwitch(
        "current_speaker == 's'", "images/Scott.png",
        "True", im.MatrixColor(
            "images/Scott.png",
            im.matrix.saturation(0.4) * im.matrix.brightness(-0.2)
        )
    )
    zoom 0.75
    xanchor 0.5
    yanchor 0.5
    xpos 1433
    ypos 716

image Alex:
    ConditionSwitch(
        "current_speaker == 'a'", "images/Alex.png",
        "True", im.MatrixColor(
            "images/Alex.png",
            im.matrix.saturation(0.4) * im.matrix.brightness(-0.2)
        )
    )
    zoom 0.75
    xanchor 0.5
    yanchor 0.5
    xpos 1433
    ypos 716

image catfish_shadow = "images/catfish_shadow.png"
#label是游戏的开始点，游戏从这里开始运行。label后面跟着的名字是这个标签的名字，start是Ren'Py默认的游戏开始标签。
label start:
    # scene是覆盖 show是显示 一个用作背景图 一个用于立绘 with是转场效果 fade是淡入淡出 dissolve是溶解
    scene Cover
    with fade

    window hide

    
    play sound "audio/飞溅.mp3"

    # 黑影从右向左快速掠过。
    show catfish_shadow:
        zoom 0.5

        # 以图片中心定位，垂直位置在画面中间。
        anchor (0.5, 0.5)
        ypos 540

        # 起点在屏幕右侧外面。
        xpos 2400

        # 用 1 秒匀速移动到屏幕左侧外面。
        linear 1 xpos -500

    # 等待移动完成。
    $ renpy.pause(2, hard=True)

    # 移出画面后，清理这张图片。
    hide catfish_shadow
    
   

    play sound "audio/穿刺.mp3"
    hide catfish_shadow

  
    $ renpy.pause(1, hard=True)

    show David:
        xpos 1433-500
    with dissolve
    d "Hey! I hit it!"
    
    show Scott
    with dissolve
    s "Hey, quick! Gotta stop it!"
   
    show Alex:
        xpos 500
    with dissolve
    a "No way! It's too big. We're gonna get knocked flying!"

    # 第一次询问玩家是否追赶

    menu:
        "What do you want to do?"

        "I wanna try":
            jump chase_scene

        "I don't wanna chase it":
            call solo_character("Scott")
            s "Are you sure? We can still catch it!"

    call clear_characters
    p "The catfish thrashes at the surface, scattering water around us."
    call solo_character("Scott")
    s "We didn't come all this way for nothing."
    call solo_character("Alex")
    a "Look at the size of it. What if it pulls us in?"             

    # 第一次不追，听完劝说后，进入第二次询问。
    menu:
        "Chase it?"

        "Okay, let's try":
            jump chase_scene

        "No, it's too dangerous":
            call solo_character("Scott")
            s "It's getting away! This is our last chance!"
    call clear_characters
    p "For a moment, nobody moves."
    p "The ripples spread out. The fish is slipping farther away."
    call solo_character("Scott")
    s "If we're going, we need to go now."
    # 第二次仍然不追，进入最后一次询问。
    menu:
        "One last chance. What do you want to do?"

        "Fine! Let's chase it":
            jump chase_scene

        "No. Let it go":
            jump escape_ending



# 注意：下面的 label 顶格写，与 label start: 对齐。
label chase_scene:
    call solo_character("Alex")
    a "It's about 200 pounds, right? Are we just gonna let it get away?"

    # 在这里继续写追赶剧情。
    "We race after it."

    return


label escape_ending:

    "It feels like we avoided something..."
    "Ending 1: The Escape"

    return
   
    
label solo_character(sprite):

    hide David
    hide Scott
    hide Alex

    show expression sprite:
        xpos 960

    with dissolve

    # 回到调用的位置，继续后面的台词。
    return

# 清空人物立绘，保留背景。
label clear_characters:

    hide David
    hide Scott
    hide Alex

    with dissolve
    return
    # 此处为游戏结尾。
  
   
