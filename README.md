This is a python program to allow for an Xbox controller to change the speed of the Citra 3DS emulator, as well as toggle fullscreen. This only works in Windows.

This assumes that + increases the speed, - decreases the speed, and F11 toggles fullscreen, but this can be changed in the program and in Citra itself.

The default button for changing speed is RB and for fullscreen it is LB, but this can be changed in the program.

You can change the speed multiplier by modifying the SPEED_MULTIPLIER variable. The default is x3.

If you want the speed change to be a toggle, set the TOGGLE variable to True.

If you get a ModuleNotFoundError, run 'pip install keyboard inputs pygetwindow' in the terminal.
