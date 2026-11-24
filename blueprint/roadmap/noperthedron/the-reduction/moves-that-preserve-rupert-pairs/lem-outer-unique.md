---
declaration: lemma
origin: cited
lean: Cayley.rupPair_of_row2_eq
statement: formalized
proof: formalized
---

# Same view

Let $(R_o, R_i)$ be a Rupert pair with $R_o \in SO(3)$, and let $S \in SO(3)$ have the same third row as $R_o$. Then $(S,\ S R_o^T R_i)$ is a Rupert pair.

## Depends on

- [Common left factor](lem-move-left.md)

## Proof

The third row of $L = S R_o^T$ consists of the inner products of the third row of $S$ with the rows of $R_o$, so it is $e_z$. Apply Lemma [Common left factor](lem-move-left.md); $L R_o = S$.

## Lean

Formalized as [`Cayley.rupPair_of_row2_eq`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.rupPair_of_row2_eq).

## Sources

- [Noperthedron blueprint: chapters/reduction.tex, line 45](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/reduction.tex#L45)
