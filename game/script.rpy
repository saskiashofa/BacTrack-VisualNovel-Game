# Karakter
define y = Character('Nyra', color="#b60909")
define o = Character('Dr. Orion',color="#dd6413")
define a = Character('Ayla', color="#ac7d27")
define n = Character (None)

transform kamar: 
    xalign 0.8
    yalign 0.6
    zoom 0.7
transform kanan: 
    xpos 1.07
    ypos 1.02
    xanchor 1.0
    yanchor 1.0
    zoom 0.5
transform kiri: 
    xpos -0.04
    ypos 1.02
    xanchor 0.0
    yanchor 1.0
    zoom 0.5
transform tengah:
    xalign 0.5
    yalign 0.5
    zoom 0.7

default kebun_unlocked = False
default rumah_unlocked = False
default kesempatan_quiz_lab = 2
default kesempatan_quiz_kebun = 2
default kesempatan_quiz_rumah = 2
            
label start:
    scene black
    with fade
    stop music fadeout 0.5
    window hide
    show expression Movie(size=(1920, 1080), play="images/video/intro.webm") as bg_vid
    with dissolve
    pause 7
    scene black
    with fade
     
    stop music
    jump mainmenu

label mainmenu:

    scene menuu
    with dissolve
    play music "audio/antent.mp3" fadein 1.0

    call screen menu

    stop music fadeout 1.0

label scene: 
    scene room
    with fade

    play music "audio/room.mp3" fadein 1.0

    show nysad at kamar
    y "Aduh... materi virus lagi..."
    y "Makin dibaca makin gak ngerti..."
    y "Kepalaku malah makin pusing..."
    hide nysad

    show nysmile at kamar
    y "Ah, nggak! Aku harus fokus!"
    y "Kalau gini terus, aku nggak bakal paham!"

    hide nysmile

    stop music fadeout 1.5

    # GLITCH START
    window hide
    show expression Movie(size=(1920, 1080), play="images/video/glitch.webm", loop=True) as bg_vid
    with dissolve
    with hpunch
    pause 3

    scene roomeror
    $ quick_menu = True
    window show
    play music "audio/horor.mp3" fadein 1.0
    show nyhah at kamar
    y "Hah?!"
    y "Apa itu barusan...?!"
    y "Layar komputernya... berubah?!"

    y "Desa...? Wabah...?"

    show black:
        alpha 0.4
    with dissolve

    y "Ini bukan berita biasa..."
    y "Eh?! Tubuhku... kenapa?!"
    stop music fadeout 1.0
    hide nyhah

    show black:
        linear 1.0 alpha 1.0

    pause 0.5

    # TELEPORT

    window hide
    show expression Movie(size=(1920, 1080), play="images/video/teleport.webm") as bg_vid
    with dissolve
    pause 13
    jump scene1

label scene1:

    scene desa
    with fade

    stop music fadeout 1.0
    play music "audio/mystery.mp3"

    show nyhah at kamar
    y "...Aku di mana ini?"

    show nyb at kamar
    y "Tempat ini..."
    y "Sepi banget..."

    y "Nggak ada suara... nggak ada orang..."

    y "Apa yang sebenarnya terjadi di sini...?"

    hide nyb
    hide nyhah

    play sound "audio/woosh.ogg"

    show osmile at kiri
    with moveinleft

    o "Kamu akhirnya sadar juga."

    play sound "audio/woosh.ogg"
    show nyhah at kanan
    with moveinright

    y "Hah?!"
    y "Siapa kamu?!"
    hide nyhah
    show nyb at kanan
    o "Tenang."
    o "Aku bukan musuhmu."
    o "Namaku Orion."
    o "Dokter di desa ini."
    hide osmile
    y "Kalau kamu dokter..."
    y "Jawab aku—"

    y "Kemana semua orang?!"

    pause 0.3
    show osrius at kiri
    with dissolve
    o "Mereka tidak menghilang."
    o "Mereka... sedang sekarat karena wabah."

    play sound "audio/shocked.ogg"
    with hpunch

    hide nyb
    show nyhah at kanan
    y "Apa?! Wabah...?"

    o "Ya. Wabah misterius yang disebabkan oleh wirus menyebar dengan sangat cepat."

    y "...Ini sama seperti yang kulihat..."
    y "Di komputerku..."
    hide nyhah

    pause 0.5

    show osrius at kiri
    o "Kalau begitu..."
    o "Kamu memang orang yang kami tunggu."
    show nyb at kanan
    y "Apa maksudmu...?"

    o "Kamu dipanggil ke sini."
    o "Dan waktumu tidak banyak."

    stop music fadeout 1.0
    scene black
    with fade
    stop music fadeout 2.0

    call screen map_screen
    return

label lab:
    stop music fadeout 1.0
    scene lab
    with fade
    
    play music "audio/science.mp3" fadein 1.0 
    show nywow at kanan
    y "Wow.. ini laboratorium?"
    hide nywow
    show osrius at kiri
    o "Ya, ini adalah laboratorium yang aku gunakan selama meneliti wabah virus di desa"
    show nyb at kanan
    y "Semua alat ini... dipakai buat meneliti wabah itu?"
    o "Benar"
    o "Tapi sebelum kita melangkah lebih jauh"
    o "Kamu harus memahami dasar-dasarnya terlebih dahulu"
    o "Tapi sebelum itu, coba kamu cocokkan gambar bentuk virus yang sama."
    
    hide nyb
    hide osrius
    with fade
    window hide
    $ quick_menu = False
    stop music fadeout 0.5

    call memoria_game from _call_memoria_game

    with fade
    $ quick_menu = True
    play music "audio/science.mp3" fadein 1.0 
    window show
    show osmile at kiri
    show nyhppy at kanan

    o "Bagus. Kamu berhasil mencocokkan gambar bentuk virus."
    o "Sekarang kita masuk ke materi virus."

    hide osmile
    hide nyhppy
    with dissolve

label materi_lab:
    with fade 
    pause 1.0 

    show osrius at kiri
    with dissolve
    o "Virus adalah organisme yang sangat kecil, bahkan tidak bisa dilihat tanpa mikroskop elektron"
    o "Virus tidak memiliki struktur sel lengkap, sehingga tidak bisa berkembang biak sendiri."
    show nyb at kanan
    with dissolve
    y "Jadi virus harus menumpang pada makhluk hidup lain?"
    o "Benar. Virus hanya dapat bereplikasi di dalam sel hidup yang disebut sel inang."
    y "Lalu bedanya virus dengan bakteri apa?"
    o "Bakteri adalah makhluk hidup ber-sel satu yang dapat berkembang biak sendiri."
    o "Sedangkan virus tidak memiliki sel lengkap dan harus bergantung pada sel inang."
    y "Berarti bakteri bisa berkembang biak sendiri, tapi virus tidak."
    o "Tepat sekali."
    o "Secara umum, virus memiliki materi genetik berupa DNA atau RNA."
    o "Materi genetik itu dilindungi oleh kapsid, yaitu selubung protein."
    o "Bentuk virus juga bermacam-macam."

    show expression Solid("#000000") as dark:
        alpha 0.6
    with dissolve

    show jenisvirus:
        xalign 0.5
        yalign 0.5
        zoom 1.0
    with dissolve

    o "Perhatikan gambar ini."
    o "Ini adalah beberapa contoh bentuk virus."
    o "Virus memiliki bentuk yang bermacam-macam, seperti batang, bulat, oval (peluru), filamen (benang), polihedral, dan seperti huruf T. "
    o "Bentuk batang, misalnya TMV (Tobacco Mosaic Virus). Bentuk batang dengan ujung oval seperti peluru, misalnya Rhabdovirus. Bentuk bulat, misalnya HIV (Human Immunodeficiency Virus) dan Orthomyxovirus. "
    o "Bentuk filamen (benang), misalnya virus Ebola. Bentuk polihedral, misalnya Adenovirus. Bentuk seperti huruf T, misalnya bakteriofag, yaitu virus yang menyerang bakteri Escherichia coli. "
    o "Salah satu virus yang bentuknya kompleks adalah bakteriofag."
    y "Bakteriofag itu yang bentuknya seperti huruf T?"
    o "Benar. Bakteriofag adalah virus yang menyerang bakteri."

    hide jenisvirus
    hide dark
    with dissolve

    # background gelap transparan
    show expression Solid("#000000") as dark:
        alpha 0.6
    with dissolve

    show virus:
        xalign 0.5
        yalign 0.5
        zoom 1.8
    with dissolve

    o "Sekarang perhatikan struktur bakteriofag."
    o "Bakteriofag memiliki beberapa bagian utama, yaitu kepala, kapsid, materi genetik, leher, ekor, lempeng dasar, dan serabut ekor."
    o "Bagian kepala berisi materi genetik virus."
    o "Materi genetik tersebut dapat berupa DNA atau RNA."
    y "Lalu kapsid itu apa?"

    o "Kapsid adalah selubung protein yang melindungi materi genetik virus."
    o "Bagian leher menghubungkan kepala dengan ekor."
    o "Ekor berperan dalam proses memasukkan materi genetik virus ke dalam sel inang."
    o "Serabut ekor membantu bakteriofag menempel pada permukaan sel inang."
    o "Sementara lempeng dasar membantu proses pelekatan sebelum virus menginfeksi sel."
    y "Jadi struktur bakteriofag berhubungan dengan cara virus menyerang sel inang."
    o "Tepat sekali."

    hide virus
    hide dark
    with dissolve
    
    o "Lanjut ke bagian penting yaitu replikasi virus"
    o "Ada dua cara replikasi virus yaitu daur litik dan lisogenik"

    show expression Solid("#000000") as dark:
        alpha 0.6
    with dissolve

    show replikasi:
        xalign 0.5
        yalign 0.3
        zoom 1.3
    with dissolve

    o "Perhatikan gambar ini."
    o "Bagian kiri menunjukkan daur litik, sedangkan bagian kanan menunjukkan daur lisogenik."
    o "Pada daur litik, virus menempel pada sel inang, memasukkan materi genetik, membentuk bagian-bagian virus baru, lalu sel inang pecah."
    y "Berarti pada daur litik, sel inangnya hancur ya?"
    o "Benar."
    o "Tahap akhirnya disebut lisis, yaitu ketika sel inang pecah dan virus baru keluar."
    o "Agar lebih paham, mari kita lihat video berikut ini."

    stop music
    window hide
    hide replikasi
    hide dark
    show expression Movie(size=(1920, 1080), play="images/video/litik.webm") as bg_vid
    with dissolve
    pause 57
    hide bg_vid

    $ quick_menu = True
    window show
    play music "audio/science.mp3" fadein 1.0 
    o "Dari video tadi, kita bisa melihat tahapan daur litik."
    o "Tahapnya dimulai dari adsorpsi, penetrasi, sintesis, perakitan, lalu lisis."
    y "Jadi lisis itu tahap terakhir saat sel inang pecah dan virus baru keluar?"
    o "Tepat sekali."
    o "Sekarang kita lanjut ke daur lisogenik."

    show expression Solid("#000000") as dark:
        alpha 0.6
    with dissolve

    show replikasi:
        xalign 0.5
        yalign 0.3
        zoom 1.3
    with dissolve

    o "Sekarang perhatikan bagian kanan pada gambar."
    o "Bagian kanan itu menunjukkan daur lisogenik."
    o "Pada daur lisogenik, virus memasukkan materi genetiknya ke dalam sel inang."
    o "Setelah itu, materi genetik virus bergabung dengan DNA sel inang."
    y "Berarti DNA virus masuk dan menyatu dengan DNA sel inang?"
    o "Benar. Gabungan DNA virus dengan DNA sel inang disebut profag."
    o "Pada tahap ini, sel inang tidak langsung pecah."
    o "Sel inang masih bisa hidup dan membelah."
    y "Kalau sel inangnya membelah, virusnya ikut terbawa juga?"
    o "Iya. Karena DNA virus sudah menyatu dengan DNA sel inang, maka saat sel inang membelah, DNA virus juga ikut disalin."
    o "Namun, jika kondisi tertentu terjadi, profag bisa aktif kembali."
    o "Jika aktif, virus dapat masuk ke daur litik dan akhirnya membuat sel inang pecah."
    y "Jadi gampangnya, lisogenik itu virus menyisip dulu di DNA sel inang, tapi belum langsung menghancurkan sel."
    o "Tepat sekali."

    hide replikasi
    hide dark
    with dissolve

    o "Itulah dasar tentang virus yang harus kamu pahami"
    o "Sekarang, aku akan menguji pemahamanmu"

    hide nyb 
    hide osrius
    window hide
    show expression Solid("#000000") as dark: 
        alpha 0.6 
    with dissolve 
    $ quick_menu = False
    call screen kuis
    pause 1.0
    $ skor_lab = 0

    window show

    # SOAL 1 - UMUM VIRUS DAN BAKTERI
    menu:
        "Perbedaan virus dan bakteri yang paling tepat adalah..."

        "Virus memiliki sel sendiri, sedangkan bakteri tidak memiliki sel":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Coba ingat lagi ciri utama virus dan bakteri."
            hide osrius

        "Bakteri dapat berkembang biak sendiri, sedangkan virus membutuhkan sel inang":
            play sound "audio/benar.ogg"
            with vpunch
            $ skor_lab += 1
            show osmile at kiri
            o "Tepat. Virus membutuhkan sel inang untuk memperbanyak diri."
            hide osmile

        "Virus dan bakteri sama-sama tidak memiliki materi genetik":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Virus dan bakteri sama-sama memiliki materi genetik, tetapi strukturnya berbeda."
            hide osrius

    # SOAL 2 - STRUKTUR BAKTERIOFAG
    window hide

    call screen soal_nomor_gambar(
        "Berdasarkan gambar, materi genetik (DNA) virus ditunjukkan oleh nomor...",
        "soalvirus"
    )

    $ jawab = _return

    if jawab == "2":
        play sound "audio/benar.ogg"
        with vpunch

        $ skor_lab += 1

        show osmile at kiri
        o "Tepat. Nomor 2 menunjukkan materi genetik virus."
        hide osmile

    else:
        play sound "audio/salah.ogg"
        with hpunch

        show osrius at kiri
        o "Belum tepat. Perhatikan lagi bagian yang berada di dalam kepala virus."
        hide osrius

    # SOAL 3 - JENIS VIRUS
    call screen soal_gambar_teks(
        "Berdasarkan bentuknya, virus Ebola memiliki bentuk...",
        "ebola",
        "Filamen",
        "Polihedral",
        "Batang",
        zoom_gambar=0.18
    )

    $ jawab = _return

    if jawab == "a":
        play sound "audio/benar.ogg"
        with vpunch
        $ skor_lab += 1
        show osmile at kiri
        o "Tepat. Virus ebola berbentuk filamen atau bentuk benang."
        hide osmile
    else:
        play sound "audio/salah.ogg"
        with hpunch
        show osrius at kiri
        o "Belum tepat. Coba ingat lagi jenis dan bentuk-bentuk virus."
        hide osrius

    # SOAL 4 - DAUR LITIK
    menu:
        "Pada daur litik, tahap adsorpsi adalah tahap ketika..."

        "Virus memperbanyak bagian-bagian tubuhnya":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Tahap itu terjadi setelah virus berhasil masuk ke sel inang."
            hide osrius

        "Sel inang pecah dan virus baru keluar":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Itu adalah tahap akhir pada daur litik."
            hide osrius

        "Virus menempel pada permukaan sel inang":
            play sound "audio/benar.ogg"
            with vpunch
            $ skor_lab += 1
            show osmile at kiri
            o "Tepat. Adsorpsi adalah tahap saat virus menempel pada sel inang."
            hide osmile

    # SOAL 5 - DAUR LITIK
    call screen soal_gambar_teks(
        "Pada bagian daur litik, tahap ketika sel inang pecah dan virus baru keluar disebut...",
        "lisis",
        "Penetrasi",
        "Lisis",
        "Sintesis",
        zoom_gambar=2.4
    )

    $ jawab = _return

    if jawab == "b":
        play sound "audio/benar.ogg"
        with vpunch
        $ skor_lab += 1
        show osmile at kiri
        o "Tepat. Lisis adalah tahap saat sel inang pecah dan virus baru keluar."
        hide osmile
    else:
        play sound "audio/salah.ogg"
        with hpunch
        show osrius at kiri
        o "Belum tepat. Perhatikan tahap akhir pada daur litik."
        hide osrius


    # SOAL 6 - DAUR LISOGENIK
    menu:
        "Hal yang terjadi pada daur lisogenik adalah..."

        "Sel inang langsung pecah setelah virus menempel":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Itu lebih sesuai dengan daur litik."
            hide osrius

        "Virus keluar dari sel tanpa memasukkan materi genetik":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Virus tetap memasukkan materi genetiknya ke dalam sel inang."
            hide osrius

        "DNA virus ikut tersalin saat sel inang membelah":
            play sound "audio/benar.ogg"
            with vpunch
            $ skor_lab += 1
            show osmile at kiri
            o "Tepat. Pada lisogenik, DNA virus dapat ikut tersalin saat sel inang membelah."
            hide osmile

    # SOAL 7 - DAUR LISOGENIK
    call screen soal_nomor_gambar(
        "Pada daur lisogenik, gabungan DNA virus dengan DNA sel inang disebut...",
        "lisogenik",
    )

    $ jawab = _return

    if jawab == "3":
        play sound "audio/benar.ogg"
        with vpunch
        $ skor_lab += 1
        show osmile at kiri
        o "Tepat. Profag adalah DNA virus yang bergabung dengan DNA sel inang."
        hide osmile
    else:
        play sound "audio/salah.ogg"
        with hpunch
        show osrius at kiri
        o "Belum tepat. Ingat kembali istilah pada daur lisogenik."
        hide osrius

    hide dark
    with dissolve

    if skor_lab >= 6:

        hide osmile
        hide osrius

        play sound "audio/benarsmw.ogg"
        call screen hasil_quiz(skor_lab, 7, 6)

        $ quick_menu = True
        show osmile at tengah

        o "Bagus sekali!"
        o "Kamu sudah memahami dasar tentang virus."

        o "Kita lanjut ke tempat berikutnya."

        hide osmile
        with dissolve

        $ kebun_unlocked = True

        "Kebun sekarang terbuka!"

        stop music fadeout 1.0
        pause 1.0

        jump world_map

    else:
        $ kesempatan_quiz_lab -= 1
        hide osmile
        hide osrius
        play sound "audio/aw.ogg"
        call screen hasil_quiz(skor_lab, 7, 6, kesempatan_quiz_lab <= 0)

        if kesempatan_quiz_lab <= 0:
            jump bad_ending
        
        $ quick_menu = True
        show osrius at tengah

        o "Jawabanmu masih kurang tepat"
        o "Kesempatanmu tersisa [kesempatan_quiz_lab] kali lagi"

        hide osrius

        jump materi_lab

label kebun:
    stop music
    scene kebunvirus
    with fade

    play music "audio/kebun.mp3" fadein 1.0 
    show nysad at kanan
    y "Tempat ini luas sekali..."
    y "Ada kebun dan peternakan juga."
    show osrius at kiri
    o "Benar."
    o "Tempat ini menunjukkan bahwa virus bisa berdampak pada banyak bagian kehidupan, bukan hanya manusia"
    y "Maksudnya, virus bisa menyerang tanaman dan hewan juga?"
    o "Iya, virus dapat merugikan manusia, hewan, dan tumbuhan."
    o "Tapi di sisi lain, virus juga dapat dimanfaatkan dalam bidang tertentu."
    y "Jadi virus tidak selalu buruk?"
    o "Tentu saja."

    jump materi_kebun

label materi_kebun:
    hide nysad
    hide osrius
    show osrius at kiri
    with dissolve
    o "Sekarang kamu perhatikan materi pada video berikut"
    stop music
    hide osrius
    with dissolve

    window hide
    $ quick_menu = False
    show expression Movie(size=(1920, 1080), play="images/video/perkebunan.webm") as bg_vid
    with dissolve
    pause 72.5
    hide bg_vid
    $ quick_menu = True
    window show

    play music "audio/kebun.mp3" fadein 1.0 
    show nysmile at kanan
    with dissolve
    y "Sekarang aku paham."
    y "Virus bisa merugikan karena menyebabkan penyakit pada manusia, hewan, dan tumbuhan."
    show osrius at kiri
    with dissolve
    o "Benar. Namun, virus juga bisa dimanfaatkan, misalnya dalam pembuatan vaksin, terapi gen, bakteriofag, dan biopestisida."
    y "Jadi kebun dan peternakan ini jadi contoh kalau virus punya dampak besar dalam kehidupan."
    o "Tepat sekali. Virus punya dua peranan, yaitu merugikan dan menguntungkan."
    o "Sekarang, aku akan menguji pemahamanmu."

    hide nysmile
    hide osrius
    window hide
    with dissolve

    show expression Solid("#000000") as dark:
        alpha 0.6
    with dissolve

    $ quick_menu = False
    call screen kuis
    pause 1.0

    $ skor_kebun = 0

    # SOAL 1
    menu:
        "Pernyataan yang paling tepat tentang peranan virus dalam kehidupan adalah..."

        "Virus dapat merugikan, tetapi juga dapat dimanfaatkan":
            play sound "audio/benar.ogg"
            with vpunch
            $ skor_kebun += 1
            show osmile at kiri
            o "Tepat. Virus memiliki peranan merugikan dan juga menguntungkan."
            hide osmile

        "Virus dapat merugikan, tetapi tidak dapat dimanfaatkan":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Virus juga dapat dimanfaatkan dalam bidang tertentu."
            hide osrius

        "Virus dapat dimanfaatkan, tetapi tidak menyebabkan penyakit":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Virus juga dapat menyebabkan penyakit pada makhluk hidup."
            hide osrius

    # SOAL 2
    menu:
        "Kelompok penyakit pada manusia yang disebabkan oleh virus adalah..."

        "Rabies, tetelo, dan penyakit kuku dan mulut":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Coba ingat kembali contoh penyakit akibat virus yang menyerang manusia."
            hide osrius

        "Mosaik, tungro, dan TYLC":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Perhatikan lagi kelompok penyakit yang sesuai dengan pertanyaan."
            hide osrius

        "Influenza, campak, dan AIDS":
            play sound "audio/benar.ogg"
            with vpunch
            $ skor_kebun += 1
            show osmile at kiri
            o "Tepat. Influenza, campak, dan AIDS termasuk penyakit pada manusia yang disebabkan oleh virus."
            hide osmile

    # SOAL 3
    menu:
        "Contoh penyakit akibat virus yang dapat menyerang hewan adalah..."

        "Rabies, tetelo, dan penyakit kuku dan mulut":
            play sound "audio/benar.ogg"
            with vpunch
            $ skor_kebun += 1
            show osmile at kiri
            o "Tepat. Contoh tersebut termasuk penyakit akibat virus pada hewan."
            hide osmile

        "Campak, influenza, dan AIDS":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Coba ingat kembali contoh penyakit akibat virus sesuai materi."
            hide osrius

        "Mosaik, tungro, dan daun menggulung":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Perhatikan lagi kelompok penyakit yang sesuai dengan pertanyaan."
            hide osrius

    # SOAL 4
    menu:
        "Penyakit pada tumbuhan yang disebabkan oleh virus adalah..."

        "Rabies pada hewan dan tetelo pada unggas":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Coba pahami lagi contoh penyakit akibat virus dalam materi."
            hide osrius

        "Mosaik pada tembakau dan tungro pada padi":
            play sound "audio/benar.ogg"
            with vpunch
            $ skor_kebun += 1
            show osmile at kiri
            o "Tepat. Mosaik dan tungro termasuk contoh penyakit virus pada tumbuhan."
            hide osmile

        "Influenza dan campak pada manusia":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Perhatikan kembali contoh penyakit yang sesuai dengan pertanyaan."
            hide osrius

    # SOAL 5
    menu:
        "Virus dapat dimanfaatkan dalam pembuatan vaksin karena..."

        "Dapat membantu tubuh membentuk respons kekebalan":
            play sound "audio/benar.ogg"
            with vpunch
            $ skor_kebun += 1
            show osmile at kiri
            o "Tepat. Vaksin berkaitan dengan pembentukan kekebalan tubuh terhadap penyakit tertentu."
            hide osmile

        "Dapat membawa materi genetik dalam terapi gen":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Itu termasuk pemanfaatan virus, tetapi bukan fungsi utama vaksin."
            hide osrius

        "Dapat digunakan sebagai biopestisida pada tanaman":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Itu juga termasuk pemanfaatan virus, tetapi bukan dalam pembuatan vaksin."
            hide osrius

    # SOAL 6
    menu:
        "Contoh pemanfaatan virus dalam bidang pertanian adalah..."

        "Pemanfaatan virus untuk membantu tubuh kebal penyakit":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Itu memang termasuk pemanfaatan virus, tetapi bukan dalam bidang pertanian."
            hide osrius

        "Penggunaan virus sebagai biopestisida":
            play sound "audio/benar.ogg"
            with vpunch
            $ skor_kebun += 1
            show osmile at kiri
            o "Tepat. Virus tertentu dapat dimanfaatkan sebagai biopestisida untuk membantu mengendalikan hama tanaman."
            hide osmile

        "Pemanfaatan virus sebagai pembawa materi genetik":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Itu juga termasuk pemanfaatan virus, tetapi bukan contoh utama dalam bidang pertanian."
            hide osrius

    hide dark
    with dissolve

    if skor_kebun >= 5:

        hide osmile
        hide osrius

        play sound "audio/benarsmw.ogg"
        call screen hasil_quiz(skor_kebun, 6, 5)

        $ quick_menu = True

        show osmile at tengah

        o "Bagus sekali!"
        o "Kamu sudah memahami peranan virus dalam kehidupan."
        o "Sekarang kita bisa melanjutkan ke lokasi berikutnya."

        hide osmile
        with dissolve

        $ rumah_unlocked = True

        "Rumah warga sekarang terbuka."

        stop music fadeout 1.0
        pause 1.0

        jump world_map

    else:
        $ kesempatan_quiz_kebun -= 1

        hide osmile
        hide osrius

        play sound "audio/aw.ogg"
        call screen hasil_quiz(skor_kebun, 6, 5, kesempatan_quiz_kebun <= 0)

        if kesempatan_quiz_kebun <= 0:
            jump bad_ending

        $ quick_menu = True

        show osrius at tengah

        o "Jawabanmu masih kurang tepat"
        o "Kesempatanmu tersisa [kesempatan_quiz_kebun] kali lagi"
        o "Ayo pelajari kembali materi tentang peranan virus"

        hide osrius
        window hide
        with fade

        jump materi_kebun

    $ rumah_unlocked = True

    "Rumah warga sekarang terbuka."

    jump world_map


label rumah:
    stop music
    scene desa
    with fade

    play music "audio/rumahwrg.mp3" fadein 1.0 

    show nyb at kanan
    show osrius at kiri

    y "Dok... kayaknya ada orang di dalam rumah itu."

    o "Kita masuk."
    o "Kita harus melihat kondisi warga secara langsung."

    scene rumahwarga
    with fade

    show aysad at kanan
    with dissolve
    a "Uhuk... uhuk..."
    a "Siapa... itu...?"
    show osrius at kiri
    with dissolve

    o "Halo ayla, ini Dokter Orion."
    o "Sepertinya kamu sakit, coba ceritakan apa yang kamu rasakan."

    a "Ah, dokter orion."
    a "Badanku panas sejak tadi..."
    a "Aku juga batuk..."
    a "Tubuhku terasa lemas..."
    a "Kadang napasku terasa berat..."

    hide aysad
    show nyb at kanan
    with dissolve

    y "Demam, batuk, lemas, dan napas berat..."

    o "Benar. Gejala seperti demam, batuk, tubuh lemas, dan gangguan pernapasan dapat menjadi tanda adanya infeksi virus."

    y "Jadi dari gejalanya, kita bisa mulai menganalisis kemungkinan infeksi?"

    o "Tepat. Namun, gejala saja belum cukup."
    o "Kita juga harus melihat kemungkinan penularannya."

    hide osrius
    show aysad at kiri
    with dissolve

    y "Ayla, sebelum sakit, kamu sempat pergi ke tempat ramai?"

    a "Iya... Aku pergi ke pasar di desa sebelah."
    a "Banyak orang batuk di sekitar sana."

    y "Apa kamu sempat kontak dekat dengan orang-orang di sana?"

    a "Iya... Aku juga tidak terlalu menjaga jarak..."

    hide aysad
    show osrius at kiri
    with dissolve

    o "Itu bisa meningkatkan risiko penularan."
    o "Penyakit akibat virus dapat menular melalui udara saat dekat dengan penderita yang batuk atau bersin."
    o "Penularan juga bisa terjadi melalui tangan yang terkontaminasi."

    y "Maksudnya kalau tangan menyentuh benda yang terkena virus, lalu menyentuh wajah?"

    o "Benar. Karena itu, mencuci tangan sangat penting untuk mencegah penularan."

    y "Jadi pencegahannya bukan cuma mengobati orang yang sakit?"

    o "Betul. Pencegahan infeksi virus dapat dilakukan dengan vaksinasi dan pola hidup sehat."

    o "Contoh pola hidup sehat adalah sering mencuci tangan, menjauhi kontak dekat dengan penderita penyakit menular, membersihkan lingkungan, makan makanan bergizi, olahraga teratur, dan istirahat cukup."

    y "Kalau vaksinasi fungsinya apa?"

    o "Vaksin membantu tubuh membentuk kekebalan."
    o "Dengan begitu, tubuh lebih siap melawan penyebab penyakit tertentu."

    y "Jadi untuk kasus Ayla, kita perlu melihat tiga hal."

    o "Sebutkan."

    y "Pertama, gejalanya. Kedua, kemungkinan penularannya. Ketiga, cara pencegahannya."

    o "Tepat sekali."
    o "Sekarang, aku akan menguji pemahamanmu."

    hide nyb
    hide osrius
    with dissolve

    window hide

    show expression Solid("#000000") as dark:
        alpha 0.6
    with dissolve

    $ quick_menu = False
    call screen kuis
    pause 1.0

    $ skor_rumah = 0

    # SOAL 1
    menu:
        "Untuk menganalisis kondisi Ayla, data awal yang paling penting diperhatikan adalah..."

        "Riwayat tempat yang dikunjungi Ayla sebelum sakit":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Informasi itu penting, tetapi ada hal yang perlu diamati lebih dulu."
            hide osrius

        "Keluhan tubuh yang dirasakan Ayla saat sakit":
            play sound "audio/benar.ogg"
            with vpunch
            $ skor_rumah += 1
            show osmile at kiri
            o "Tepat. Analisis awal dapat dimulai dari gejala atau keluhan yang dialami pasien."
            hide osmile

        "Kegiatan Ayla setelah kembali ke rumah":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Informasi itu bisa membantu, tetapi bukan data awal yang paling utama."
            hide osrius

    # SOAL 2
    menu:
        "Keluhan Ayla yang paling mendukung dugaan infeksi virus adalah..."

        "Demam, nyeri perut, gatal, dan sulit tidur":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Coba ingat kembali keluhan utama yang disampaikan Ayla."
            hide osrius

        "Batuk, mata berair, luka kulit, dan nyeri sendi":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Beberapa keluhan itu tidak sesuai dengan kondisi Ayla."
            hide osrius

        "Demam, batuk, lemas, dan napas terasa berat":
            play sound "audio/benar.ogg"
            with vpunch
            $ skor_rumah += 1
            show osmile at kiri
            o "Tepat. Gejala tersebut dapat menjadi petunjuk adanya infeksi virus."
            hide osmile

    # SOAL 3
    menu:
        "Informasi yang paling mendukung kemungkinan penularan sebelum Ayla sakit adalah..."

        "Ayla berada di pasar ramai dan dekat dengan banyak orang batuk":
            play sound "audio/benar.ogg"
            with vpunch
            $ skor_rumah += 1
            show osmile at kiri
            o "Tepat. Riwayat berada di tempat ramai dapat membantu menganalisis kemungkinan penularan."
            hide osmile

        "Ayla beristirahat di rumah setelah tubuhnya terasa lemas":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Informasi itu terjadi setelah Ayla mulai merasakan keluhan."
            hide osrius

        "Ayla merasa tidak enak badan ketika sudah berada di rumah":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Coba perhatikan kejadian yang terjadi sebelum Ayla sakit."
            hide osrius

    # SOAL 4
    menu:
        "Jalur penularan yang paling sesuai dengan kasus Ayla adalah..."

        "Melalui benda yang disentuh tanpa memperhatikan kebersihan tangan":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Itu bisa menjadi risiko, tetapi belum paling sesuai dengan cerita Ayla."
            hide osrius

        "Melalui udara lembap di tempat yang ramai":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Coba perhatikan penyebab penularan yang lebih jelas dalam kasus ini."
            hide osrius

        "Melalui percikan dari orang sakit saat batuk atau bersin":
            play sound "audio/benar.ogg"
            with vpunch
            $ skor_rumah += 1
            show osmile at kiri
            o "Tepat. Percikan dari orang yang sakit dapat menjadi jalur penularan virus."
            hide osmile

    # SOAL 5
    menu:
        "Langkah yang paling tepat untuk mengurangi penyebaran virus di desa adalah..."

        "Merawat warga sakit saja tanpa mengubah kebiasaan warga lain":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Penanganan orang sakit perlu disertai pencegahan pada warga lain."
            hide osrius

        "Mengurangi kontak dekat, menjaga kebersihan, memakai masker, dan vaksinasi":
            play sound "audio/benar.ogg"
            with vpunch
            $ skor_rumah += 1
            show osmile at kiri
            o "Tepat. Pencegahan perlu dilakukan dengan beberapa langkah yang saling mendukung."
            hide osmile

        "Menunggu gejala semakin parah sebelum membatasi kegiatan warga":
            play sound "audio/salah.ogg"
            with hpunch
            show osrius at kiri
            o "Belum tepat. Pencegahan sebaiknya dilakukan sebelum penyebaran semakin luas."
            hide osrius

    hide dark
    with dissolve

    if skor_rumah >= 4:

        hide osmile
        hide osrius

        play sound "audio/benarsmw.ogg"
        call screen hasil_quiz(skor_rumah, 5, 4)

        window show
        $ quick_menu = True

        show osmile at kiri
        show nysmile at kanan

        o "Bagus sekali!"
        o "Kamu sudah mampu menganalisis gejala, penularan, dan pencegahan infeksi virus."

        y "Jadi sekarang kita bisa membantu warga?"

        o "Ya."
        o "Dengan memahami gejala dan cara penularannya, kita bisa menentukan langkah pencegahan yang tepat."
        hide osmile
        with dissolve
        show aysmile at kiri

        a "Nyra..."
        a "Terima kasih..."
        a "Aku sudah bisa bernapas lebih lega sekarang."

        y "Syukurlah, Ayla..."

        a "Kamu benar-benar membantu kami."

        hide aysmile
        hide nysmile
        window hide
        with dissolve

        stop music fadeout 1.0

        jump good_ending

    else:

        hide osmile
        hide osrius

        $ kesempatan_quiz_rumah -= 1

        play sound "audio/aw.ogg"
        call screen hasil_quiz(skor_rumah, 5, 4, kesempatan_quiz_rumah <= 0)

        if kesempatan_quiz_rumah <= 0:
            jump bad_ending

        window show
        $ quick_menu = True

        show osrius 

        o "Jawabanmu masih kurang tepat."
        o "Kesempatanmu tersisa [kesempatan_quiz_rumah] kali lagi."
        o "Ayo analisis kembali gejala, penularan, dan pencegahan infeksi virus."

        hide osrius
        with dissolve

        window hide

        jump rumah

label world_map:

    play music "audio/antent.mp3"
    call screen map_screen

    return

label good_ending:
    stop music fadeout 1.0

    scene desaa
    with fade

    play music "audio/happyend.mp3" fadein 1.0 

    show osmile at kiri
    with dissolve

    o "Warga mulai memahami cara melindungi diri."
    o "Mereka menjaga kebersihan, mengurangi kontak dekat, dan merawat yang sakit."
    show nyhppy at kanan
    y "Ternyata memahami virus itu penting banget..."
    y "Bukan cuma untuk menjawab soal, tapi juga untuk menyelamatkan orang."

    o "Tepat sekali."

    scene black
    with fade

    n "Hari demi hari, keadaan desa mulai berubah."
    n "Warga yang sakit mulai membaik."
    n "Kebun dan peternakan yang sebelumnya terdampak perlahan kembali pulih."

    scene kebunsehat
    with fade

    show nysmile at kanan
    show osmile at kiri

    y "Desanya... sudah terlihat hidup lagi."

    o "Ini hasil dari keberanian dan pemahamanmu, Nyra."

    y "Aku cuma mencoba memahami semuanya..."
    y "Dari struktur virus, replikasi, peranan, sampai pencegahannya."

    o "Dan pemahaman itulah yang membuatku berhasil."

    show expression Solid("#ffffff") as light:
        alpha 0.0
        linear 1.5 alpha 1.0

    y "Cahaya itu lagi..."

    o "Sepertinya waktumu di sini sudah selesai."

    y "Dokter Orion..."
    y "Terima kasih sudah membimbingku."

    o "Terima kasih juga, Nyra."
    o "Berkatmu, desa ini punya harapan lagi."

    scene black
    with fade
    pause 1.0

    stop music fadeout 1.0

    scene room
    with fade

    play music "audio/room.mp3" fadein 1.0 

    show nyhppy at kamar

    y "...Aku kembali?"

    y "Kamarku... Komputerku..."

    hide nyhppy
    with dissolve
    show nysmile at kamar

    y "Tapi sekarang semuanya terasa berbeda."
    y "Materi virus yang tadinya membingungkan..."
    y "Sekarang akhirnya aku paham."

    y "Virus bukan hanya sesuatu yang menakutkan."
    y "Virus harus dipahami, dianalisis, dan dicegah penyebarannya."

    stop music
    hide nysmile
    with dissolve

    scene good
    play music "audio/happyend.mp3" fadein 1.0 
    with fade

    window hide
    $ quick_menu = False

    pause

    $ quick_menu = True
    stop music fadeout 1.0

    return

label bad_ending:
    stop music fadeout 1.0

    scene desa
    with fade

    play music "audio/badend.mp3" 
    $ quick_menu = True
    show nysad at kanan
    show osrius at kiri

    y "Aku... gagal lagi."
    y "Aku belum benar-benar memahami materi virus ini."

    o "Nyra... Waktumu sudah habis."

    y "Jadi... aku gagal membantu desa ini?"

    o "Kamu sudah berusaha."
    o "Tapi dalam menghadapi virus, pemahaman yang keliru bisa berakibat fatal."

    hide nysad
    hide osrius
    with dissolve

    show expression Solid("#000000") as light:
        alpha 0.0
        linear 1.5 alpha 1.0
    with fade

    n "Wabah terus menyebar."
    n "Desa yang sebelumnya meminta pertolongan perlahan kehilangan harapan."
    n "Nyra tidak berhasil menyelesaikan misinya."

    scene black
    with fade

    stop music fadeout 1.0

    scene room
    with fade
    play music "audio/room.mp3" fadein 1.0 

    show nysad at kamar

    y "...Aku kembali?"
    y "Kamarku..."
    y "Tapi rasanya berbeda..."

    y "Aku gagal... Karena aku tidak memahami virus dengan cukup baik."

    y "Sekarang aku sadar..."
    y "Belajar bukan cuma soal menjawab pertanyaan."
    y "Tapi memahami agar tidak salah mengambil keputusan."

    hide nysad
    stop music
    with dissolve

    scene black
    with fade
    scene bad
    play music "audio/badend.mp3" 

    window hide
    $ quick_menu = False

    pause

    $ quick_menu = True
    stop music fadeout 1.0

    return