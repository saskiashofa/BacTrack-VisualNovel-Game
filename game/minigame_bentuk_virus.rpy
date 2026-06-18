# =========================================================
# MINIGAME MEMORY - BENTUK-BENTUK VIRUS
# =========================================================

init python:

    all_cards = [
        "batang",
        "peluru",
        "bulat",
        "filamen",
        "polihedral",
        "bakteriofag"
    ]

    ww = 4
    hh = 3
    max_c = 2
    card_size = 48
    max_time = 60
    wait = 0.5
    img_mode = True

    values_list = []

    for fn in renpy.list_files():
        if fn.startswith("images/mini_game/card_") and fn.endswith(".png"):
            name = fn[22:-4]
            renpy.image("card " + name, fn)

    def cards_init():
        global values_list
        values_list = []

        for current_card in all_cards:
            for i in range(0, max_c):
                values_list.append(current_card)

        renpy.random.shuffle(values_list)

        while len(values_list) < ww * hh:
            values_list.append("empty")

screen memo_scr():

    timer 1.0 action If(
        memo_timer > 1,
        SetVariable("memo_timer", memo_timer - 1),
        Jump("memo_game_lose")
    ) repeat True

    add "lab"
    add Solid("#000000") as dark:
        alpha 0.6

    text "Cocokkan Virus-virus Berikut Berdasarkan Bentuknya":
        xalign 0.5
        yalign 0.05
        size 50
        color "#FFFFFF"

    text str(memo_timer):
        xalign 0.5
        yalign 0.15
        size 50
        color "#FFFFFF"

    grid ww hh:
        align (0.5, 0.60)
        spacing 18

        for card in cards_list:
            button:
                xsize 165
                ysize 165
                padding (0, 0)
                background None

                if card["c_value"] == "empty":
                    if img_mode:
                        add "card empty":
                            xysize (165, 165)
                    else:
                        text " " size card_size

                else:
                    if card["c_chosen"]:
                        if img_mode:
                            add "card " + card["c_value"]:
                                xysize (165, 165)
                        else:
                            text card["c_value"] size card_size
                    else:
                        if img_mode:
                            add "card back":
                                xysize (165, 165)
                        else:
                            text "#" size card_size

                action If(
                    card["c_chosen"] or not can_click,
                    None,
                    [
                        Play("sound", "audio/miniklik.ogg"),
                        SetDict(cards_list[card["c_number"]], "c_chosen", True),
                        Return(card["c_number"])
                    ]
                )

screen hasil_memory(judul="", teks="", warna="#C5D83F"):

    modal True

    add "lab"
    add Solid("#000000") as dark:
        alpha 0.6

    frame:
        xalign 0.5
        yalign 0.5
        xsize 850
        ysize 350

        background Solid("#150C0C")

        padding (40, 35)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            text judul:
                xalign 0.5
                size 60
                color warna
                outlines [(3, "#000000", 0, 0)]

            add Solid(warna):
                xalign 0.5
                xsize 400
                ysize 4

            text teks:
                xalign 0.5
                text_align 0.5
                size 35
                color "#F6E3CB"

            textbutton "LANJUT":
                xalign 0.5
                text_size 24
                text_color "#F6E3CB"

                background Solid("#4F0803")
                hover_background Solid(warna)

                padding (40, 12)

                action Return()

label memoria_game:
    
    play music "audio/minigame.mp3" 
    $ cards_init()
    $ cards_list = []

    python:
        for i in range(0, len(values_list)):
            if values_list[i] == "empty":
                cards_list.append({
                    "c_number": i,
                    "c_value": values_list[i],
                    "c_chosen": True
                })
            else:
                cards_list.append({
                    "c_number": i,
                    "c_value": values_list[i],
                    "c_chosen": False
                })

    $ memo_timer = max_time

    show screen memo_scr

    label memo_game_loop:

        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []
        $ turns_left = max_c

        label turns_loop:

            if turns_left > 0:
                $ result = ui.interact()
                $ turned_cards_numbers.append(cards_list[result]["c_number"])
                $ turned_cards_values.append(cards_list[result]["c_value"])
                $ turns_left -= 1
                jump turns_loop

        $ can_click = False

        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):

            $ renpy.pause(wait, hard=True)

            python:
                for i in range(0, len(turned_cards_numbers)):
                    cards_list[turned_cards_numbers[i]]["c_chosen"] = False

        else:
            play sound "audio/ding.ogg"
            $ renpy.pause(wait, hard=True)

            python:
                for i in range(0, len(turned_cards_numbers)):
                    cards_list[turned_cards_numbers[i]]["c_value"] = "empty"

                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump("memo_game_loop")

                renpy.jump("memo_game_win")

        jump memo_game_loop

label memo_game_lose:

    hide screen memo_scr

    play sound "audio/aw.ogg"

    call screen hasil_memory(
        judul="WAKTU HABIS",
        teks="Kamu belum berhasil menemukan semua pasangan bentuk virus.",
        warna="#AA1F1F"
    )

    stop music fadeout 1.0
    jump memoria_game

label memo_game_win:

    hide screen memo_scr

    play sound "audio/tepuk.ogg"

    call screen hasil_memory(
        judul="BERHASIL",
        teks="Kamu berhasil menemukan semua pasangan bentuk virus.",
        warna="#C5D83F"
    )

    return