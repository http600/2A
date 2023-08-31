#!/usr/bin/env python3

from sys import argv
from os import linesep

def run(text):
    text = open(text, 'r')
    lines = [x.rstrip() for x in text.readlines()]
    text.close()

    latex = open('README.tex', 'w')
    latex.write(r'% !TeX program = xelatex' + linesep)
    latex.write(r'\documentclass{article}' + linesep)
    latex.write(r'\usepackage{xeCJK}' + linesep)
    latex.write(r'\usepackage{tikz}' + linesep)
    latex.write(r'\usepackage[outline]{contour}' + linesep)
    latex.write(r'\usepackage{graphicx}' + linesep)
    latex.write(r'\graphicspath{ {./} }' + linesep)
    latex.write(r'\setCJKmainfont{Kaiti SC}' + linesep)
    latex.write(r'% \setCJKmainfont{Xingkai SC}' + linesep)
    latex.write(r'% \setCJKmainfont{STKaiti}' + linesep)
    latex.write(r'' + linesep)
    latex.write(r'\newcommand\Grid[1]{%' + linesep)
    latex.write(r' \tikz[baseline=(char.base)]{%' + linesep)
    latex.write(r'  \draw[xstep=1ex,ystep=1ex,help lines] (-1ex,-1ex) grid (1ex,1ex);' + linesep)
    latex.write(r'  \draw[help lines,densely dash dot]' + linesep)
    latex.write(r'  (-1ex,-1ex) -- (1ex,1ex)  (-1ex,1ex) -- (1ex,-1ex);' + linesep)
    latex.write(r'  \node[inner sep=0pt] (char) at (0,0) {#1};' + linesep)
    latex.write(r' }%' + linesep)
    latex.write(r'}' + linesep)
    latex.write(r'\pagenumbering{gobble}' + linesep)
    latex.write(r'\begin{document}' + linesep)
    latex.write(r'\begin{center}' + linesep)
    latex.write(r'    \Huge {} \\'.format(lines[0]) + linesep)
    latex.write(r'\end{center}' + linesep)
    latex.write(r'\begin{flushright}' + linesep)
    latex.write(r'    \huge {} $\bullet$ {} \\'.format(lines[1], lines[2]) + linesep)
    latex.write(r'\end{flushright}' + linesep)
    latex.write(r'\begin{center}' + linesep)
    for x in range(3, len(lines)):
        latex.write(r'    \Huge {} \\'.format(lines[x]) + linesep)
    latex.write(r'\end{center}' + linesep)
    latex.write(r'\hrule' + linesep)
    latex.write(r'\begin{center}' + linesep)
    latex.write(r'    \Huge ')
    for x in lines[0]:
        latex.write(r'\Grid{{{}}}'.format(x))
    latex.write(r' \\' + linesep)
    latex.write(r'\end{center}' + linesep)
    latex.write(r'\begin{flushright}' + linesep)
    latex.write(r'    \huge ')
    for x in lines[1]:
        latex.write(r'\Grid{{{}}}'.format(x))
    latex.write(r' $\bullet$ ')
    for x in lines[2]:
        latex.write(r'\Grid{{{}}}'.format(x))
    latex.write(r' \\' + linesep)
    latex.write(r'\end{flushright}' + linesep)
    latex.write(r'\begin{center}' + linesep)
    for x in range(3, len(lines)):
        latex.write(r'    \Huge ')
        for y in lines[x]:
            latex.write(r'\Grid{{{}}}'.format(y))
        latex.write(r' \\' + linesep)
    latex.write(r'\end{center}' + linesep)
    latex.write(r'\hrule' + linesep)
    latex.write(r'\newpage' + linesep)
    latex.write(r'\begin{figure}' + linesep)
    latex.write(r'    \centering' + linesep)
    latex.write(r'    \makebox[0pt]{\includegraphics[width=0.9\paperwidth]{image.jpg}}' + linesep)
    latex.write(r'\end{figure}' + linesep)
    latex.write(r'\end{document}' + linesep)
    return

if __name__ == '__main__':
    text = 'README.text'
    if len(argv) > 1:
        text = argv[1]
    run(text)