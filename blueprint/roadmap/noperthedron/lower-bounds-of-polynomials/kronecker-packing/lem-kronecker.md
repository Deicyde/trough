---
declaration: lemma
origin: cited
lean: Cayley.Pack.Layout.ev_kron, Cayley.Pack.enc_eq
statement: formalized
proof: formalized
---

# kronecker

If the exponents of $p$ fit the layout, then $p$ evaluated at the Kronecker point is $\sum_j c_j 2^{W j}$, where $c_j$ is the coefficient in slot $j$. If moreover $|c_j| < 2^{W-1}$ for all $j$, then adding $2^{W-1}$ to every slot gives a natural number whose $j$-th base-$2^W$ digit is $c_j + 2^{W-1}$.

## Depends on

- [layout](def-layout.md)

## Proof

Evaluation at the Kronecker point is a ring homomorphism, and the mixed-radix indexing is injective on the exponents that fit.

## Lean

Formalized as [`Cayley.Pack.Layout.ev_kron`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.Layout.ev_kron), [`Cayley.Pack.enc_eq`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.enc_eq).

## Sources

- [Noperthedron blueprint: chapters/polybounds.tex, line 102](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/polybounds.tex#L102)
