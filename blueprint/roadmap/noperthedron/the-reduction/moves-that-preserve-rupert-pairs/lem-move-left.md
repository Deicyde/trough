---
declaration: lemma
origin: cited
lean: Cayley.rupPair_left, Cayley.rupPair_Rz, Cayley.rupPair_RxPi
statement: formalized
proof: formalized
---

# Common left factor

Let $L$ be a $3 \times 3$ matrix with $\pi \circ L = \ell \circ \pi$ for some invertible linear map $\ell$ of the screen. If $(R_o, R_i)$ is a Rupert pair, then so is $(L R_o, L R_i)$. In particular this holds for $L = R_z(\gamma)$ and for the half-turn $L = R_x(\pi)$, since a rotation with $L e_z = \pm e_z$ has this property.

## Depends on

- [shadow](../../rupert-pairs/shadows-and-the-separation-criterion/def-shadow.md)

## Proof

$\mathrm{Sh}(L R) = \ell(\mathrm{Sh}(R))$, and $\ell$ is a homeomorphism.

## Lean

Formalized as [`Cayley.rupPair_left`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.rupPair_left), [`Cayley.rupPair_Rz`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.rupPair_Rz), [`Cayley.rupPair_RxPi`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.rupPair_RxPi).

## Sources

- [Noperthedron blueprint: chapters/reduction.tex, line 29](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/reduction.tex#L29)
