#!/bin/bash
SUDOKU="python2 PADS/Sudoku.py"
OUT="sudokus"
TMP=`mktemp`
while true; do
  if ! $SUDOKU -g -a -f numeric > $TMP; then
    rm $TMP
    exit 1
  fi
  LVL=`grep Level $TMP | cut -d" " -f2`
  if [[ "$LVL" != "easy" && "$LVL" != "moderate" ]]; then
    mkdir -p $OUT/$LVL
    i=`ls $OUT/$LVL | sort -n | tail -n 1`
    [[ -z "$i" ]] && i=0
    echo $LVL $i
    mv $TMP $OUT/$LVL/$(($i + 1))
  fi
done
