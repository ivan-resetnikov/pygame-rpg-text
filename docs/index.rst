RPG Text generator for Pygame
=============================

Example
~~~~~~~

Use ``pip install RPG-text-engine`` to install the module
Then import it using ``import RPGtext``.

Use this line of code to create red text
``red_text = RPGtext.Text(r'<"font": {"color": [255, 0 0]}>This text is red!', 'fontFileName.ttf', <font_size>, <letters_spacing>, True)``

Then (already in your game loop), use this to render it:
``red_text.render(window, (x, y))``

More detailed syntax docs
~~~~~~~~~~~~~~~~~~~~~~~~~
``red_text = RPGtext.Text(<text>, <fontPath>, <fontSize>, <letterSpacing>, <isFontAA>)``

text          : string  - text to render (see syntax of modyfiers below)
fontPath      : string  - path to .ttf file
fontSize      : integer - size of font
letterSpacing : integer - space between letters
isFontAA      : boolean - Enable/disable anti-aliasing

Modifiers syntax
~~~~~~~~~~~~~~~~

**How to use :**
Basically, it's json formated.
But first layer is surrounded with ``<>`` isteard of ``{}``.

Example:

<"font": {"color": [255, 255, 255]}> - will make text white

Heres is the list of all modifiers:

font<br>
* color (list) : list of three RPG values<br>
* isAA  (bool) : enable/disable anti-aliasing<br>
<br>
effects<br>
* wave (int)  : wave effect<br>
* shake (int) : shaking effect<br>

animSpeed (float) : chage animation speed<br>

Also the special one
~~~~~~~~~~~~~~~~~~~~

Use ``<next>`` to go to next line, example:

``r'Line1 <next> Line2'``

**IMPORTANT** after the "<next>" modifier **must** be space or else text might broke (will be fixed later)
