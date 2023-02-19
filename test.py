import RPGtext

import pygame as pg

window = pg.display.set_mode((500, 500))
clock = pg.time.Clock()


text = RPGtext.Text(
	r'<"effects": {"wave": 5}, "animSpeed": 0.1>Hiii~♪<"font": {"color": [255, 0, 0]}, "effects": {"wave": 0}> ♥ <"font": {"color": [0, 255, 255]}> <next>Long <"font": {"color": [255, 255, 255]}> time no see!',
	'pixel.ttf', 15, 3, False)



running = 1
while running :
	for event in pg.event.get() :
		if event.type == pg.QUIT :
			running = 0

	text.render(window, (250, 250), True)
	

	pg.display.flip()
	clock.tick(60)
	window.fill((0, 0, 0))