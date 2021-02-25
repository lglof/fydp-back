to test:

`python3 setup.py pytest`

to build package:

- update the version number
  `python3 setup.py bdist_wheel`

then to install the package:

- from the root dir of the project you want to install it in
  `pip install /path/to/.whl`
  the .whl should be in `fydp-back/dist/`
  Just make sure you get the right version when getting the wheel file

- why's `rfidFunctions.py` almost all commented out?
  Since I removed the hardware dependant stuff so that testing works ok.
