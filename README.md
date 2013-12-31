This set of scripts can be used to generate Sudoku puzzles and write them into a PDF file.

# Howto

0. init submodule: `git submodule init && git submodule update`
1. run `./build.sh` for a while
2. run `python2 rand.py [difficulty] | python2 mkpdf.py output.pdf`

A random subset of the generated Sudokus will be written to the specified PDF file.
