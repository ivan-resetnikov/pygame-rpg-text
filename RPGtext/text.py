import pygame as pg



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

			font    : pg.Font,
			isAA    : bool) :

		self.letter  = font.render(letter, isAA, effects['color'])
		self.pos     = pos

		self.effects = effects


	def render (self, frame: pg.Surface) -> None :
		img = self._animate()

		frame.blit(img, self.pos)


	def _animate (self) -> pg.Surface :
		img = self.letter.copy()

		# TODO: effects

		return img



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

	def __init__ (self, text: str) :
		self.letters = self._loadText(text)


	def render (self, frame: pg.Surface) -> None :
		[letters.render(frame) for letter in self.letters]


	def _loadText (self, text) -> list :
		letters = []

		# TODO: syntax parsing

		return letters