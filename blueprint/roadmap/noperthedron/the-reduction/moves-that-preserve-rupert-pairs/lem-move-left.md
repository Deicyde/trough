---
declaration: lemma
origin: cited
lean: Cayley.rupPair_left, Cayley.rupPair_RxPi
statement: formalized
proof: formalized
---

# Common left factor

Let $L$ be an orthogonal $3 \times 3$ matrix whose third row is $\pm e_z$. If $(R_o, R_i)$ is a Rupert pair, then so is $(L R_o, L R_i)$. In particular this holds for the half-turn $L = R_x(\pi) = \mathrm{diag}(1, -1, -1)$.

## Depends on

- [shadow](../../rupert-pairs/shadows-and-the-separation-criterion/def-shadow.md)

## Proof

The third column of $L$ is $\pm e_z$ as well, so $L$ is block diagonal and its upper left $2 \times 2$ block $\ell$ is orthogonal. Then $\pi \circ L = \ell \circ \pi$, so $\mathrm{Sh}(L R) = \ell(\mathrm{Sh}(R))$, and $\ell$ is a homeomorphism of the screen.

## Lean

Formalized as [`Cayley.rupPair_left`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.rupPair_left), [`Cayley.rupPair_RxPi`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.rupPair_RxPi).

## Sources

- [Noperthedron blueprint: chapters/reduction.tex, line 29](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/reduction.tex#L29)
