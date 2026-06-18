init python:
    g = Gallery()

    g.button("pg1_1")
    g.condition("True")
    g.image("room")

    g.button("pg1_2")
    g.condition("True")
    g.image("desa")

    g.button("pg1_3")
    g.condition("True")
    g.image("lab")

    g.button("pg1_4")
    g.condition("True")
    g.image("kebunvirus")

    g.button("pg1_5")
    g.condition("True")
    g.image("kebunsehat")

    g.button("pg1_6")
    g.condition("True")
    g.image("rumahwarga")

    g.button("pg1_7")
    g.condition("True")
    g.image("good")

    g.button("pg1_8")
    g.condition("True")
    g.image("bad")

    g.button("pg1_9")
    g.condition("True")
    g.image("map")


screen galleryA():
    tag menu

    add "gui/gallery.png"

    hbox:
        yalign 0.5
        xalign 0.5

        use gallery_navigation

        grid 3 3:
            spacing 25

            add g.make_button("pg1_1", Transform("room", xysize=(260, 145)), locked="CGs/preview/locked.png")
            add g.make_button("pg1_2", Transform("desa", xysize=(260, 145)), locked="CGs/preview/locked.png")
            add g.make_button("pg1_3", Transform("lab", xysize=(260, 145)), locked="CGs/preview/locked.png")

            add g.make_button("pg1_4", Transform("kebunvirus", xysize=(260, 145)), locked="CGs/preview/locked.png")
            add g.make_button("pg1_5", Transform("kebunsehat", xysize=(260, 145)), locked="CGs/preview/locked.png")
            add g.make_button("pg1_6", Transform("rumahwarga", xysize=(260, 145)), locked="CGs/preview/locked.png")

            add g.make_button("pg1_7", Transform("good", xysize=(260, 145)), locked="CGs/preview/locked.png")
            add g.make_button("pg1_8", Transform("bad", xysize=(260, 145)), locked="CGs/preview/locked.png")
            add g.make_button("pg1_9", Transform("map", xysize=(260, 145)), locked="CGs/preview/locked.png")