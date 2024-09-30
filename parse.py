s = """.O..O..O..O..O..O..O..O..O..O..O..O..O..O..O..O..O..O..O.
.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.
.........................................................
.OOOOOOOOOOOOOOOOOOOOOOOOOOOOO..OOO..OOOOOOOOOOOOOOOOOOO.
O..............................OO...OO..................O
.OOOOOOOOOOOOOOOOOOOOOOOO..OOO...OO...OOOO..OOOOOOOOOOOO.
..........................OO...............OO............
.OOOOOOOOOOOOOOOOOOOOOOOO..OOO...OO.....OO...OO..OOOOOOO.
O..............................OO...O.OO........OO......O
.OOOOOOOOOOOOOOOOOOOOOOOO..OOO..OOO...OO.....OO...OOOOOO.
..........................OO............OO.OO............
.OOOOOOOOOOOOOOOOOOOOOOOO...OOOOO..........OO.....OOOOOO.
O............................O...............OO.OO......O
.OOOOOOOOOOOOOOOOOOOOOOOO.....O.........O.......OO..OOOO.
..........................O.O......O...O..........OO.....
.OOOOOOOOOOOOOOOOOOOOOOOO...O.O.OOOOO......O.......OOOOO.
O..............................OOO...O......O...........O
.OOOOOOOOOOOOOOOOOOOOOOOO...O.O.OOOOO......O.......OOOOO.
..........................O.O......O...O..........OO.....
.OOOOOOOOOOOOOOOOOOOOOOOO.....O.........O.......OO..OOOO.
O............................O...............OO.OO......O
.OOOOOOOOOOOOOOOOOOOOOOOO...OOOOO..........OO.....OOOOOO.
..........................OO............OO.OO............
.OOOOOOOOOOOOOOOOOOOOOOOO..OOO..OOO...OO.....OO...OOOOOO.
O..............................OO...O.OO........OO......O
.OOOOOOOOOOOOOOOOOOOOOOOO..OOO...OO.....OO...OO..OOOOOOO.
..........................OO...............OO............
.OOOOOOOOOOOOOOOOOOOOOOOO..OOO...OO...OOOO..OOOOOOOOOOOO.
O..............................OO...OO..................O
.OOOOOOOOOOOOOOOOOOOOOOOOOOOOO..OOO..OOOOOOOOOOOOOOOOOOO.
.........................................................
.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.
.O..O..O..O..O..O..O..O..O..O..O..O..O..O..O..O..O..O..O."""
s = s.split("\n")
for i in range(len(s)):
    n = s[i].strip("\t")
    #print(n)
    for k in range(len(n)):
        if n[k]=="O":
            print(f"({k},{i})", end=",")