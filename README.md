# Project 1 and 2 - Foundations of Programming (2023/2024)

## Project 1 - Mountains and Valleys
## Overview
Analyze a rectangular territory with intersections that can be free or occupied by mountains, forming mountain chains and valleys. Functions allow querying and analyzing the territory using Python.

## Features
- Validate territories and intersections
- Retrieve adjacent intersections and top-right intersection
- Identify mountain chains and valleys
- Check connectivity between intersections
- Count mountains, mountain chains, and valley sizes

## Usage
from project1 import * -
i1 = cria_intersecao('A', 2) -
i2 = cria_intersecao('B', 3) -
intersecoes_iguais(i1, i2)  // False

## Notes
- Invalid arguments raise ValueError with specific messages
- Functions handle immutability and maintain abstraction barriers
- Incremental development and testing recommended

## Project 2 - Go Game
## Overview
Implement the game of Go for two players. The program uses abstract data types (TADs) for intersections, stones, and the board (goban) to manage game state. Supports placing stones, capturing, scoring, and validating legal moves.

## Features
- Create, compare, and get adjacent intersections
- Create white, black or neutral stone. Check colors.
- Create boards, place/remove stones, get chains, territories, and scores
- Play, update board, handle player's move (play or pass)
- Returns True if white wins, False if black wins
- Validation for suicide, ko, and illegal moves
- Score calculation and territory evaluation

## Usage
from project2 import * -
g = cria_goban_vazio(9) - 
b, p = cria_pedra_branca(), cria_pedra_preta() -
i1 = cria_intersecao('C', 8) -
coloca_pedra(g, i1, b) -
print(goban_para_str(g)) -
### Outputs the board with the white stone at C8

## Notes
- All functions verify arguments where specified and raise ValueError
- Game ends when both players pass consecutively
- Abstraction barriers are enforced
- Incremental development and testing recommended

## Project Structure
- FP2324P1.py - main implementation of project 1
- FP2324P2.py - main implementation of project 2
- FP-2023-P1.pdf, FP-2023-P2-v2.pdf - project intructions, guidelines and relevant information
