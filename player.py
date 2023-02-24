######################################################################################
#                                                                                    # 
#                            ,.--------._                                            #
#                           /            ''.                                         #
#                         ,'                \     |"\                /\          /\  #
#                /"|     /                   \    |__"              ( \\        // ) #
#               "_"|    /           z#####z   \  //                  \ \\      // /  #
#                 \\  #####        ##------".  \//                    \_\\||||//_/   #
#                  \\/-----\     /          ".  \                      \/ _  _ \     #
#                   \|      \   |   ,,--..       \                    \/|(O)(O)|     #
#                   | ,.--._ \  (  | ##   \)      \                  \/ |      |     #
#                   |(  ##  )/   \ `-....-//       |///////////////_\/  \      /     #
#                     '--'."      \                \              //     |____|      #
#                  /'    /         ) --.            \            ||     /      \     #
#               ,..|     \.________/    `-..         \   \       \|     \ 0  0 /     #
#            _,##/ |   ,/   /   \           \         \   \       U    / \_//_/      #
#          :###.-  |  ,/   /     \        /' ""\      .\        (     /              #
#         /####|   |   (.___________,---',/    |       |\=._____|  |_/               #
#        /#####|   |     \__|__|__|__|_,/             |####\    |  ||                #
#       /######\   \      \__________/                /#####|   \  ||                #
#      /|#######`. `\                                /#######\   | ||                #
#     /++\#########\  \                      _,'    _/#########\ | ||                #
#    /++++|#########|  \      .---..       ,/      ,'##########.\|_||  Donkey By     #
#   //++++|#########\.  \.              ,-/      ,'########,+++++\\_\\ Hard'96       #
#  /++++++|##########\.   '._        _,/       ,'######,''++++++++\                  #
# |+++++++|###########|       -----."        _'#######' +++++++++++\                 #
# |+++++++|############\.     \\     //      /#######/++++ S@yaN +++\                #
#      ________________________\\___//______________________________________         #
#     / ____________________________________________________________________)        #
#    / /              _                                             _                #
#    | |             | |                                           | |               #
#     \ \            | | _           ____           ____           | |  _            #
#      \ \           | || \         / ___)         / _  )          | | / )           #
#  _____) )          | | | |        | |           (  __ /          | |< (            #
# (______/           |_| |_|        |_|            \_____)         |_| \_)           #
#                                                                           19.08.02 #
######################################################################################

# import is include

#import everything from settings
from settings import *
#rename pygame
import pygame as pg
#import math library
import math

class Player:
	def __init__(self, game):
		self.game = game
		self.x, self.y = PLAYER_POS
		self.angle = PLAYER_ANGLE
        
	def movement(self):
		sin_a = math.sin(self.angle)
		cos_a = math.cos(self.angle)
		dx, dy = 0, 0
        # De snelheid wordt vermenigvuldigd met de tijd die is verstreken sinds de laatste keer dat de methode werd aangeroepen.
        # Dit zorgt ervoor dat de bewegingssnelheid consistent blijft ongeacht de snelheid van de computer.
		speed = PLAYER_SPEED * self.game.delta_time
        # Geven de verandering in de x, y, coordinaten van de speler die beweegt in de richting van de huidige hoek
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
		
        '''
        Je gebruikt de sinus en de cosinus om de BEWEGINGSVECTOR van de camera te bepalen in de huidige HOEK (i.e. RICHTING) van de camera.
        Let op: Dit is een virtuele camera. Geen echte.
        hoek (i.e. angle) is de richting waarin de camera kijkt.
        cosinus van een hoek -> verandering in de x richting (i.e. horizontale beweging)
        sinus van een hoek -> verandering in de y richting (i.e. verticale beweging)
        Door de BEWEGINGSVECTOR van de camera te berekenen (via sinus en cosinus van een huidige hoek), kan de camera worden "verplaatst" in de juiste richting.
        M.a.w. de cosinus en sinus zijn essentieel bij het berekenen van de beweging van een camera.


        In de raycaster kan de beweging van de camera worden beschreven in een x,y vector. (want 2 dimensions).
        De hoek/angle geeft aan in welke richting de camera kijkt. Bijv links/rechts/omhoog/omlaag vanaf de speler position de 2d wereld.
        Door de SNELHEID/SPEED van de camera te vermenigvuldigen met de sinus en cosinus van de huidige hoek/angle, kan je de horizontale (x-richting) en de
        verticale (y-richting) onderdelen van de bewegingsvector bepalen. 

        Wil je dat de camera naar rechts beweegt? (dus in de positive x richting), dan vermenigvuldig je de cosinus van de hoek met de snelheid.
        Waarom? Omdat de cosinus van 0 graden gelijk is aan 1. Dit betekent dat de x component van de bewegingsvector gelijk zal zijn aan de sneheid. 


        '''
		keys = pg.key.get_pressed() # get pressed or get rekt
		if keys[pg.K_w]:
			dx += speed_cos
			dy += speed_sin
		if keys[pg.K_a]:
			dx += speed_sin
			dy -= speed_cos
		if keys[pg.K_s]:
			dx -= speed_cos
			dy -= speed_sin
		if keys[pg.K_d]:
			dx -= speed_sin
			dy += speed_cos

		self.x += dx
		self.y += dy

		if keys[pg.K_LEFT]:
			self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
		if keys[pg.K_RIGHT]:
			self.angle += PLAYER_ROT_SPEED * self.game.delta_time
		self.angle %= math.tau 
		# "% tau" haal %6.28 an het bedrag af zodat de radialen overblijven waar die sin/cos mee werkt

	def update(self):
		self.movement()

	@property # TODO begrijpen property
	def pos(self):
		return self.x, self.y
	
	@property
	def map_pos(self):
		return int(self.x), int(self.y)