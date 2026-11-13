---
declaration: section
origin: cited
lean: MetaMathlibExt.CubeRotationMove, MetaMathlibExt.cubeRotationMove_examples, MetaMathlibExt.CubeVertexMove, MetaMathlibExt.CubeEdgeMove, MetaMathlibExt.CubeFaceMove, MetaMathlibExt.cubeVertexEdgeFaceMove_examples, MetaMathlibExt.cubeRotationNim_pPositions, MetaMathlibExt.cubeVertexNim_pPositions
statement: formalized
---

# Nim on a cube

16 results, 6 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html).

## Rotation move on the cube

Label the faces of a cube $f_a, f_b, f_c, f_A, f_B, f_C$, where
$f_A$, $f_B$, $f_C$ are opposite $f_a$, $f_b$, $f_c$, and record a position as the tuple
$p = (a, b, c, A, B, C)$ of numbers of tokens on these faces. A rotation is one of the three
belts of four faces $\{f_a, f_b, f_A, f_B\}$, $\{f_a, f_c, f_A, f_C\}$ and
$\{f_b, f_c, f_B, f_C\}$. In the game $C_R$ there is a move from a position $p$ to a position $q$
when, for some rotation, $q$ agrees with $p$ on the two faces outside the rotation, $q \le p$ on
every face, and $q \ne p$; that is, at least one token in total is removed from the four faces
of the rotation.

## Sources

- Balaji R. Kadam and A. J. Shaiju, *Variations of the Nim Game Played on a Cube*, INTEGERS 25 (2025), Article G2, Section 2 (the variation `C_R`).

Formalized by `MetaMathlibExt.CubeRotationMove`, a definition declared in [WantedExt/Combinatorics/CubeRotationNimWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CubeRotationNimWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html#cube-rotation-move).

## Rotation moves at the empty cube

Write positions as tuples $(a, b, c, A, B, C)$ of numbers
of tokens on the faces $f_a, f_b, f_c, f_A, f_B, f_C$ of a cube. In the game $C_R$ there is a
rotation move from $(0, 0, 0, 0, 0, 1)$ to the empty position $(0, 0, 0, 0, 0, 0)$, and there is
no rotation move from the empty position.

## Sources

- Balaji R. Kadam and A. J. Shaiju, *Variations of the Nim Game Played on a Cube*, INTEGERS 25 (2025), Article G2, Section 2 (the variation `C_R`).

Formalized by `MetaMathlibExt.cubeRotationMove_examples`, a theorem declared in [WantedExt/Combinatorics/CubeRotationNimWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CubeRotationNimWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html#cube-rotation-move-examples).

## Vertex move on the cube

Label the faces of a cube $f_a, f_b, f_c, f_A, f_B, f_C$, where
$f_A$, $f_B$, $f_C$ are opposite $f_a$, $f_b$, $f_c$, and record a position as the tuple
$p = (a, b, c, A, B, C)$ of numbers of tokens on these faces. In the game $C_V$ there is a move
from a position $p$ to a position $q$ when, for some choice of one face from each opposite pair
$\{f_a, f_A\}$, $\{f_b, f_B\}$, $\{f_c, f_C\}$ (three faces that meet at a vertex), $q$ agrees
with $p$ on the other three faces, $q \le p$ on every face, and $q \ne p$; that is, at least one
token in total is removed from the three faces at one vertex.

## Sources

- Balaji R. Kadam and A. J. Shaiju, *Variations of the Nim Game Played on a Cube*, INTEGERS 25 (2025), Article G2, Section 1 (the variation `C_V`).

Formalized by `MetaMathlibExt.CubeVertexMove`, a definition declared in [WantedExt/Combinatorics/CubeRotationNimWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CubeRotationNimWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html#cube-vertex-move).

## Edge move on the cube

Label the faces of a cube $f_a, f_b, f_c, f_A, f_B, f_C$, where
$f_A$, $f_B$, $f_C$ are opposite $f_a$, $f_b$, $f_c$, and record a position as the tuple
$p = (a, b, c, A, B, C)$ of numbers of tokens on these faces. In the game $C_E$ there is a move
from a position $p$ to a position $q$ when, for some two faces from different opposite pairs
(two faces that share an edge), $q$ agrees with $p$ on the other four faces, $q \le p$ on every
face, and $q \ne p$; that is, at least one token in total is removed from the two faces at one
edge.

## Sources

- Balaji R. Kadam and A. J. Shaiju, *Variations of the Nim Game Played on a Cube*, INTEGERS 25 (2025), Article G2, Section 1 (the variation `C_E`).

Formalized by `MetaMathlibExt.CubeEdgeMove`, a definition declared in [WantedExt/Combinatorics/CubeRotationNimWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CubeRotationNimWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html#cube-edge-move).

## Face move on the cube

Label the faces of a cube $f_a, f_b, f_c, f_A, f_B, f_C$, where
$f_A$, $f_B$, $f_C$ are opposite $f_a$, $f_b$, $f_c$, and record a position as the tuple
$p = (a, b, c, A, B, C)$ of numbers of tokens on these faces. In the game $C_F$ there is a move
from a position $p$ to a position $q$ when, for some face, $q$ agrees with $p$ on the other five
faces, $q \le p$ on every face, and $q \ne p$; that is, at least one token is removed from one
face. So $C_F$ is Nim with six heaps.

## Sources

- Balaji R. Kadam and A. J. Shaiju, *Variations of the Nim Game Played on a Cube*, INTEGERS 25 (2025), Article G2, Section 1 (the variation `C_F`).

Formalized by `MetaMathlibExt.CubeFaceMove`, a definition declared in [WantedExt/Combinatorics/CubeRotationNimWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CubeRotationNimWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html#cube-face-move).

## Examples of vertex, edge and face moves

Write positions as tuples $(a, b, c, A, B, C)$ of
numbers of tokens on the faces $f_a, f_b, f_c, f_A, f_B, f_C$ of a cube. There is a vertex move
(game $C_V$) from $(1, 1, 1, 0, 0, 0)$ to the empty position $(0, 0, 0, 0, 0, 0)$, an edge move
(game $C_E$) from $(1, 1, 0, 0, 0, 0)$ to the empty position, and a face move (game $C_F$) from
$(1, 1, 1, 0, 0, 0)$ to $(0, 1, 1, 0, 0, 0)$. No vertex move, edge move or face move starts at
the empty position.

## Sources

- Balaji R. Kadam and A. J. Shaiju, *Variations of the Nim Game Played on a Cube*, INTEGERS 25 (2025), Article G2, Section 1.

Formalized by `MetaMathlibExt.cubeVertexEdgeFaceMove_examples`, a theorem declared in [WantedExt/Combinatorics/CubeRotationNimWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CubeRotationNimWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html#cube-vertex-edge-face-move-examples).

## P-positions of rotation Nim on a cube

Write positions of the game $C_R$ as tuples
$(a, b, c, A, B, C)$ of numbers of tokens on the faces $f_a, f_b, f_c, f_A, f_B, f_C$, where
$f_A$, $f_B$, $f_C$ are opposite $f_a$, $f_b$, $f_c$. Let $\mathcal P$ be the set of positions with
$a + A = b + B = c + C$. Then no rotation move leads from a position in $\mathcal P$ to a position
in $\mathcal P$, and from every position outside $\mathcal P$ there is a rotation move to a
position in $\mathcal P$.

Every move removes a token, so the game terminates and $\mathcal P$ is exactly the set of
P-positions (second-player wins) under normal play.

## Sources

- Balaji R. Kadam and A. J. Shaiju, *Variations of the Nim Game Played on a Cube*, INTEGERS 25 (2025), Article G2, Theorem 5.

Stated but not proved: `MetaMathlibExt.cubeRotationNim_pPositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/CubeRotationNimWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CubeRotationNimWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html#cube-rotation-nim-p-positions).

## P-positions of vertex Nim on a cube

Write a position of the cube game as
$p = (a, b, c, A, B, C)$, the numbers of tokens on the six faces of a cube, where the faces
carrying $A$, $B$, $C$ are opposite those carrying $a$, $b$, $c$; a vertex move removes at
least one token in total from the three faces at one vertex (one face from each opposite pair).
Let $P$ be the set of positions with $a = A$, $b = B$ and $c = C$. Then no vertex move leads
from a position in $P$ to a position in $P$, and from every position not in $P$ some vertex
move leads to a position in $P$.

Since every play terminates, these two properties make $P$ the set of P-positions
(second-player wins) under normal play.

## Sources

- Balaji R. Kadam and A. J. Shaiju, *Variations of the Nim Game Played on a Cube*, INTEGERS 25 (2025), Article G2, Theorem 2.

Stated but not proved: `MetaMathlibExt.cubeVertexNim_pPositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/CubeRotationNimWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CubeRotationNimWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html#cube-vertex-nim-p-positions).

## P-positions of edge Nim on a cube

Write positions of the game $C_E$ as tuples
$(a, b, c, A, B, C)$ of numbers of tokens on the faces $f_a, f_b, f_c, f_A, f_B, f_C$, where
$f_A$, $f_B$, $f_C$ are opposite $f_a$, $f_b$, $f_c$, and let $\oplus$ be the Nim-sum (bitwise
exclusive or) of natural numbers. Let $\mathcal P$ be the set of positions with
$a \oplus A = b \oplus B = c \oplus C$. Then no edge move leads from a position in $\mathcal P$
to a position in $\mathcal P$, and from every position outside $\mathcal P$ there is an edge
move to a position in $\mathcal P$.

Every move removes a token, so the game terminates and $\mathcal P$ is exactly the set of
P-positions (second-player wins) under normal play.

## Sources

- Balaji R. Kadam and A. J. Shaiju, *Variations of the Nim Game Played on a Cube*, INTEGERS 25 (2025), Article G2, Theorem 3.

Stated but not proved: `MetaMathlibExt.cubeEdgeNim_pPositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/CubeRotationNimWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CubeRotationNimWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html#cube-edge-nim-p-positions).

## Misère P-positions of vertex Nim on a cube

Write a position of the cube game as
$p = (a, b, c, A, B, C)$, the numbers of tokens on the six faces of a cube, where the faces
carrying $A$, $B$, $C$ are opposite those carrying $a$, $b$, $c$; a vertex move removes at
least one token in total from the three faces at one vertex (one face from each opposite pair).
Let $P$ be any set of positions such that $p \in P$ if and only if $p$ has a vertex move and
no vertex move from $p$ leads to a position in $P$ (the misère P-positions). Then for every
position $p$ with $a \le A$, $b \le B$, $a \le b$ and $C$ at least every entry of $p$, we have
$p \in P$ if and only if either $a = A$, $b = B$, $c = C$ and $C \ge 2$ all hold, or $p$ is one
of $(0, 0, 0, 0, 0, 1)$, $(0, 1, 1, 0, 1, 1)$ and $(1, 1, 1, 1, 1, 1)$.

## Sources

- Balaji R. Kadam and A. J. Shaiju, *Variations of the Nim Game Played on a Cube*, INTEGERS 25 (2025), Article G2, Theorem 6.

Stated but not proved: `MetaMathlibExt.cubeVertexNim_misere_pPositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/CubeRotationNimWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CubeRotationNimWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html#cube-vertex-nim-misere-p-positions).

## Misère P-positions of rotation Nim on a cube

Write positions of the game $C_R$ as tuples
$p = (a, b, c, A, B, C)$ of numbers of tokens on the faces $f_a, f_b, f_c, f_A, f_B, f_C$, where
$f_A$, $f_B$, $f_C$ are opposite $f_a$, $f_b$, $f_c$. Let $\mathcal P$ be any set of positions
such that a position lies in $\mathcal P$ if and only if it has a rotation move and every
rotation move from it leads to a position outside $\mathcal P$; this is the set of P-positions
under misère play, where the player making the last move loses. Let $p$ be a position in which
every entry is at most $C$, and $a \le A$, $b \le B$ and $a \le b$. Then $p \in \mathcal P$ if
and only if either $C \ge 2$ and $a + A = b + B = c + C$, or $p = (0, 0, 0, 0, 0, 1)$, or
$p = (1, 1, 1, 1, 1, 1)$.

## Sources

- Balaji R. Kadam and A. J. Shaiju, *Variations of the Nim Game Played on a Cube*, INTEGERS 25 (2025), Article G2, Theorem 8.

Stated but not proved: `MetaMathlibExt.cubeRotationNim_misere_pPositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/CubeRotationNimWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CubeRotationNimWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html#cube-rotation-nim-misere-p-positions).

## Misère P-positions of face Nim on a cube

Write positions of the game $C_F$ (Nim with six
heaps) as tuples $p = (a, b, c, A, B, C)$ of numbers of tokens on the faces
$f_a, f_b, f_c, f_A, f_B, f_C$, where $f_A$, $f_B$, $f_C$ are opposite $f_a$, $f_b$, $f_c$, and let
$\oplus$ be the Nim-sum (bitwise exclusive or) of natural numbers. Let $\mathcal P$ be any set
of positions such that a position lies in $\mathcal P$ if and only if it has a face move and
every face move from it leads to a position outside $\mathcal P$; this is the set of
P-positions under misère play, where the player making the last move loses. Let $p$ be a
position in which every entry is at most $C$, and $a \le A$, $b \le B$ and $a \le b$. Then
$p \in \mathcal P$ if and only if either $C \ge 2$ and $a \oplus b \oplus c \oplus A \oplus B
\oplus C = 0$, or $C < 2$ and $a \oplus b \oplus c \oplus A \oplus B \oplus C = 1$.

## Sources

- Balaji R. Kadam and A. J. Shaiju, *Variations of the Nim Game Played on a Cube*, INTEGERS 25 (2025), Article G2, Theorem 9.

Stated but not proved: `MetaMathlibExt.cubeFaceNim_misere_pPositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/CubeRotationNimWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CubeRotationNimWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html#cube-face-nim-misere-p-positions).

## P-positions of slow vertex Nim on a cube

Write a position of the cube game as
$p = (a, b, c, A, B, C)$, the numbers of tokens on the six faces of a cube, where the faces
carrying $A$, $B$, $C$ are opposite those carrying $a$, $b$, $c$. A slow vertex move is a vertex
move (removing at least one token in total from the three faces at one vertex, one face from
each opposite pair) in which each face loses at most one token. Let $P$ be the set of positions
for which $a + A$, $b + B$ and $c + C$ are all even. Then no slow vertex move leads from a
position in $P$ to a position in $P$, and from every position not in $P$ some slow vertex move
leads to a position in $P$.

Since every play terminates, these two properties make $P$ the set of P-positions of the slow
game under normal play.

## Sources

- Balaji R. Kadam and A. J. Shaiju, *Variations of the Nim Game Played on a Cube*, INTEGERS 25 (2025), Article G2, Theorem 10.

Stated but not proved: `MetaMathlibExt.slowCubeVertexNim_pPositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/CubeRotationNimWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CubeRotationNimWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html#slow-cube-vertex-nim-p-positions).

## P-positions of slow edge Nim on a cube

Write a position of the cube game as
$p = (a, b, c, A, B, C)$, the numbers of tokens on the six faces of a cube, where the faces
carrying $A$, $B$, $C$ are opposite those carrying $a$, $b$, $c$. A slow edge move is an edge
move (removing at least one token in total from two faces in different opposite pairs) in which
each face loses at most one token. Let $P$ be the set of positions for which $a + A$, $b + B$
and $c + C$ are all even or all odd. Then no slow edge move leads from a position in $P$ to a
position in $P$, and from every position not in $P$ some slow edge move leads to a position in
$P$.

Since every play terminates, these two properties make $P$ the set of P-positions of the slow
game under normal play.

## Sources

- Balaji R. Kadam and A. J. Shaiju, *Variations of the Nim Game Played on a Cube*, INTEGERS 25 (2025), Article G2, Theorem 11.

Stated but not proved: `MetaMathlibExt.slowCubeEdgeNim_pPositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/CubeRotationNimWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CubeRotationNimWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html#slow-cube-edge-nim-p-positions).

## P-positions of slow face Nim on a cube

Write a position of the cube game as
$p = (a, b, c, A, B, C)$, the numbers of tokens on the six faces of a cube. A slow face move is
a face move that removes exactly one token from one face. Let $P$ be the set of positions with
$a + b + c + A + B + C$ even. Then no slow face move leads from a position in $P$ to a position
in $P$, and from every position not in $P$ some slow face move leads to a position in $P$.

Since every play terminates, these two properties make $P$ the set of P-positions of the slow
game under normal play.

## Sources

- Balaji R. Kadam and A. J. Shaiju, *Variations of the Nim Game Played on a Cube*, INTEGERS 25 (2025), Article G2, Theorem 12.

Stated but not proved: `MetaMathlibExt.slowCubeFaceNim_pPositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/CubeRotationNimWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CubeRotationNimWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html#slow-cube-face-nim-p-positions).

## P-positions of slow rotation Nim on a cube

Write a position of the cube game as
$p = (a, b, c, A, B, C)$, the numbers of tokens on the six faces of a cube, where the faces
carrying $A$, $B$, $C$ are opposite those carrying $a$, $b$, $c$. A slow rotation move is a
rotation move (removing at least one token in total from the four faces of one rotation, that is
from the faces of two opposite pairs) in which each face loses at most one token. Let $P$ be any
set of positions such that $p \in P$ if and only if no slow rotation move from $p$ leads to a
position in $P$ (the P-positions under normal play). Then for every position $p$ with
$a \le A$, $b \le B$ and $c \le C$, we have $p \in P$ if and only if the vector of remainders
$(a, b, c, A, B, C) \bmod 2$ is one of $(0, 0, 0, 0, 0, 0)$, $(0, 0, 0, 1, 1, 1)$,
$(1, 1, 1, 0, 0, 0)$ and $(1, 1, 1, 1, 1, 1)$.

## Sources

- Balaji R. Kadam and A. J. Shaiju, *Variations of the Nim Game Played on a Cube*, INTEGERS 25 (2025), Article G2, Theorem 13.

Stated but not proved: `MetaMathlibExt.slowCubeRotationNim_pPositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/CubeRotationNimWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CubeRotationNimWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html#slow-cube-rotation-nim-p-positions).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Nim on a cube](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/nim-on-a-cube/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GameTheory/combinatorial-games/nim-on-a-cube)
