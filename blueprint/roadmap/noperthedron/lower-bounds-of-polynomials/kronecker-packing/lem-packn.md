---
declaration: lemma
origin: cited
lean: Cayley.Pack.packN, Cayley.Pack.packN_land, Cayley.Pack.packN_add, Cayley.Pack.packN_sub, Cayley.Pack.packN_signs, Cayley.Pack.packN_mod
statement: formalized
proof: formalized
---

# packN

Let $\mathrm{pack}(d) = \sum_{j < n} d_j 2^{W j}$ with every digit $d_j < 2^W$. Bitwise *and*, digit-wise sums and differences (when no digit over- or underflows), the extraction of the top bit of every digit, and the sum of all digits (via the remainder modulo $2^W - 1$, when that sum is below $2^W - 1$) all act digit by digit.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Induction on $n$.

## Lean

Formalized as [`Cayley.Pack.packN`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.packN), [`Cayley.Pack.packN_land`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.packN_land), [`Cayley.Pack.packN_add`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.packN_add), [`Cayley.Pack.packN_sub`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.packN_sub), [`Cayley.Pack.packN_signs`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.packN_signs), [`Cayley.Pack.packN_mod`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.packN_mod).

## Sources

- [Noperthedron blueprint: chapters/polybounds.tex, line 143](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/polybounds.tex#L143)
