import RPGtext

import pygame as pg

window = pg.display.set_mode((500, 500))
clock = pg.time.Clock()


text0 = RPGtext.Text(
	r'<"effects": {"wave": 5}, "font": {"color": [0, 175, 255]}>~Wavy groovy text~',
	'pixel.ttf', 15, 3, False)

text1 = RPGtext.Text(
	r'<"effects": {"shake": 2}, "font": {"color": [255, 0, 0]}>Sha-a-aky te-e-ext',
	'pixel.ttf', 15, 3, False)

text2 = RPGtext.Text(
	r'<"font": {"color": [255, 0, 0]}>R<"font": {"color": [255, 122, 0]}>A<"font": {"color": [255, 255, 0]}>I<"font": {"color": [0, 255, 0]}>N<"font": {"color": [0, 255, 255]}>B<"font": {"color": [0, 0, 255]}>O<"font": {"color": [122, 0, 122]}>W<"font": {"color": [255, 0, 255]}>!',
	'pixel.ttf', 15, 3, False)

text3 = RPGtext.Text(
	r'Cool typing text effect!',
	'pixel.ttf', 15, 3, False, 0.25)



running = 1
while running :
	for event in pg.event.get() :
		if event.type == pg.QUIT :
			running = 0

	text0.render(window, (250, 75), True)
	text1.render(window, (250, 200), True)
	text2.render(window, (250, 325), True)
	text3.render(window, (250, 425), True)
	

	pg.display.flip()
	clock.tick(60)
	window.fill((0, 0, 0))