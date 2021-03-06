import os
from tkinter import *
from pygame import mixer
from math import sqrt, floor


# Board with all sounds
class AllSounds(object):
    def __init__(self, frame):
        self.frame = frame

        self.board_name = 'All Sounds'
        self.ext = 'wav'
        self.path_tos = [os.path.join('Sounds', 'Eric Andre'),
                         os.path.join('Sounds', 'Tim and Eric'),
                         os.path.join('Sounds', 'Steve Brule'),
                         os.path.join('Sounds', 'Lenny Pepperbottom'),
                         os.path.join('Sounds', 'Tourettes Guy'),
                         os.path.join('Sounds', 'Misc')]

        self.paths = []
        self.sounds = []
        self.buttons = []

        ea_filenames = ['yahBoobay',
                        'LRon',
                        'Xenu',
                        'DiploSong',
                        'SecondComing',
                        'PoopIntoWine',
                        'ImSaladMan',
                        'LettuceGuy',
                        'WorstShow',
                        'Osama',
                        'BirdUp',
                        'OhOh',
                        'Time4Ranch',
                        'Convention',
                        'BurningMan',
                        'EhYa',
                        'Legalize',
                        'PizzaBall',
                        'PizzaBallSong',
                        'Revolution',
                        'StephNuggz',
                        'Brotendo',
                        'RanchItUp',
                        'CherokeeChicks',
                        'BuzzMe',
                        'MellowMike',
                        'LittleSquirt',
                        'Daddy',
                        'ArtProject']

        te_filenames = ['Great Job',
                        'B M Fahrtz',
                        'The Poop Tube',
                        'Really Works',
                        'Better Than It Used Too',
                        'Sell Poop Tube',
                        'Spagett 1',
                        'Spagett 2',
                        'Spagett 3',
                        'Spagett 4',
                        'Got Ya',
                        'Armando',
                        'Cig Juice',
                        'Diah Riha Jones',
                        'D Pants',
                        'Free Real Estate']

        sb_filenames = ['Doris Salahari',
                        'Lots Have Em',
                        'Lets Check It Out',
                        'Cheers',
                        'I Gotcha',
                        'Dingus',
                        'Gravy',
                        'Orgasm',
                        'Dry',
                        'Church',
                        'Lonely',
                        'Call Me Jengus',
                        'Sneeze',
                        'Check It Out!',
                        'Friendly Lady',
                        'Guacamole',
                        'Hi',
                        'Holy Guacamole',
                        'Konnichiwa',
                        'Not That Hard',
                        'Shushee Sandwiches',
                        'Hot Guacamole']

        nw_filenames = ['Everyone Knows',
                        'Gun',
                        'Respect',
                        'How Neat Is That',
                        'Thats Pretty Neat',
                        'Cuz The Way It Is',
                        'What A Beaut',
                        'Animal Calls',
                        'G Dang It',
                        'Theme']

        tg_filenames = ['Ah Shit',
                        'Bitch',
                        'Bob Saget 1',
                        'Bob Saget 2',
                        'Bob Saget 3',
                        'Combs',
                        'Ouch',
                        'Puerto Rican',
                        'Shit! Damnit!',
                        'Shit! Sorry!',
                        'Star Trek',
                        'Total',
                        'Tuba',
                        'What I Like',
                        'Youre a Dick',
                        'Youre a F@&#%t',
                        'Are You Shitting Me',
                        'Bacon And Eggs',
                        'Car Alarm',
                        'Chewbacca',
                        'Chicken Shit Bullshit',
                        'Colgate',
                        'Duhuhuh',
                        'Fish Sticks',
                        'Fuck Salt',
                        'Hell Hole',
                        'Holy Fuck',
                        'I Called Her A Bitch',
                        'I Love You',
                        'Mens Asses',
                        'Mickey Mouse',
                        'My Own Ass',
                        'Out Of My Way',
                        'Shes A Bitch',
                        'Stay At Home',
                        'Thats My Ass',
                        'Wait A Minute',
                        'You Cant Do Shit']

        misc_filenames = ['Yee',
                          'Yee2',
                          'Chilis',
                          'Windows',
                          'WarioWhisper',
                          'WaluigiWhisper',
                          'PoopWa',
                          'CoolWas',
                          'FancyWa',
                          'AngryWa',
                          'LuigiWa',
                          'memes',
                          'JustOne1',
                          'JustOne2',
                          'JustOne3',
                          'JustOne4',
                          'JustOne5',
                          'JustOne6',
                          'FriendsDisappoint',
                          'WeirdQuestion',
                          'Touches',
                          'AsuhDude',
                          'DudeSuh',
                          'FuckBees',
                          'Bees',
                          'Fuck',
                          'KrustyKrab',
                          'WhatTheEff',
                          'SueYou',
                          'ShitOnOurBodies',
                          'FuckingDemon',
                          'Cheezits1',
                          'Cheezits2']

        all_filenames = ea_filenames + te_filenames + sb_filenames + nw_filenames + tg_filenames + misc_filenames

        self.filenames = [ea_filenames, te_filenames, sb_filenames, nw_filenames, tg_filenames, misc_filenames]
        for i in range(0, len(self.path_tos)):
            for name in self.filenames[i]:
                path = '{}{}{}.{}'.format(self.path_tos[i], os.sep, name, self.ext)
                self.paths.append(path)

        self.count = len(self.paths)
        self.nearest_square = int(floor(sqrt(self.count)))

        for path in self.paths:
            sound = mixer.Sound(path)
            self.sounds.append(sound)

        for i in range(0, self.count):
            text = all_filenames[i]
            btn = Button(self.frame, text=text, command=self.sounds[i].play)
            self.buttons.append(btn)

        self.make_grid()

    def make_grid(self):
        title = Label(self.frame, text=self.board_name)
        title.grid(row=0, columnspan=self.nearest_square)
        gridded = 0
        row = 1
        column = 0
        while gridded < self.count:
            self.buttons[gridded].grid(row=row, column=column)
            gridded += 1
            if gridded % self.nearest_square == 0:
                column = 0
                row += 1
            else:
                column += 1
