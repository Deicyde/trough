---
declaration: lemma
origin: cited
lean: Cayley.tauPair, Cayley.tau_pair
statement: formalized
proof: formalized
---

# tau_pair

For a vertex $S = (-1)^\ell R_z(2\pi k/15)\, C_3$ let $\sigma(S) = (-1)^{1-\ell} R_z(-2\pi k/15)\, C_3$. Then $\tau S = \sigma(S)$.

## Depends on

- [tau](def-tau.md)
- [noperthedron](../../the-noperthedron/definition-of-the-noperthedron/def-noperthedron.md)

## Proof

Use $\tau R_z(\alpha) = R_z(-\alpha) \tau$ and $\tau C_3 = -C_3$.

## Lean

Formalized as [`Cayley.tauPair`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.tauPair), [`Cayley.tau_pair`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.tau_pair).

## Sources

- [Noperthedron blueprint: chapters/reduction.tex, line 124](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/reduction.tex#L124)
