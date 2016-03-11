## Instructions ##
(I'm assuming that the user has doesn't have python or pip installed)
* First make sure you're using python 2.7.10, Macs' already have python installed but just in case go [here] (https://www.python.org/downloads/mac-osx/) and find the 2.7.10 version and select the Mac Installer.

* Go to your terminal once you have installed python and type `python`, you should see the following:
  ![python image](/python_repl.png)

* Now let's install pip using easy_install and type in your password: `sudo easy_install pip`

* With pip installed, install one of the libraries we're going to use: `pip install pyautogui`

* Now you should be able to run the following command inside the Python repl: `execfile(tetris.py)`.
* You can also run it directly from the command line with: `python tetris.py`
* Once you have it up and running, the instructions are as follows:
	1. a (return): move piece left
	2. d (return): move piece right
	3. w (return): rotate piece counter clockwise
	4. s (return): rotate piece clockwise

Enjoy!
