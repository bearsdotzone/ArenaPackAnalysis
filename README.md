# ArenaPackAnalysis
*Python 3*

Expects cards in a plaintext file in the following format.

```
(Num Cards) (Card Name) (Set{Optional})
10 Forest (KHM)
1 Command Tower
```
usage: analysis.py [-h] [-i INPUTFILE] [-c]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputfile INPUTFILE
                        Indicate an input file, defaults to input.txt in pwd.
  -c                    Show card frequency analysis, used for multiple decklists in one file.
```
