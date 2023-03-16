# Pygame RPG Text

## Introduction

The Text Animation Library is a Python library that allows the user to animate text, giving it a more dynamic appearance on screen. It is based on the Pygame library, which provides the graphics engine used to render the text. This library has two main classes: the Text class, which represents the text and provides methods to render it on screen, and the _Letter class, which represents each letter in the text and handles its animation.
Installation

This library requires the Pygame library to be installed. To install the Text Animation Library, run the following command:

::

shell

$ pip install text-animation-library

Usage

To use the Text Animation Library, you first need to import it:

.. code-block:: python

python

from text_animation_library import Text

To create a new text object, you need to provide the text string, the path to the font file, the font size, the letter spacing, and a boolean flag indicating whether the font should be anti-aliased:

.. code-block:: python

vbnet

text = Text("Hello World!", "fonts/arial.ttf", 48, 2, True)

To render the text on screen, you need to call the render method on the text object, providing a Pygame Surface object to render onto and the position of the text:

.. code-block:: python

scss

screen = pygame.display.set_mode((800, 600))
text.render(screen, [100, 100])

You can also animate the text by setting the typeSpeed parameter to a value greater than zero:

.. code-block:: python

vbnet

text = Text("Hello World!", "fonts/arial.ttf", 48, 2, True, typeSpeed=0.2)

The typeSpeed parameter specifies how fast the text should be typed out. A value of 1.0 means that the text should be typed out instantly, while a value of 0.1 means that each letter should be typed out in 0.1 seconds.
License

The Text Animation Library is released under the MIT License. See LICENSE.txt for more details.
Documentation

Full documentation can be found in the docstrings of the source code.
