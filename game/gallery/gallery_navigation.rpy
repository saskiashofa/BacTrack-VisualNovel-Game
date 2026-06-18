screen gallery_navigation:
    vbox:
        spacing 20
        xoffset -100

        imagebutton auto "gui/button/gallerybutton1_%s.png"  action ShowMenu("galleryA")

        imagebutton auto "gui/button/return_%s.png"  action Return() yoffset -180 xoffset 1300
