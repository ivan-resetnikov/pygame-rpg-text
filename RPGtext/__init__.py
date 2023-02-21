# parcing
from json import loads as parceJSON

# effects
from math   import sin
from random import uniform

# graphics
import pygame as pg
pg.font.init()



class _Letter :
	'''
	Class "_Letter" doc string

	Description :
		_Letter class, is a class which
		represents each letter in text.

	Public methods :
		render() - renders letter

	Private methods :
		_animate() - animates letter
	'''

	def __init__ (self,
			letter  : str,
			pos     : list[float],

			effects : dict,

			font    : pg.font.Font,

			index   : int) :

		self.letter  = font.render(letter, effects['font']['isAA'], effects['font']['color'])
		self.pos     = pos

		self.effects = {
			'font' : {
				'color' : effects['font']['color'],
				'isAA'  : effects['font']['isAA']
			},
			'effects' : {
				'wave'  : effects['effects']['wave'],
				'shake' : effects['effects']['shake']
			},
			'animSpeed' : effects['animSpeed']
		}

		self.time = 0 + index


	def render (self, frame: pg.Surface, pos: list[float]) -> None :
		img, offset = self._animate()

		frame.blit(img, [
			self.pos[0] + pos[0] + offset[0],
			self.pos[1] + pos[1] + offset[1]])


	def _animate (self) -> pg.Surface :
		self.time += self.effects['animSpeed']

		img    = self.letter.copy()
		offset = [0, 0]

		offset[1] += sin(self.time) * self.effects['effects']['wave']
		
		offset[0] += uniform(-self.effects['effects']['shake'], self.effects['effects']['shake'])
		offset[1] += uniform(-self.effects['effects']['shake'], self.effects['effects']['shake'])

		return (img, offset)



class Text :
	'''
	Class "Text" doc string

	Description :
		Text class is a class which represents text,
		and will be bridge between library and user application.

	Public methods :
		render() - renders text

	Private methods :
		_loadText() - parses syntax of input text,
		to list of objects of class _Letter
	'''

	def __init__ (self, text: str, fontPath: str, fontSize: int, letterSpacing: int, isFontAA: bool, typeSpeed: float = 0) :
		self.font    = pg.font.Font(fontPath, fontSize)

		self.isFontAA = isFontAA
		self.fontSize = fontSize
		self.letterSpacing = letterSpacing

		self.letters = self._loadText(text)

		self.typeSpeed = typeSpeed
		
		if typeSpeed == 0 :
			self.cursorPos = len(self.letters)
		else :
			self.cursorPos = 0


	def render (self, frame: pg.Surface, pos: list[float], centered: bool) -> None :
		offset = [0, 0]

		if centered :
			offset[0] = -self.textSize[0] * 0.5
			offset[1] = -self.textSize[1] * 0.5

		[letter.render(frame, [pos[0] + offset[0], pos[1] + offset[1]]) for letter in self.letters[:round(self.cursorPos):]]

		if self.cursorPos < len(self.letters) : self.cursorPos += self.typeSpeed


	def _loadText (self, text) -> list :
		letters = []

		effects = {
			'font' : {
				'color' : [255, 255, 255],
				'isAA'  : self.isFontAA
			},
			'effects' : {
				'wave'  : 0,
				'shake' : 0
			},
			'animSpeed' : 0.1,
		}

		parcingMode = 'parcing text'
		cursorPos = [0, 0]

		self.textSize = [0, self.fontSize]
		lastTextSize = 0


		for i, letter in enumerate(text) :
			if letter == '<' :
				parcingMode = 'parcing modifier'
				modifierString = ''

				if text[i+1:i+5] == 'next' :
					self.textSize[1] += self.fontSize * 2
					cursorPos[1] += self.fontSize * 2

					cursorPos[0] = 0

					lastTextSize = self.textSize[0]
					self.textSize[0] = 0

			elif text[i-1:i] == '>' :
				parcingMode = 'parcing text'
				self._parceModifier(modifierString, effects)

			if parcingMode == 'parcing modifier' :
				modifierString += letter

			elif parcingMode == 'parcing text' :
				if letter != ' ' :
					letters.append(_Letter(
						letter,
						[cursorPos[0], cursorPos[1]],
						effects,
						self.font,
						cursorPos[0] / (self.fontSize + self.letterSpacing)
					))

				cursorPos[0]  += self.fontSize + self.letterSpacing
				self.textSize[0] += self.fontSize + self.letterSpacing

				if self.textSize[0] > lastTextSize : lastTextSize = self.textSize[0]

		return letters


	def _parceModifier (self, modifierText: str, effects: dict) -> dict :
		if modifierText != '<next>' :
			modifierText = modifierText.replace('\'', '"')
			modifierText = modifierText.replace('<', '{')
			modifierText = modifierText.replace('>', '}')

			modifier = parceJSON(modifierText)

			if 'font' in modifier :
				if 'color' in modifier['font'] : effects['font']['color'] = modifier['font']['color']
				if 'isAA'  in modifier['font'] : effects['font']['isAA']  = modifier['font']['isAA']

			if 'effects' in modifier :
				if 'wave'  in modifier['effects'] : effects['effects']['wave']  = modifier['effects']['wave']
				if 'shake' in modifier['effects'] : effects['effects']['shake'] = modifier['effects']['shake']

			if 'animSpeed'     in modifier : effects['animSpeed']     = modifier['animSpeed']