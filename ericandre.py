from tkinter import *
from pygame import mixer

# Board with Eric Andre sounds
class EricAndre:

    def __init__(self, window):
        frame = Frame(window)
        frame.pack()

        yb = mixer.Sound('Sounds\Eric Andre\yahBoobay.wav')
        LRon = mixer.Sound('Sounds\Eric Andre\Scientology\LRon.wav')
        xenu = mixer.Sound('Sounds\Eric Andre\Scientology\Xenu.wav')
        diplo = mixer.Sound('Sounds\Eric Andre\Scientology\DiploSong.wav')
        second = mixer.Sound('Sounds\Eric Andre\Scientology\SecondComing.wav')
        poopWine = mixer.Sound('Sounds\Eric Andre\Scientology\PoopIntoWine.wav')
        saladMan = mixer.Sound('Sounds\Eric Andre\Salad Man\ImSaladMan.Wav')
        lettuce = mixer.Sound('Sounds\Eric Andre\Salad Man\LettuceGuy.wav')
        worst = mixer.Sound('Sounds\Eric Andre\Bird Up\WorstShow.wav')
        osama = mixer.Sound('Sounds\Eric Andre\Bird Up\Osama.wav')
        birdUp = mixer.Sound('Sounds\Eric Andre\Bird Up\BirdUp.wav')
        ohoh = mixer.Sound('Sounds\Eric Andre\Bird Up\OhOh.wav')
        time4ranch = mixer.Sound('Sounds\Eric Andre\Ranch1\Time4Ranch.wav')
        nin = mixer.Sound('Sounds\Eric Andre\Ranch1\Convention.wav')
        burningMan = mixer.Sound('Sounds\Eric Andre\Ranch1\BurningMan.wav')
        ehYa = mixer.Sound('Sounds\Eric Andre\Ranch1\EhYa.wav')
        legalize = mixer.Sound('Sounds\Eric Andre\Ranch1\Legalize.wav')
        pizzaBall = mixer.Sound('Sounds\Eric Andre\Pizza Ball\PizzaBall.wav')
        pizzaBallSong = mixer.Sound('Sounds\Eric Andre\Pizza Ball\PizzaBallSong.wav')
        ranchRev = mixer.Sound('Sounds\Eric Andre\Ranch2\Revolution.wav')
        steph = mixer.Sound('Sounds\Eric Andre\Ranch2\StephNuggz.wav')
        brotendo = mixer.Sound('Sounds\Eric Andre\Ranch2\Brotendo.wav')
        ranchUp = mixer.Sound('Sounds\Eric Andre\Ranch3\RanchItUp.wav')
        cherokee = mixer.Sound('Sounds\Eric Andre\Ranch3\CherokeeChicks.wav')
        buzz = mixer.Sound('Sounds\Eric Andre\Ranch3\BuzzMe.wav')
        mellow = mixer.Sound('Sounds\Eric Andre\Ranch3\MellowMike.wav')
        littleSquirt = mixer.Sound('Sounds\Eric Andre\Juice\LittleSquirt.wav')
        daddy = mixer.Sound('Sounds\Eric Andre\Juice\Daddy.wav')
        artProject = mixer.Sound('Sounds\Eric Andre\ArtProject.wav')
        # ----------------------------------------------------------------------

        self.title = Label(frame, text='Eric Andre Sounds')
        self.title.grid(row=0, columnspan=5)

        self.ybBtn = Button(frame, text='Yah Boobay!', command=yb.play)
        self.LRonBtn = Button(frame, text='L Ron Hubbard', command=LRon.play)
        self.xenuBtn = Button(frame, text='Xenu', command=xenu.play)
        self.diploBtn = Button(frame, text='Diplo Song', command=diplo.play)
        self.secondBtn = Button(frame, text='Second Coming', command=second.play)
        self.poopWineBtn = Button(frame, text='Turn That Poop Into Wine', command=poopWine.play)
        self.saladManBtn = Button(frame, text='Salad Man', command=saladMan.play)
        self.lettuceBtn = Button(frame, text='Lettuce Guy', command=lettuce.play)
        self.worstBtn = Button(frame, text='Worst Show on TV', command=worst.play)
        self.osamaBtn = Button(frame, text='Osama bin Laden', command=osama.play)
        self.birdUpBtn = Button(frame, text='Bird Up', command=birdUp.play)
        self.ohohBtn = Button(frame, text='Oh oooooh', command=ohoh.play)
        self.time4ranchBtn = Button(frame, text='Time For Some Ranch', command=time4ranch.play)
        self.ninBtn = Button(frame, text='Nintendo Convention', command=nin.play)
        self.burningManBtn = Button(frame, text='Burning Man Rehearsal', command=burningMan.play)
        self.ehYaBtn = Button(frame, text='Eh Ya', command=ehYa.play)
        self.legalizeBtn = Button(frame, text='Legalize Ranch', command=legalize.play)
        self.pizzaBallBtn = Button(frame, text='Pizza Ball', command=pizzaBall.play)
        self.pizzaBallSongBtn = Button(frame, text='Pizza Ball Sung', command=pizzaBallSong.play)
        self.ranchRevBtn = Button(frame, text='Ranch Revolution', command=ranchRev.play)
        self.stephBtn = Button(frame, text='Steph Nuggz', command=steph.play)
        self.brotendoBtn = Button(frame, text='Yo Brotendo', command=brotendo.play)
        self.ranchUpBtn = Button(frame, text='Ranch It Up', command=ranchUp.play)
        self.cherokeeBtn = Button(frame, text='Cherokee Chicks', command=cherokee.play)
        self.buzzBtn = Button(frame, text='Buzz Me', command=buzz.play)
        self.mellowBtn = Button(frame, text='Mellow Mike', command=mellow.play)
        self.littleSquirtBtn = Button(frame, text='Little Squirt', command=littleSquirt.play)
        self.daddyBtn = Button(frame, text='Daddy Needs His Juice', command=daddy.play)
        self.artProjectBtn = Button(frame, text='Art Project', command=artProject.play)
        # ----------------------------------------------------------------------

        self.ybBtn.grid(row=1, column=0)
        self.LRonBtn.grid(row=1, column=1)
        self.xenuBtn.grid(row=1, column=2)
        self.diploBtn.grid(row=1, column=3)
        self.secondBtn.grid(row=1, column=4)
        self.poopWineBtn.grid(row=2, column=0)
        self.saladManBtn.grid(row=2, column=1)
        self.lettuceBtn.grid(row=2, column=2)
        self.worstBtn.grid(row=2, column=3)
        self.osamaBtn.grid(row=2, column=4)
        self.birdUpBtn.grid(row=3, column=0)
        self.ohohBtn.grid(row=3, column=1)
        self.time4ranchBtn.grid(row=3, column=2)
        self.ninBtn.grid(row=3, column=3)
        self.burningManBtn.grid(row=3, column=4)
        self.ehYaBtn.grid(row=4, column=0)
        self.legalizeBtn.grid(row=4, column=1)
        self.pizzaBallBtn.grid(row=4, column=2)
        self.pizzaBallSongBtn.grid(row=4, column=3)
        self.ranchRevBtn.grid(row=4, column=4)
        self.stephBtn.grid(row=5, column=0)
        self.brotendoBtn.grid(row=5, column=1)
        self.ranchUpBtn.grid(row=5, column=2)
        self.cherokeeBtn.grid(row=5, column=3)
        self.buzzBtn.grid(row=5, column=4)
        self.mellowBtn.grid(row=6, column=0)
        self.littleSquirtBtn.grid(row=6, column=1)
        self.daddyBtn.grid(row=6, column=2)
        self.artProjectBtn.grid(row=6, column=3)
        # ----------------------------------------------------------------------
